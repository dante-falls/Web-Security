<h1>XSS Achieved In File Input Functionality</h1>

When input isn't properly sanitized, attackers may be able to achieve XSS by uploading HTML that displays a file browsing button on the screen that let's users pick a file to upload. Once the user
uploads their file, the JavaScript is executed.

Analyze the following scenario: An attacker finds that input is not sanitized in the comment section of a user's blog. The attacker then writes a comment that includes malicious HTML that pressures other
users to click the file browse button and choose their favorite cat pictures to share in the comments. Once a victim user clicks the file browse button and chooses a file to open, JavaScript is executed 
in their browser, and an alert message pops up on their screen. See the images below.

<h2>An Attacker Injects Malicious HTML That Includes A File Browsing Button, Requesting That Users Upload Cat Pictures</h2>

![image](https://github.com/user-attachments/assets/045b7640-affd-426f-a194-f056240a7b16)

![image](https://github.com/user-attachments/assets/9f990a60-1f68-4b11-9289-03add413c3ab)

<h2>A Victim User Sees The Highlighted Text And Decides To Click Browse And Choose A Cat Picture To Upload</h2>

![image](https://github.com/user-attachments/assets/6250230c-2a5a-490c-8a37-4fe6c83b6e78)

![image](https://github.com/user-attachments/assets/013190ec-257b-4501-b3f3-a72dade61c05)

<h2>When The User Finally Clicks Open, Or Double Clicks On Their Selected File, The JavaScript Will Execute And They Will See An Alert Popup</h2>

![image](https://github.com/user-attachments/assets/1c7a282f-c211-4b66-9a74-d7b080b86b52)

<h2>Page Source Shows That Injected HTML Is Not Sanitized</h2>

![image](https://github.com/user-attachments/assets/f7fd5bd7-07fd-40d2-8e6a-6afbfc494a5c)

<h2>HTML To Achieve XSS In File Input Functionality</h2>

```
<input/type="file"/onchange=prompt('XSS-Confirmed-In-File-Input-Functionality')>
```

<h2>Less User Interaction</h2>

This XSS attack can also be achieved with less user interaction by using the onclick or the onmouseover event handlers. With the onclick event handler, as soon as the user clicks the 
file "Browse" button, the JavaScript will execute. With the onmouseover event handler, whenver the user hovers over the "Browse" button, the JavaScript will execute. Analyze the HTML below:

<h3>onclick event handler</h3>

```
<input/type="file"/onclick=prompt('XSS-Confirmed-In-File-Input-Functionality')>
```

<h3>onmouseover event handler</h3>

```
<input/type="file"/onmouseover=prompt('XSS-Confirmed-In-File-Input-Functionality')>
```
