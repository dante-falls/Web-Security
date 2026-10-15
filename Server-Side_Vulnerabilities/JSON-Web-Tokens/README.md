<h1>What Is A JSON Web Token (JWT)?</h1>

A JSON Web Token (JWT) is a way of communicating claims between two parties. Imagine a theme park trying to conduct access control to certain rides. Instead of keeping a giant book with each person's ride permissions, they just
give each person a wrist band when they pay for their tickets. If the person has a certain wrist band, they are conveying that they do or do not have access to certain rides. This is also how JWT's work.

For Web Servers, JWT's allow for easy access control. It tells the server that you are 1. authenticated, and 2. what permissions you have to access server resources. The JWT tells the server who you are and what type of user
you are.

A JWT consists of three parts:

1. **The Header**: Contains metadata about the token, typically the signing algorithm (alg, e.g., HS256, RS256) and the token type (typ: JWT)

2. **The Payload**: Contains the claims (the actual data), such as user ID, username, role (sub, name, admin=false, expiration time exp)

3. **The Signature**: Created by taking the encoded header, encoded payload, a secret key (or private key), and applying the hashing algorithm specified in the header. It ensures integrity—proving the token wasn't modified by the client

Analyze the below image

<img width="1408" height="768" alt="structure-of-a-json-web-token" src="https://github.com/user-attachments/assets/18290b58-2411-4cb5-8f64-9dae8c68cf33" />

