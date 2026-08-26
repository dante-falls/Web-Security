<h1>How To Hunt For IDORs</h1>

IDORs are an authorization issue that allow you to view or modify other user's data. This means we will need multiple testing accounts on the target. The IDOR Lab has 3 test accounts already written into the application. You can use PwnFox to
login to multiple accounts in different browser tabs.

<h2>PwnFox Burpsuite Extension</h2>

To make it easier to see which account is sending a request, I use a Burpsuite extension called "PwnFox". Pwnfox will proxify each of your browser tabs and then color code each session in Burpsuite HTTP History. For example, User-A's requests
can be highlighted as green in Burpsuite History, and User-B's requests can be highlighted as red. This is a good way to visually organize your authorization testing. See images below.

<img width="1895" height="385" alt="pwn-fox-color-coding-http-history" src="https://github.com/user-attachments/assets/97a6af1c-139f-4896-bfe5-6863c894af4c" />


<mark>I have ran into a few instances where PwnFox caused me to identify a false positive for an IDOR. You should always verify your IDOR by logging into each test account on separate machines and checking if the IDOR is still reproducible.</mark>


<h1>Reading JavaScript Files To Find API Requests</h1>

JavaScript files are a goldmine when testing for IDORs. You can read through JavaScript files in order to find API Requests and "hidden" endpoints. If you can't find any JavaScript files, try filtering for the API
endpoint in your Proxy HTTP History and also filtering for JavaScript files, only. You can also filter for parameter names, like postId, commentId, etc. For example, see the image below where I filter for JavaScript Files Only and also filter for the string "/api/posts/update". In the image, notice we find the /static/api.js file that defines all the API requests for the IDOR Lab.

<img width="1901" height="725" alt="filtering-for-javascript-files" src="https://github.com/user-attachments/assets/566e2381-3961-48a1-a89e-04152b243bc3" />


After locating a JavaScript file with some API Endpoints, we can analyze the JavaScript file and figure out how to send requests to each of the endpoints. Analyze the image below of the /static/api.js file defining how to update a post via the API.

<img width="1409" height="628" alt="analyzing-the-api-js-file" src="https://github.com/user-attachments/assets/78aba07e-7d44-4b28-a6eb-ea56cdeb01ac" />

<h2>Identifying API Requests With The Canary Technique</h2>

I believe that some IDORs are not identified because testers are not properly identifying every request where their input is used by the back-end server, especially in cases where API documentation is not available. To properly identify where your
user input is processed, you can use the canary technique. The Canary Technique is the same technique used when you're hunting for client-side injection vulnerabilities, like XSS. When you're testing for XSS, you want to know exactly where the 
front-end is processing and displaying your input. So security testers will use a long, unique string called a "canary" in their user input and then search for the canary in their Proxy HTTP History, or Browser Developer Tools. By using searchable 
input, you can see where and how the front end processes your user input.

The same rules apply for testing for IDORs. You want to use searchable user input, or Canaries, so you can search for the string in Burpsuite History and see exactly what API requests your Canary is used in. This can be useful in instances where you
don't have access to API documentation.

For example, when you send a request to create a post in the IDOR lab, you can write the post title as **"User-A-Post-Title-20394237179029034907234079891723"** and then filter for the numeric string **20394237179029034907234079891723** in Burpsuite
History in order to see what requests the string **20394237179029034907234079891723** shows up in. Sometimes, the backend server processes your user input in multiple requests, so if you can filter for your Canary then you can see all requests where
your Canary is used. See example image below where we filter for our Canary in Burpsuite History and view all the requests where our Canary is used in.

<img width="1901" height="528" alt="user-input-canary-example" src="https://github.com/user-attachments/assets/5a865ff7-cd5e-4ac8-9447-8227e0654c45" />

<h2>Test All Functionality</h2>

To identify an IDOR, we need to test all the functionality we can reach. 

<h3>Testing Post Management For IDORs</h3>

For the IDOR lab, we know we can create posts, so lets start by testing the post management process. User-A will be our Victim account and User-B will be our Attacker account. Follow this process:

<ol>
  <li>Start the IDOR lab application</li>
  <li>Start Burpsuite. It's also recommended to use PwnFox so that you can proxify each browser tab and login to each account with separate sessions</li>
  <li>Travel to http://127.0.0.1:8001/login and login as User-A</li>
  <img width="1900" height="718" alt="user-a-successfully-authenticated" src="https://github.com/user-attachments/assets/89a3c863-e567-4125-97e3-9207b552d0e0" />
  <li>Travel to http://127.0.0.1:8001/login and login as User-B</li>
  <img width="1902" height="765" alt="user-b-successfully-authenticated" src="https://github.com/user-attachments/assets/d1ab47a6-60ff-42e4-b76b-19e69ab36be5" />
  <li>As User-A, create a post and use a Canary (unique, searchable string) in the post title and post body</li>
  <img width="1909" height="751" alt="user-a-post-creation" src="https://github.com/user-attachments/assets/5ea9c957-3529-436e-af0f-8d06dcf3a0de" />
  <li>As User-A, refresh the page on http://127.0.0.1:8001/dashboard and click the "View Post" button under the post that User-A just created.</li>
  <img width="1908" height="785" alt="user-a-view-post-in-gui-2" src="https://github.com/user-attachments/assets/09260011-2089-41a0-9f80-2666269a5e83" />
  <li>As User-A, notice you can also update your post. Lets test if User-B can update User-A's post. This would be an IDOR with significant impact to user data Integrity.</li>
  <li>As User-A, update your post by changing the text in the post title and post body.</li>
  <img width="1904" height="694" alt="user-a-successfully-updates-post" src="https://github.com/user-attachments/assets/2c525996-742b-4ec9-a96f-9c7d8997ffc0" />
  <li>As User-A, refresh the page that is displaying your post and notice you successfully updated your post as User-A</li>
  <img width="1912" height="904" alt="user-a-successfully-updates-post-image-2" src="https://github.com/user-attachments/assets/de44be60-844f-437b-a6fc-23efe0ed6d21" />
  <li>Open Burpsuite HTTP History and filter for the Canary you used to create User-A's post. You should see the POST request sent to /api/posts/update that updated User-A's post. Send this request to Burpsuite Repeater</li>
  <img width="1906" height="308" alt="canary-filter-idor-lab" src="https://github.com/user-attachments/assets/609ee32b-c553-4c4a-a314-4d94c361e51e" />
  <img width="1420" height="815" alt="idor-lab-request-user-a-update-post" src="https://github.com/user-attachments/assets/8a4d0041-77e8-447f-a68d-b665d6ada7fb" />
  <li>We will now check if User-B can update User-A's post, but first we must collect User-B's sessionId cookie.</li>
  <li>Remove the Canary filter in Burpsuite History and then refresh the page on http://127.0.0.1:8001/dashboard as User-B. Collect User-B's sessionId from one of User-B's requests in Burpsuite History</li>
  <img width="1909" height="785" alt="collecting-user-b-sessionId-cookie" src="https://github.com/user-attachments/assets/3ca99dad-9beb-4260-996c-9edf96c47f17" />
  <li>As User-B, open Burpsuite Repeater and resend the POST request to update User-A's post, this is the POST request we sent to Burpsuite Repeater in Step 10. <mark>Make sure you replace User-A's sessionId with User-B's sessionId
    so we are correctly test using User-B's session</mark></li>
  <img width="1412" height="675" alt="user-b-successfully-updates-user-a-post" src="https://github.com/user-attachments/assets/be4ce388-18e7-4720-92f1-25f56fa64e29" />
  <li>As User-B, notice we get a 200 Response from the POST request we sent in Step 13 to update User-A's post.</li>
  <li>As User-A, refresh the page that is displaying your post and notice User-B successfully updated your post</li>
  <img width="1911" height="905" alt="user-a-confirms-user-b-updated-their-post" src="https://github.com/user-attachments/assets/58698225-a399-4196-beb3-0621e3573e98" />
  <li>We have now successfully identified an IDOR that allows users to update other user's posts.</li>
</ol>

<h1>Can The Attacker Access The Victim's Object Identifier In Order To Exploit The IDOR</h1>

After identifying an IDOR, you want to check if the Attacker can view the Victim's Object Identifier that the Attacker requires to exploit the IDOR. If the Attacker can gather the Victim's Object Identifier, then the Attack Complexity for the IDOR
is low. In other words, it is easy for an Attacker to exploit the IDOR and update other user's posts because all users on the blog application can see other user's postId values.

Lets check if User-B can view the Victim's postId. Follow this process:

<ol>
  <li>As User-B, send the following GET request and notice you can see User-A's postId in the response. This confirms that User-B can access the required UUID values needed to exploit the IDOR</li>
<code>
GET /api/posts/list HTTP/1.1
Host: 127.0.0.1:8001
Cookie: sessionId=42ea262c-4f9f-43b1-8a75-0d40886b33c4
</code>
<img width="1413" height="633" alt="user-b-can-view-user-a-postId-UUID-value-via-api-request" src="https://github.com/user-attachments/assets/596808c8-b720-420a-a973-9d9b89132407" />
  <li>The Attacker can also view the Victim's postId in the URL when viewing the post in the browser. See image below.</li>
  <img width="1906" height="358" alt="attacker-views-victim-postId-in-url" src="https://github.com/user-attachments/assets/fe62d328-26fd-4913-b69b-ec83a2a65211" />
</ol>


<h1>Bug Bounty Report</h1>

Now that we have identified an IDOR, it's time to submit our finding as a bug bounty report. I will do this in the "Writing-A-Report.md" section
