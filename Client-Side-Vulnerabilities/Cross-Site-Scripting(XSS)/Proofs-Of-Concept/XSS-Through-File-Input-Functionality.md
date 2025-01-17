<h1>XSS Achieved Through File Input Functionality</h1>

XSS can be achieved in an input element of type "file" when user's browse for files and click a file to upload. Analyze the scenario below.

Scenario: User's comments on blogs are not sanitized, so an attacker can inject a script that allows other users to choose a file. The JavaScript will execute when the victim user clicks 'browse',
chooses a file and then clicks 'upload'.

<h2>Attacker Injects Malicious File Input Functionality Into Another User's Blog via Comment Section</h2>

![image](https://github.com/user-attachments/assets/147c439e-72b4-4030-98c9-d1de64efba17)

![image](https://github.com/user-attachments/assets/e5a99fab-8acc-4f6d-9f52-a598e09ccc5d)

<h2>Victim User See's The File Browsing Button In The Comments And Uploads A File.</h2>

![image](https://github.com/user-attachments/assets/263ca1cd-c560-4f44-aa5d-92900069a3a5)

![image](https://github.com/user-attachments/assets/4805c7ea-5eb1-4d78-811d-bee0fa686d31)

<h2>JavaScript Executes When User Chooses A File And Clicks Upload</h2>

![image](https://github.com/user-attachments/assets/60f553ae-11e9-4340-86f0-cd6df3957e16)

<h2>Page Source With Unsanitized Malicious Input</h2>

![image](https://github.com/user-attachments/assets/cf8e6104-f74e-4b42-8c11-1ad668b60f2a)

<h2>Malicious HTML</h2>

This is the entire malicious HTML that an attacker can use to achieve XSS when user's click 'browse', choose a file and then click 'upload'.

```
<input type="file" onchange="this.setAttribute('webkitdirectory','');prompt('XSS-JavaScript-Alerts-After-User-Chooses-File')">
```





