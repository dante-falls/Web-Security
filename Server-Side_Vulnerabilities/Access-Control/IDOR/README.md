<h1>Insecure Direct Object Reference (IDOR)</h1>

Sometimes, web applications organize data with object identifiers. An object identifier can tell a server what data you want to retrieve, or modify. For example, you might have seen parameters in the URL, or in the request body that look like
**userId=1**, **"customer_id":"a5b72252-3b3c-4106-ac23-48f43bdd3f7b"**, or **invoiceId=TS2092340710**

<img width="1419" height="633" alt="idor-readme-image" src="https://github.com/user-attachments/assets/2cba9dd3-88ec-46c0-acc8-dc5ce3c8f96c" />


These are Object Identifiers that tell the server what data you want to retrieve or modify. If you change the object identifier and retrieve or modify another user's data, then this is an Insecure Direct Object Reference, or an IDOR for short. 
The server should have access control checks in place to ensure you can only access data that you are authorized to access.

