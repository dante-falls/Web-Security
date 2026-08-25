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

<mark>There is an api.js file that you can analyze in order to understand all the functionality.</mark>

<h2>All Object Identifiers Are UUIDs</h2>

I tried to make the application feel decently realistic to a modern day web application, so the object identifiers are all Universally Unique Identifiers (UUIDs). The fact that all the IDORs require an un-guessable object identifier will of course
affect the attack complexity. We will talk about that later on in the **Impact** section.

<h2>Your Mission</h2>

Your mission is simple...Find all the IDORs in the lab and write a bug bounty report for each IDOR you find.
