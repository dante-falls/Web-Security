<h1>How To Detect SSTI</h1>

<h2>Fuzzing For Interesting Responses</h2>

Try fuzzing the template by injecting a sequence of special characters commonly used in template expressions, such as: 

```
${{<%[%'"}}%\
```
If an exception is raised, this indicates that the injected template syntax is potentially being interpreted by the server in some way. 
This is one sign that a vulnerability to server-side template injection may exist.


<h2>Plaintext Context</h2>

Most template languages allow you to freely input content either by using HTML tags directly or by using the template's native syntax, which will be rendered to HTML on the back-end before the HTTP response is sent. 
For example, in Freemarker, the line render('Hello ' + username) would render to something like Hello Carlos. 

During auditing, we might test for server-side template injection by requesting a URL such as:

```
http://vulnerable-website.com/?username=${7*7}
```

If the resulting output contains Hello 49, this shows that the mathematical operation is being evaluated server-side. This is a good proof of concept for a server-side template injection vulnerability.

<h2>Code Context</h2>

In other cases, the vulnerability is exposed by user input being placed within a template expression. This may take the form of a user-controllable variable name being placed inside a parameter, such as:

```
greeting = getQueryParameter('greeting')
engine.render("Hello {{"+greeting+"}}", data)
```

On the website, the resulting URL would be something like:

```
http://vulnerable-website.com/?greeting=data.username
```

RESULT: <b>Hello Carlos</b>

One method of testing for server-side template injection in this context is to first establish that the parameter doesn't contain a direct XSS vulnerability by injecting arbitrary HTML into the value:

```
http://vulnerable-website.com/?greeting=data.username<tag>
```

In the absence of XSS, this will usually either result in a blank entry in the output (just Hello with no username), encoded tags, or an error message. The next step is to try and break out of the statement 
using common templating syntax and attempt to inject arbitrary HTML after it:

```
http://vulnerable-website.com/?greeting=data.username}}<tag>
```

If this again results in an error or blank output, you have either used syntax from the wrong templating language or, if no template-style syntax appears to be valid, server-side template injection is not possible. 

<mark>Alternatively, if the output is rendered correctly, along with the arbitrary HTML, this is a key indication that a server-side template injection vulnerability is present:</mark>

```
Hello Carlos<tag>
```

<h2>Identify Specific Templating Engine</h2>

Once you have detected the template injection potential, the next step is to identify the template engine.

Although there are a huge number of templating languages, many of them use very similar syntax that is specifically chosen not to clash with HTML characters. As a result, it can be relatively simple to create probing 
payloads to test which template engine is being used.

Simply submitting invalid syntax is often enough because the resulting error message will tell you exactly what the template engine is, and sometimes even which version. For example, the invalid expression 

```
<%=foobar%>
```

triggers the following response from the Ruby-based ERB engine:

```
(erb):1:in `<main>': undefined local variable or method `foobar' for main:Object (NameError)
from /usr/lib/ruby/2.5.0/erb.rb:876:in `eval'
from /usr/lib/ruby/2.5.0/erb.rb:876:in `result'
from -e:4:in `<main>'
```

<img width="1416" height="602" alt="basic-ssti-ruby-template-engine-error-message" src="https://github.com/user-attachments/assets/a0302e66-09df-458e-9992-8c261ddd1690" />



Otherwise, you'll need to manually test different language-specific payloads and study how they are interpreted by the template engine. Using a process of elimination based on which syntax appears to be valid or invalid, you can narrow down the options quicker than you might think. A common way of doing this is to inject arbitrary mathematical operations using syntax from different template engines. You can then observe whether they are successfully evaluated. To help with this process, you can use a decision tree similar to the following:
Template decision tree

<h2>Exploitation</h2>

Once you have identified the specific templating engine, you can use resources like PayloadsAlltheThings to find payloads specific to the engine. In the below image from an example lab environment, notice we are able to run 'cat /etc/passwd' on the target system using SSTI payloads specific to the vulnerable Ruby Templating Engine.

<img width="1406" height="663" alt="basic-ssti-ruby-template-engine-remote-code-execution" src="https://github.com/user-attachments/assets/cd250c20-21fb-43cb-a225-5c3e77e7a1ff" />





