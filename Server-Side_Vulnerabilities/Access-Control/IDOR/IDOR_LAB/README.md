<h1>The IDOR Lab</h1>

<mark>Me and AI built an Insecure Direct Object Reference (IDOR) lab to practice hunting for IDORs.</mark>

<img width="1911" height="853" alt="IDOR-lab-intro-image" src="https://github.com/user-attachments/assets/c51469f4-35c7-4a05-b999-15094806a266" />

<h2>What Functionality Does The Lab Have?</h2>

There isn't much functionality, but it's a blog application that allows users to:

<ol>
  <li>Create posts</li>
  <li>Comment on posts</li>
  <li>Send private messages to other users</li>
  <li>Add Friends</li>
  <li>Block Users</li>
  <li>Add Backup Email Address</li>
</ol>

<mark>There is an api.js file that you can analyze in order to understand all the functionality. There is not always a GUI option.</mark>

<h2>All Object Identifiers Are UUIDs</h2>

I tried to make the application feel decently realistic to a modern day web application, so the object identifiers are all Universally Unique Identifiers (UUIDs). The fact that all the IDORs require an un-guessable object identifier will of course
affect the attack complexity. We will talk about that later on in the **Impact** section.

<h2>Your Mission</h2>

Your mission is simple...Find all the IDORs in the lab and write a bug bounty report for each IDOR you find.

<h2>How To Get The Lab</h2>

The lab is a python flask application. I put all the files into a zip file that you can easily unzip. You should view the contents of zip files before unzipping them, you can do this by attaching the '-l' flag to the unzip command in kali linux. See images below

<img width="1182" height="790" alt="list-files-in-idor-lab-zip" src="https://github.com/user-attachments/assets/69cd3178-c124-46dd-a3bb-9e1227da2dec" />

<img width="879" height="791" alt="unzip-idor-lab-files" src="https://github.com/user-attachments/assets/a8d027bf-5d25-4a1c-bdba-9e9d2813ad28" />


<h2>How To Start The IDOR Lab</h2>

<mark>Requirements: This IDOR lab requires Python Flask</mark>

<mark>By default, the application runs in port 8001. You can change this by altering the app.py file.</mark>

To start the lab, move into the the IDOR-Lab directory and use python to start the app.py program. When the application has started, you can travel to http://127.0.0.1:8001/login in the browser and login as one of the available users. 
See images below.

<img width="1902" height="716" alt="start-the-idor-lab" src="https://github.com/user-attachments/assets/20e118da-58e0-4c9e-9394-e6d5c081b8c8" />

<img width="1910" height="603" alt="idor-lab-login-screen" src="https://github.com/user-attachments/assets/9a9954bc-6c8f-460a-8b3e-4e19be75fc63" />

<h2>Application File Structure</h2>

Here is the application file structure. See image below.

<img width="1079" height="739" alt="idor-lab-file-tree" src="https://github.com/user-attachments/assets/f04fabea-3194-46e9-8656-cd1aef6711a0" />


