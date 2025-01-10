<h1>Stored XSS into anchor href attribute with double quotes HTML-encoded</h1>

This is an example of Stored Cross Site Scripting (SXSS) injected into an anchor tag's href attribute. Double Quotation marks and Angle Brackets are HTML encoded in most cases. Review the scenario below.

<h1>Vulnerable Blog Comment Functionality</h1>

The target website is a blog. Users can leave comments on other user's blogs after filling out a form that collects the comment text, the user's name, their email address and their personal website.
Analyze the images below.

![image](https://github.com/user-attachments/assets/fa56781f-b0ae-44f4-9e33-b48a3ac49a71)
![image](https://github.com/user-attachments/assets/7698eb43-79b0-4034-89dd-bf2cc8860de9)

<mark>Let's test to see how <> and " symbols are encoded. Analyze the images below:</mark>

![image](https://github.com/user-attachments/assets/7745cfcb-82b7-4f85-ab26-bbaaca534f9a)
![image](https://github.com/user-attachments/assets/81adee23-3d0c-4c5e-868e-67edf0ce6fb4)
![image](https://github.com/user-attachments/assets/cb5ccdff-6bd2-4b60-a6b1-8ad71f79437d)


As you can see, double quotation symbols and angle brackets are html encoded in the page source. This is likely a defense against XSS. However, it is weird that we are able to input non-URL values
for our website name. We should only be able to put URL's that start with "http" or "https" as a website name.

Because we can input any value as our personal website name, let's try to input the javascript:alert(document.cookie) as our website name. Analyze the images below:

![image](https://github.com/user-attachments/assets/c4c95381-8297-4782-a5f7-8ac3ab70be9f)

As you can see in the above image, Stored XSS was achieved in the anchor tag's href attribute because user's can input any value as their personal website name.

<h1>Proof Of Concept</h1>

In the above scenario, an attacker simply needs to inject the javascript: pseudo protocol with a javascript command as their website name when leaving a comment on the blog. This should achieve Stored XSS after a user clicks on my name after I post my comment. See the below images for proof of concept.

![image](https://github.com/user-attachments/assets/bdce3077-5d80-4334-af09-4954573fbf0e)
![image](https://github.com/user-attachments/assets/2c318daf-fc91-44a8-96b7-769499a30938)







