<h1>What is Server-Side Template Injection (SSTI)</h1>

SSTI is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.

Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, 
rather than passed in as data. This allows attackers to inject arbitrary template directives in order to manipulate the template engine, often enabling them to take complete control of the server. As the name suggests, 
server-side template injection payloads are delivered and evaluated server-side, potentially making them much more dangerous than a typical client-side template injection.

<h1>Impact</h1>

At the severe end of the scale, an attacker can potentially achieve remote code execution, taking full control of the back-end server and using it to perform other attacks on internal infrastructure.

Even in cases where full remote code execution is not possible, an attacker can often still use server-side template injection as the basis for numerous other attacks, potentially gaining read access to sensitive 
data and arbitrary files on the server.

<h1>How Do SSTI Vulnerabilities Happen?</h1>

Server-side template injection vulnerabilities arise when user input is concatenated into templates rather than being passed in as data.

Static templates that simply provide placeholders into which dynamic content is rendered are generally not vulnerable to server-side template injection. The classic example is an email that greets each user by their name, 
such as the following extract from a Twig template: 

```
$output = $twig->render("Dear {first_name},", array("first_name" => $user.first_name) );
```

<mark>This is not vulnerable to server-side template injection because the user's first name is merely passed into the template as data. </mark>

However, as templates are simply strings, web developers sometimes directly concatenate user input into templates prior to rendering. Let's take a similar example to the one above, but this time, users are able to customize 
parts of the email before it is sent. For example, they might be able to choose the name that is used: 

```
$output = $twig->render("Dear " . $_GET['name']);
```

In this example, instead of a static value being passed into the template, <mark>part of the template itself is being dynamically generated using the GET parameter name</mark>. As template syntax is evaluated server-side, this potentially 
allows an attacker to place a server-side template injection payload inside the name parameter as follows:

```
http://vulnerable-website.com/?name={{bad-stuff-here}}
```
