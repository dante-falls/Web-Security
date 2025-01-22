<h1>Level 5 - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/998f803e-d289-4a8d-9778-e3ea16d1bd6e)

<h2>Scenario</h2>

Level 4 is an example of Reflected XSS. The malicious user input is immediately reflected back to the user in the form of a clickable anchored element.

1. On the front page, users can click the "signup" button which sends them to ```https://xss-game.appspot.com/level5/frame/signup?next=confirm``` See the next 2 images.

![image](https://github.com/user-attachments/assets/874c6d1d-bb04-4bb9-a94d-8cf4b1aa902d)

![image](https://github.com/user-attachments/assets/4b0426c2-fe7b-4451-9218-e214fa9c0cb7)

2. As you can see, there is a parameter called "next=". Notice that your user input in the next parameter is sent to the server and reflected back onto the page in a clickable link called "Next>>"
   See the next 2 images where we inject "TEST69420" into the next parameter in the URL.

![image](https://github.com/user-attachments/assets/c56b05cc-c41a-489a-aee3-450711481fd6)

![image](https://github.com/user-attachments/assets/89cb0982-6237-4762-b304-967463cf1cc9)

3. Because our input is injected into an href attribute, we can actually inject a JavaScript Pseuodo Protocol like ```javascript:alert(1)``` to achieve JavaScript exeuction when the user clicks the
   "Next>>" link on the page. See the successful JavaScript execution in the next image.

![image](https://github.com/user-attachments/assets/8392b414-1979-4873-96ee-c1ed6f590e84)

4. Great job! We can now move onto the final level....Level 6.

