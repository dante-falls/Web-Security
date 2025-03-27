<h1>Stored XSS In An Admin Portal</h1>

<h2>Overview</h2>

Stored-XSS can be a serious vulnerability, especially if your XSS Payloads trigger in an admin portal. Imagine your stored-blind xss payloads triggering in an admin portal, and you then recieve all of the
admin's session cookies. You could Session Hijack the administrator and cause negative effects for the website. And this all happened because someone forgot to sanitize user input somewhere.

Stored-XSS is fun to test for in Web Security, so I built a little python program that uses Flask to spin up a simple little application that let's you see what it looks like when your stored-xss payloads
trigger in an admin portal.

<h2>How To Use The Stored XSS Test Program</h2>
