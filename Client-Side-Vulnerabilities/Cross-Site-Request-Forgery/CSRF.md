<h1>Cross Site Request Forgery (CSRF)</h1>

**Cross Site Request Forgery** (AKA XSRF, AKA Sea Surf, AKA Session Riding, AKA Poor Man's XSS - I made the last one up), is a web vulnerability that effects the client's browser. An attacker will host a malicious script on a domain that they control. The purpose
of the script is to make any victim that visits your domain conduct an action on another website. For example, picture the scenario below:

Scenario: A user named Gullible is shopping on a video game website called videogames-r-us[.]com, ready to buy the FINALLY released Grand Theft Auto 6, and all of a sudden someone from their gaming dischord sends them this link (gta-discounts[.]ec08b9g-abx920[.]dnshook[.]site)
Gullible (the victim user) decides it is worth clicking on the suspicious link because he might get a discount on his upcoming Grand Theft Auto purchase. So Gullible goes ahead and clicks the link and is sent to the malicious website, where he is shown
fake Grand Theft Auto discount codes. Gullible spends the next 10 minutes testing each discount code, and to his suprise none of them work. When Gullible gives up and goes back to his account on the video game website, all his information is changed.

The above scenario is an example a web attack called Cross Site Request Forgery. If you are having troubles understanding the "Cross-Site" aspect of this, think about this. The attacker hosted some code on their malicious website that automatically
changes Gullible's billing and payment information on videogames-r-us[.]com. In other words, the attacker made Gullible change his information on the video game website from a completely different website. That is why we call it "Cross Site". This should
also help you understand the "Request Forgery" aspect of this vulnerability. When Gullible used their browser to visit the attacker's website, the attacker made Gullible's browser make a request to the video game website. The attacker forged a request
to the video game website from their own malicious website.

<h2>Why This Happens</h2>

