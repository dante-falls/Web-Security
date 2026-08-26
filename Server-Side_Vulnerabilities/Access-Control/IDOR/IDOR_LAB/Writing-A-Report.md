<h1>How To Write A Bug Bounty Report For An IDOR Vulnerability</h1>

We previously discovered an IDOR in the IDOR Lab, see https://github.com/dante-falls/Web-Security/blob/main/Server-Side_Vulnerabilities/Access-Control/IDOR/IDOR_LAB/How-To-Hunt-For-IDORs.md

Now we can practice our Bug Bounty Report Writing by writing a mock report for the IDOR we previously discovered that allows users to update other user's posts. To properly report an IDOR, most bug bounty programs will require the following sections:

<ol>
  <li><b>Title</b> - A descriptive title for your report. I like to include the type of vulnerability, a very brief description, and the vulnerable endpoint.</li>
  <li><b>Vulnerability Type</b> - The Type of Vulnerability You Are Reporting.</li>
  <li><b>Vulnerable URL</b> - The vulnerable URL on the target. If it's an IDOR on http://127.0.0.1/api/v1/users then that is the vulnerable URL.</li>
  <li><b>Vulnerability Description</b> - A description of the vulnerability.</li>
  <li><b>Impact</b> - The security impact that your bug has for the users of the website, and or the business that operates the website. If the the bug has no security impact, then it should not be reported to a bug bounty program.</li>
  <li><b>Attack Complexity</b> - The difficulty required for an Attacker to exploit the bug.</li>
  <li><b>Setup & Steps To Reproduce</b> - Here were are describing the environment setup that the bug requires, and the exact steps the triager should take to reproduce the bug.</li>
  <li><b>Mitigation/Remediation</b> - In this section you can give recommendations that the engineering team should take to fix the bug.</li>
  <li><b>Images and/or a Video Proof Of Concept showing visual proof of the bug and the steps taken to verify the bug</b></li>
</ol>

<mark>Now let's write the IDOR report</mark>

<h2>Title</h2>

IDOR Allows Users To Update Other User's Posts Via The /api/posts/update API Endpoint

<h2>Vulnerability Type</h2>

Broken Access Control (BAC) > Insecure Direct Object References (IDOR) > Modify/View Sensitive Information(Complex Object Identifiers GUID/UUID)

<h2>Vulnerable URL</h2>

http://127.0.0.1:8001/api/posts/update

<h2>Vulnerability Description</h2>

An Insecure Direct Object Reference (IDOR) has been identified on http://127.0.0.1:8001/api/posts/update that allows authenticated users to update other user's posts. The server requires a valid postId in the request but does not conduct an
authorization check to verify if the authenticated user is the owner of the post.

<h2>Impact</h2>

This IDOR affects the Integrity of user's posts on http://127.0.0.1:8001. An authenticated attacker can update other user's posts without the victim's consent, or knowledge. This can lead to wide-spread data manipulation on the platform. 
If enough user's posts are updated without their consent, this can lead to massive user trust-loss in the platform.

<h2>Attack Complexity</h2>

The Attack Complexity is low for an Attacker to exploit this IDOR. An Attacker only requires the Victim's postId UUID, which is accessible via the API with an authenticated GET request to http://127.0.0.1:8001/api/posts/list

<h2>Setup & Steps To Reproduce</h2>

To reproduce the IDOR, you must have 2 user accounts on http://127.0.0.1:8001. User-A is my Victim account and User-B is my Attacker account.

<ol>
  <li>Open Burpsuite</li>
  <li>Travel to http://127.0.0.1:8001/login and login as User-A</li>
  <img width="1902" height="724" alt="reproduction-step-2-image" src="https://github.com/user-attachments/assets/c270fb22-61da-476a-b31d-295aaaea77e6" />
  <li>Travel to http://127.0.0.1:8001/login and login as User-B</li>
  <img width="1899" height="741" alt="reproduction-step-3-image" src="https://github.com/user-attachments/assets/4c593d03-3c59-4407-a397-7fc2b537d8f2" />
  <li>As User-A, travel to http://127.0.0.1:8001/dashboard and create a post. Write the post title as "User-A-Post-Title" and the post body as "User-A-Post-Body"</li>
  <img width="1503" height="812" alt="reproduction-step-4-image" src="https://github.com/user-attachments/assets/8a463162-6598-4ace-b71a-2f8721c8eeb4" />
  <li>As User-A, click okay on the post creation pop-up and then click the blue "View Post" button under the post you just created. You will be redirected to your post page.</li>
  <li>As User-A, refresh the page and verify your post has not yet been updated.</li>
  <img width="1674" height="860" alt="reproduction-step-6-image" src="https://github.com/user-attachments/assets/b56df77d-1567-484c-baaa-d40ced851c4e" />
  <li>User-B will now update User-A's post. Continue with the instructions</li>
  <li>As User-B, send the following GET request in order to collect the Victim's postId.</li>
  <ul><li>You must replace the {ENTER_ATTACKER_sessionId_COOKIE_HERE} placeholder with the Attacker's sessionId cookie. You can find this in Burpsuite History in requests sent by the Attacker user.</li></ul>
  <code>
GET /api/posts/list HTTP/1.1
Host: 127.0.0.1:8001
Cookie: sessionId={ENTER_ATTACKER_sessionId_COOKIE_HERE}
  </code>
  <img width="1414" height="683" alt="reproduction-step-8-image" src="https://github.com/user-attachments/assets/4a750fcc-b77e-4ab3-8a76-407aebd8362c" />
  <li>As User-B, send the following POST request in order to update User-A's post. Notice you get a 200 response, indicating User-B successfully updated User-A's post.</li>
  <ul>
    <li>You must replace the {ENTER_ATTACKER_sessionId_COOKIE_HERE} placeholder with the Attacker's sessionId cookie. You can find this in Burpsuite History in requests sent by the Attacker user.</li>
    <li>You must replace the {ENTER_VICTIM_postId_HERE} placeholder with the Victim's postId we collected in Step 8.</li>
  </ul>
  <code>
POST /api/posts/update HTTP/1.1
Host: 127.0.0.1:8001
Cookie: sessionId={ENTER_ATTACKER_sessionId_COOKIE_HERE}
Content-Type: application/json
Content-Length: 0

{"title":"Attacker-Updated-This-Post","body":"Attacker-Updated-This-Post","postId":"{ENTER_VICTIM_postId_HERE}"}
  </code>
  <img width="1415" height="638" alt="reproduction-step-9-image" src="https://github.com/user-attachments/assets/20afc26b-792c-4fb6-8631-09ee0f3a720c" />
  <li>As User-A, refresh the post page in the browser and notice User-B successfully updated User-A's post</li>
  <img width="1580" height="850" alt="reproduction-step-10-image" src="https://github.com/user-attachments/assets/101f7d65-f0c8-4b58-bd06-a9565e811d45" />
</ol>

<h2>Mitigation/Remediation</h2>

To fix this IDOR, engineers must add an authorization check to POST /api/posts/update that checks if the authenticated user is the owner of the post. If the authenticated user attempts to provide the postId of a post they do not own, the server
should respond with a 403 Access Denied response.

<h2>Video Proof Of Concept</h2>

For a real report, we would want to record our steps taken to reproduce the vulnerability and attach the video to our report. Most bug bounty programs require images and/or a video proof of concept of the vulnerability.
