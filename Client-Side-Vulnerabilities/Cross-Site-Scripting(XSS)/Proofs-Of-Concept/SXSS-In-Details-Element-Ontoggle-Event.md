<h1>Stored XSS In A HTML Details Element With An Ontoggle Event</h1>

XSS Is Possible within an html details element with an ontoggle= event. Analyze the example below where an attacker injects malicious html that causes a javascript alert on the victim's screen once the victim clicks the toggle (play) button.

<h2>Attacker Injects the malicious HTML</h2>

![image](https://github.com/user-attachments/assets/a48cb7ae-943a-4428-a3c2-1976089cac63)

<h2>A victim user clicks the toggle (play button) in the malicious comment</h2>

![image](https://github.com/user-attachments/assets/cf97bd3c-5d42-49a9-aec6-2351e4c9d922)

<h2>The victim sees a JavaScript alert pop up on their screen, confirming Stored XSS is possible</h2>

![image](https://github.com/user-attachments/assets/28379a29-0abb-47c3-814b-bf078675656d)

<h2>This is the html that caused the JavaScript Execution</h2>

```
<details ontoggle="prompt('XSS-Confirmed-with-ontoggle-event-in-details-element')"><summary>Click The &#9654; To Hear A Cool Little Song </summary></details>
```
