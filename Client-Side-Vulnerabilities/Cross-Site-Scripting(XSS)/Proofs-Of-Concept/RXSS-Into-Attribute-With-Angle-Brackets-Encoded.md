<h1>Reflected XSS into attribute with angle brackets HTML-encoded</h1>

This is an example of Reflected Cross Site Scripting (XSS) injected into an HTML attribute. Angle Brackets are HTML Encoded. Review the scenario below.

<h2>Vulnerable Blog Search Functionality</h2>

The target website is a blog. There is a search bar present on the target website. Let's try injecting HTML into the search bar. I will try to inject a highlighted <mark>TEST69420</mark> into the search 
bar. Analyze the images below. I will also include the page source to show if anthing in our input is being encoded by the webpage.

![image](https://github.com/user-attachments/assets/b17c379a-9520-4ab5-ace2-ec38945f09a3)
![image](https://github.com/user-attachments/assets/6b125864-4ef3-49cd-b715-7ba433421325)
![image](https://github.com/user-attachments/assets/751740ae-de49-4f02-932a-c8a56f1ce6aa)

As you can see, the angle brackets "<>" are HTML encoded in the page source. This means that the developers are attempting to sanitize user input, this is good. HOWEVER, take another look. Our input of
TEST69420 is present in a quoted attribute. View the below code block from the page source to see where our input is present.

```
<input type=text placeholder='Search the blog...' name=search value="&lt;mark&gt;TEST69420&lt;/mark&gt;">
```

Let's send an empty search to the search bar and check the page source again, I want to see the above HTML with an empty search value. Analyze the codeblock below.

```
<input type=text placeholder='Search the blog...' name=search value="">
```

Because double quotation symbols are not encoded, we can breakout of the **value=** attribute. We can break out of the quoted **value=** attribute, we can inject another attribute, such as 
**onmouseover** or **onclick** to achieve XSS. Let's try breaking out of the **value=** attribute by sending the following XSS payload to the search bar.

```
"onmouseover="alert('VALUE-ATTRIBUTE-ESCAPED-&-RXSS-CONFIRMED')
```

Theoretically, the page source with the injected XSS will look like this after we inject the above payload and escape the **value=** attribute


<mark><input type=text placeholder='Search the blog...' name=search value=""onmouseover="alert('VALUE-ATTRIBUTE-ESCAPED-&-RXSS-CONFIRMED')"></mark>


Let's test the **"onmouseover="alert('VALUE-ATTRIBUTE-ESCAPED-&-RXSS-CONFIRMED')** payload on the search bar to see if it triggers an alert.

![image](https://github.com/user-attachments/assets/7842ad93-d346-4899-ac05-988ff2e9f325)


<h1>Proof Of Concept</h1>

To prove XSS on this web target, an attacker can send this link to a victim and an alert will pop up on their screen after the javascript is executed by the victim's browser.

https://0a3e00be039edda6829724bf0033005e.web-security-academy[.]net/?search=%22onmouseover%3D%22alert%28%27VALUE-ATTRIBUTE-ESCAPED-%26-RXSS-CONFIRMED%27%29

