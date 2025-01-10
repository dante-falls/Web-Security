<h1>Reflected XSS Into HTML Context With No Encoding</h1>

This is an example of Reflected Cross Site Scripting (XSS) injected into an HTML context. User input is unsantized. Review the scenario below.

<h2>Vulnerable Blog Search Functionality</h2>
The target website is a blog. There is a search bar present on the target website. Let's try injecting javascript into the search bar to test for XSS.

![image](https://github.com/user-attachments/assets/7a723623-c262-4617-be16-b695ffc8d1de)

![image](https://github.com/user-attachments/assets/a15c1915-8d03-49f4-8369-1871bbd04f91)

![image](https://github.com/user-attachments/assets/31835ac3-3567-4f9d-8bcd-67262af2982d)

Reflected XSS has been identified in the search functionality. Let's analyze this issue. Review the URL after the XSS pops an alert on the page.

![image](https://github.com/user-attachments/assets/6e9fb8f8-7aa5-44a7-bf54-28c5dcab88b0)

As you can see in the image above, the XSS payload is reflected in the search parameter in the URL.

**https://0a4e006d04ebc3b3864ba86000a700ca.web-security-academy.net/?search=%3Cscript%3Eprompt%28%22Is+This+XSS%3F%3F%3F%22%29%3C%2Fscript%3E**

Because the user input that is injected into the **search** parameter is not sanitized in any way, the **search** parameter is vulnerable to XSS. 

Analyze the page source below.

![image](https://github.com/user-attachments/assets/da079a1b-ff48-41c8-bf57-35f499e6ec56)

Our malicious javascript that we injected into the **search** parameter is reflected in the HTML of the page. Specifically the portion of the HTML that reflects the user's search query back to them.
Here is the specific line of HTML where the malicious javascript is injected.

```
<h1>0 search results for '<script>prompt("Is This XSS???")</script>'</h1>
```

<h1>Proof Of Concept</h1>

The XSS in the following URL proves XSS on the **search** parameter.

https://0ac400b4046e86e98092fd0c00bf0097.web-security-academy.net/?search=%3Cscript%3Ealert%28%22XSS-CONFIRMED%22%29%3C%2Fscript%3E

![image](https://github.com/user-attachments/assets/8371e057-a563-4911-9f74-a13d7eff984f)
