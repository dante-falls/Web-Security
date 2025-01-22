<h1>Level 6 - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/a2bf722f-039f-4e2e-afbd-b884cc6e9adf)

<h2>Scenario</h2>

Level 6 is an example of DOM-Based XSS. The malicious user input is used by the DOM to dynamically include a script tag with our malicious input as the source.

1. If we look at the URL, there is a URL fragment pointing to a specific source. The page seems to be trying to include a "gadget" from a specific source of /static/gadget.js

![image](https://github.com/user-attachments/assets/49121c7a-a520-4e05-9f44-9be522a4d973)

2. Let's check the page source to see if we can determine how user input in the URL is processed.

![image](https://github.com/user-attachments/assets/5fe66b37-31d5-42fd-9bb7-ce69920222d0)

<h3>ChatGippity Summary Of XSS Vulnerability In Above Script</h3>

The provided script is vulnerable to XSS because it dynamically appends <script> elements to the DOM based on attacker-controlled input, specifically the window.location.hash value. This hash value can be easily manipulated by an attacker to point to a malicious script (e.g., #evil.js), which the application loads and executes without proper validation. While the script attempts to prevent external URLs containing http:// or https://, it does not sanitize or restrict other potentially dangerous inputs, such as relative URLs, data: URLs, or JavaScript payloads. As a result, an attacker can inject arbitrary JavaScript into the application by crafting a malicious URL or using other avenues like postMessage.

3. Let's try to inject the following payload to achieve XSS:

Payload = ```data:javascript,alert('XSS')```

URL = ```https://xss-game.appspot.com/level6/frame#data:javascript,alert('XSS')```

Analyze the following image to verify that our payload successfully achieves JavaScript execution

![image](https://github.com/user-attachments/assets/2b501cc2-a540-49e1-9e77-2820cc565d25)

<h1>Congratulationz</h1>

We have now finished all of the Google XSS Challenges! Great Job!
