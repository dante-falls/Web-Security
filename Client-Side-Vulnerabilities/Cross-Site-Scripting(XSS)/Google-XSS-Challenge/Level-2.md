<h1>Level Two - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/7326c501-eacd-46dc-9e12-dc3a796530b6)

![image](https://github.com/user-attachments/assets/a55cdca7-6ff1-4f80-a301-c06b06f6f0d1)

<h2>Scenario</h2>

Level Two is a Stored XSS injected into an HTML context. There is no sanitization of user input.

1. Check for input sanitization.
     - From the above image, you can see that the word 'madness' is colored pink in the comment section of the blog. That means that you can likely inject HTML tags. Let's attempt to comment
       a highlighted TEST69420 with the HTML mark tag: ```<mark>TEST69420</mark>```
![image](https://github.com/user-attachments/assets/935e7292-d02b-4e7e-8ebb-2425d95f4b96)

2. Inject JavaScript to try and trigger an alert(1)
     - Try to comment ```<img/src='a'/onerror=alert(1)>```
![image](https://github.com/user-attachments/assets/99760d2e-e107-4ceb-a5be-dbdc9642f495)

3. Analyze this script from the blog page source that shows that user input is taken from the page and processed without sanitization, which allows for JavaScript injection and execution.
![image](https://github.com/user-attachments/assets/cea7028f-9801-47db-bbd4-88f27a61cd81)

4. Celebrate the successful JavaScript execution and move on to Level 3!






