<h1>Stored XSS into anchor href attribute with double quotes HTML-encoded</h1>

This is an example of Stored Cross Site Scripting (SXSS) injected into an anchor tag's href attribute. Double Quotation marks and Angle Brackets are HTML encoded in most cases. Review the scenario below.

<h1>Vulnerable Blog Comment Functionality</h1>

The target website is a blog. Users can leave comments on other user's blogs after filling out a form that collects the comment text, the user's name, their email address and their personal website.
Analyze the images below.

![image](https://github.com/user-attachments/assets/fa56781f-b0ae-44f4-9e33-b48a3ac49a71)
![image](https://github.com/user-attachments/assets/7698eb43-79b0-4034-89dd-bf2cc8860de9)

Let's test to see how <> and " symbols are encoded. Analyze the images below:

![image](https://github.com/user-attachments/assets/063e898f-2fb7-4ef0-a947-1c35cf40bbb9)
![image](https://github.com/user-attachments/assets/636864f5-04b7-4d3a-8d87-355bc333f8a1)
![image](https://github.com/user-attachments/assets/fdbe307d-af1c-4f65-bac0-213a1640dda2)

As you can see, double quotation symbols and angle brackets are html encoded in the page source. This is likely a defense against XSS. However, it is weird that we are able to input non-URL values
for our website name. We should only be able to put URL's that start with "http" or "https" as a website name.

Because we can input any value as our personal website name, let's try to input the javascript:alert(document.cookie) as our website name. Analyze the images below:

![image](https://github.com/user-attachments/assets/c4c95381-8297-4782-a5f7-8ac3ab70be9f)

As you can see in the above image, Stored XSS was achieved in the anchor tag's href attribute because user's can input any value as their personal website name.

<h1>Proof Of Concept</h1>

In the above scenario, an attacker simply needs to inject the javascript: pseudo protocol with a javascript command as their website name when leaving a comment on the blog. This will achieve Stored XSS.
See the below images for proof of concept.

![image](https://github.com/user-attachments/assets/bdce3077-5d80-4334-af09-4954573fbf0e)
![image](https://github.com/user-attachments/assets/2c318daf-fc91-44a8-96b7-769499a30938)







