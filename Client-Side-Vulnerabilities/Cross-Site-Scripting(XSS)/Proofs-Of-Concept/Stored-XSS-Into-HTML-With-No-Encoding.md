<h1>Stored XSS into HTML context with nothing encoded</h1>

This is an example of Stored Cross Site Scripting (SXSS) injected into an HTML context. User input is not santized or encoded in any way. Review the scenario below.

<h1>Vulnerable Blog Comment Functionality</h1>

The target website is a blog. Users can leave comments on other user's blogs after filling out a form that collects the comment text, the user's name, their email address and their personal website.
Analyze the images below.

![image](https://github.com/user-attachments/assets/e38cecce-ee03-411f-9035-8d0b7b1bdc54)

![image](https://github.com/user-attachments/assets/1598ae6c-62be-4a83-9b76-6ae03be37384)

Let's try writing a comment on someone's blog. Because we are testing for XSS, we should test to see if HTML can be injected and rendered in the comments. Analyze the images below where I attempt to
inject <mark>HELLO WORLD</mark> to see if the text is highlighted on the page.

![image](https://github.com/user-attachments/assets/9da4a16f-3703-49ca-aa5f-66ddcc4bb7ff)

![image](https://github.com/user-attachments/assets/b4f87283-beaa-4f6f-9130-0c7e7951829b)

As you can see, the text I commented is highlighted on the page. This means that HTML can be injected and rendered by the page. This is a great sign when testing for XSS.
Let's now try to inject some javascript into a comment. I will attempt to inject <script>prompt("STORED-XSS-CONFIRMED")</script> into my comment on /postId=6
Analyze the image below to see if an alert prompt displays on the screen after I post my malicious comment and refresh the page for /postId=6

![image](https://github.com/user-attachments/assets/7260a6ea-0b38-44b1-b6f0-f40585f65371)
![image](https://github.com/user-attachments/assets/5d8474d9-136e-43cc-8e34-38a5f3fe3d66)
![image](https://github.com/user-attachments/assets/9f407f1a-082a-44c5-9c14-6a14da8f977d)

<h1>Proof Of Concept</h1>
An attacker can prove Stored XSS is possible on the blog comment functionality by commenting the following payload into a comment and then posting the comment.

```
<script>prompt("STORED-XSS-CONFIRMED")</script>
```






