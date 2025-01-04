<h1>Cross Site Request Forgery (CSRF)</h1>
<h2>ALL LINKS IN THIS ARTICLE ARE FAKE, BUT DO NOT INTERACT WITH THEM</h2>

**Cross Site Request Forgery** (AKA XSRF, AKA Sea Surf, AKA Session Riding, AKA Poor Man's XSS - I made the last one up), is a web vulnerability that effects the client's browser. An attacker will host a malicious script on a domain that they control. The purpose of the script is to make any victim that visits the attacker's domain conduct an action on another website. For example, consider the scenario below:

<h3>Gullible Gets His Data Changed</h3>

A user named Gullible is shopping on a video game website called videogames-r-us[.]com. Gullible is super ready to buy the FINALLY released Grand Theft Auto 6, and all of a sudden someone from their gaming discord sends them this link gta-discounts[.]ec08b9g-abx920[.]dnshook[.]site. Gullible (the victim user) decides it is worth clicking on the suspicious link because he might get a discount on his upcoming Grand Theft Auto purchase. So Gullible clicks the link and is sent to the malicious website, where he is shown fake Grand Theft Auto discount codes. Analyze the image below to see the extremely real (but also fake) website hosting discount codes for Grand Theft Auto.

![image](https://github.com/user-attachments/assets/09722e1a-416e-4bbb-97dc-26a884389799)

Gullible spends the next 5 minutes furiously clicking the big blue button praying that it works and he get's a discount code, but to everyone's suprise, it doesn't work. When Gullible gives up and goes back to his account on the video game website, all of his billing and payment information is changed. In an insanely insecure scenario, the attacker might even be able to make Gullible pay for multiple video games and send them to the attacker's personal shipping address. Or better yet, imagine this type of attack on your banking website. An attacker might make you send all your money, or bitcoins, to his account or wallet.

The above scenario is an example of a web attack called Cross Site Request Forgery. If you are having troubles understanding the "Cross-Site" aspect of this, think about this. The attacker hosted some code on their malicious website that automatically
changes Gullible's billing and payment information on videogames-r-us[.]com. In other words, the attacker made Gullible change his information on the video game website from a **completely different website**. That is why we call it "Cross Site". This should
also help you understand the "Request Forgery" aspect of this vulnerability. When Gullible used their browser to visit the attacker's website, the attacker made Gullible's browser make a request to the video game website. The attacker **forged a request**
to the video game website from their own malicious website.

<h2>Why This Happens</h2>

Let's identify why Cross Site Request Forgery happens by identifying some HTTP requests. In the following image, notice the HTTP Request and Response. A user named 'wiener' is logging into their account on a website, and a cookie called "session" is set for them.

![image](https://github.com/user-attachments/assets/0b9cacf1-4417-447c-9048-6289863a835f)



This session cookie will be used for further session handling on the website, which allows the server to know which user is making a request. Take another look at session cookie that was set for the user 'wiener', it has a **"SameSite=None"** set as a cookie attribute. This **SameSite=None** attribute was set by the webserver, and tells the browser "This cookie can be utilized in cross-site requests". The SameSite can also be set to "Lax" and "Strict" in order to add some restrictions on the useage of the cookie by the browser, but for the purposes of this scenario, SameSite=None.

So what does SameSite=None have anything to do with Cross-Site Request Forgery? To explain that, we need some type of authenticated user action that could cause impact if exploited by an attacker. Let's choose the action for a user to update their email. If an attacker could make a user update their email to their own email address, the attacker could then use the forgot password functionality to change the victim user's password because the email will then be sent to the attacker. Analyze the HTTP Request to update a user's email address in the images below.

![image](https://github.com/user-attachments/assets/165248b8-4841-45f3-86c3-da727999d9fa)

![image](https://github.com/user-attachments/assets/359e16ba-8a3c-41c8-a12a-bdeea0a58c06)

From the images, you can see that the action to update the user's email address action is handled by a POST request to **0a08007f04e64ab080fadf5e005d0010[.]web-security-academy[.]net/my-account/change-email**. To determine which user is making this request, the webserver only looks at ONE THING...the session cookie. And the session cookie can be used by the browser in cross-site requests (remember the session cookie has SameSite=None), which means that this action to update user email addresses for **0a08007f04e64ab080fadf5e005d0010[.]web-security-academy[.]net** can be hosted on any website on the internet and the **0a08007f04e64ab080fadf5e005d0010[.]web-security-academy[.]net** webserver will still update the user's email address. This is not good because code in the pagesource of a website is not immediately visible when you visit the website, so your browser may be conducting actions in the background that you do not see.

So because the session cookie can and will be sent by the victim's browser in cross-site requests, that means that the attacker does not need to guess the session cookie, or any value for that matter. All the attacker needs to do is host a form on their own domain that updates the user's email address on **0a08007f04e64ab080fadf5e005d0010[.]web-security-academy[.]net**. Let's try this out for ourselves.

<h3>HTML Proof Of Concept</h3>

Analyze the following HTML Proof Of Concept that an attacker can host on their malicious website. When a victim goes to the attacker's website, their email address will be changed on **0a08007f04e64ab080fadf5e005d0010[.]web-security-academy[.]net**

```
<!DOCTYPE html>
<html lang="en">
    <body>
        <h1>In 6 Seconds, I Will Change Your Email Address And All Your Accounts Are Belong To Me</h1>
        <form method="POST" action="https://0a08007f04e64ab080fadf5e005d0010.web-security-academy.net/my-account/change-email">
            <input type="hidden" name="email" value="you-got-HACKED-NERD-HAHAHAHA@gmail.com">
        </form>
        <script>
            window.onload = function() {
                setTimeout(function() {
                    document.forms[0].submit();
                }, 6000);
            };
        </script>
    </body>
</html>
```

Let's see what happens when the victim user named 'wiener' visits this page. For referrence, I will include 3 images that show the victim's email address being changed after they visit my malicious webhook.site address.

**This is before the email is changed**
![image](https://github.com/user-attachments/assets/1bc6f84b-602b-4442-882b-ddf2c1ee3505)

**This is when the victim visits the attacker's website**
![image](https://github.com/user-attachments/assets/79829b6d-d049-4e06-836d-60faf44043d8)

**This is after the victim visit's the atacker's website and their email address is changed**
![image](https://github.com/user-attachments/assets/024b6409-136f-486c-9df5-80ad8a216aa9)

As you can see in the sequence of images above, the victim's email address was changed after visiting the attacker's malicious website.

<h2>Defenses Against Cross Site Request Forgery</h2>

The main idea behind Cross Site Request Forgery is that the victim user does not intend to make the request, but the browser makes the request for them anyways. So the most common defense developers use against Cross Site Request Forgery is security tokens. The idea of the security token is that the token is generated for the user's account whenever they make sensitive, authenticated requests (like changing their email address). The server uses the security tokens to verify that the user did infact make this request and therefor does want to take this action on their account. Without the security tokens, the request to change the user's email can come from any domain, whereas with the security token protection in place, the request can only come from the **server where the token was generated**. This security token protection aims to help the server determine if a user actually wants to take an action on their account.

While security tokens are a protection against Cross Site Request Forgery, sometimes these protections are not implemented correctly into the session handling. For example, let's look at an example where security tokens are required for POST requests to change email addresses, but NOT required for GET requests to change email addresses.

<h2>Incorrectly Implemented CSRF Security Token Protection</h2>

Analyze the HTTP Requests below that change the user's email address

![image](https://github.com/user-attachments/assets/2ac1ec8a-5de1-4d5b-8aba-d5b9b87365af)

![image](https://github.com/user-attachments/assets/a8a02de3-9a6d-4f38-9c56-2992ff604350)

Notice that the above POST request requires a token called "csrf", which is how the developers are implementing security token protection against Cross Site Request Forgery. The idea is that the **csrf** token in the request can only be generated on the **0afe00e80438e76787f7209f00ec00d2.web-security-academy.net** domain. So even if an attacker hosted a form to change user's email address on **0afe00e80438e76787f7209f00ec00d2.web-security-academy.net**, the request would not be successful because the **csrf** token will not be sent with the request, as it's not generated on the attacker's malicious domain.

However, the **csrf** token is only required when making POST requests that change user email addresses. Users can still use GET requests to change their email address, and there is no **csrf** token validated against GET requests to change user email addresses. Analyze the images below where a user changes their email address with a GET request that does not require the **csrf** security token.

![image](https://github.com/user-attachments/assets/846d56b1-aa93-4bd1-b3de-43c84c7f2f10)

![image](https://github.com/user-attachments/assets/31d0c1ad-7d2a-4245-81a4-890641eef5c3)

This means that  in order to make a user change their email address on **0afe00e80438e76787f7209f00ec00d2.web-security-academy.net**, an attacker can still host a form that utilizes a GET request instead of a POST request, and they will not need to include a **csrf** token in the forged request on their malicious domain. Let's test this out. I will host the GET request form to change the user's email address on a domain I own. Here is the form I will host on my malicious domain.

```
<!DOCTYPE html>
<html lang="en">
    <body>
        <h1>In 10 Seconds, I Will Change Your Email Address And All Your Accounts Are Belong To Me</h1>
        <form method="GET" action="https://0afe00e80438e76787f7209f00ec00d2.web-security-academy.net/my-account/change-email">
            <input type="hidden" name="email" value="you-got-hacked-AGAN-HAHAHAHA-NERD@gmail.com">
        </form>
        <script>
            window.onload = function() {
                setTimeout(function() {
                    document.forms[0].submit();
                }, 10000);
            };
        </script>
    </body>
</html>
```

Analyze the sequence of images below to see a victim user visit a malicious domain and then their email address is changed, once again.

**This is wiener's email address before he visits my malicious domain**
![image](https://github.com/user-attachments/assets/c5aca553-66d7-4e32-8531-3b2b13e411bb)

**This is when wiener visit's my malicious domain**
![image](https://github.com/user-attachments/assets/29bebe94-eec8-47f7-be02-1b721f9efecb)

**This is after wiener visits the malicious domain and his email address is changed**
![image](https://github.com/user-attachments/assets/06ad3c6c-c9ae-491b-a15a-32d620912962)


<h1>Summary</h1>
In summary, Cross Site Request Forgery is a way for attackers to force a victim user to make an authenticated action on their account. While Cross Site Scripting (XSS) would allow the attacker to inject arbritary javascript execution in the context of the user's browser, XSS is hard to find. However, even though your website might not be vulnerable to XSS, you might still be vulnerable to Cross Site Request Forgery which would still allow an attacker to trick user's into making authenticated actions on their account. In regards to the CIA triad, CSRF vulnerabilities effect the Integrity of user data on the web. If a victim can be forced and decieved into making authenticated actions on website A while browsing on website B, then who knows if your data on website A can be trusted. Who knows when your data on website A will be modified simply because you are browsing the internet, on a completely different website. That is why it is important to protect against Cross Site Request Forgery, or else your users won't trust your services.
