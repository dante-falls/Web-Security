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

Cross Site Request Forgery happens for multiple reasons. One reason is that Gullible's Session Cookie on the video game website has SameSite attribute that allows the cookie to be used by the browser in cross-site requests. Another reason is that the video game store webserver does not use security tokens to ensure consent behind user requests (or the token protection is incorrectly configured). Let's take a better look at each of the above reasons for CSRF.

<h3>The SameSite Attribute</h3>
