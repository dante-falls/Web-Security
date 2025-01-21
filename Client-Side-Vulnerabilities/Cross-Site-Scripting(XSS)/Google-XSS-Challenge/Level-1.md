<h1>Level One - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/e61adddd-2a8e-4a72-b229-5047aa5d177f)


<h2>Scenario</h2>

Level One is a Reflected XSS injected into an HTML context. There is no sanitization of user input.

<h2>Testing For XSS In This Scenario</h2>

1. Check for input sanitization
     - inject ~!@$%^&*()_-={}[]|\:;"'<>?,./# into search bar to see how special characters are processed
![image](https://github.com/user-attachments/assets/98437fc9-e5b9-42d4-a11a-cba426d1dcdd)

2. Check for restrictions on HTML Elements. Are HTML tags blocked?
     - inject a highlighted TEST69420 using the mark tag.
![image](https://github.com/user-attachments/assets/09b2f385-c5c3-431e-8bfb-2861876d61cd)

3. Try to trigger a javascript alert(1)
     - inject <img/src='a'/onerror=alert(1)> 
![image](https://github.com/user-attachments/assets/85d3a2ef-3637-4c78-a7c3-2219b6406431)

4. Celebrate the successful JavaScript execution and move on to Level 2!
