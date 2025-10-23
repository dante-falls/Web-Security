<h1>What The Heck Is NoSQL Injection? - FOR EDUCATIONAL PURPOSES ONLY</h1>

<mark>NoSQL Injection</mark> is a vulnerability where an attacker is able to interfere with the queries that an application makes to a NoSQL database. NoSQL injection may enable an attacker to:

1. Bypass authentication or protection mechanisms.
2. Extract or edit data.
3. Cause a denial of service.
4. Execute code on the server.


<h3>IMPORTANT</h3>
NoSQL databases store and retrieve data in a format other than traditional SQL relational tables. They use a wide range of query languages instead of a universal standard like SQL, and 
have fewer relational constraints.

<h1>Types Of NoSQL Injection</h1>

1. <mark>Syntax Injection</mark> - This occurs when you can break the NoSQL query syntax, enabling you to inject your own payload. The methodology is similar to that used in SQL injection. However the nature of the attack varies significantly, as NoSQL databases use a range of query languages, types of query syntax, and different data structures. Analyze the images below where we break the syntax with a ' symbol, and then fix it by injecting valid MongoDB syntax.
<img width="1903" height="698" alt="breaking-the-syntax-NoSQL" src="https://github.com/user-attachments/assets/bcf8f10d-68eb-4ed7-89c2-5a03fb70124f" />
<img width="1907" height="702" alt="fixing-the-syntax-NoSQL" src="https://github.com/user-attachments/assets/fc78c2e1-d151-4b27-ab8c-50d2da39b283" />


2. <mark>Operator Injection</mark> - This occurs when you can use NoSQL query operators to manipulate queries. Analyze the images below where we inject operators in order to log in as the administrator without knowing valid credentials.
<img width="1912" height="834" alt="json-login-invalid-admin-credentials" src="https://github.com/user-attachments/assets/633018e6-bd05-46fb-a3d2-e634739cc93c" />
<img width="1908" height="703" alt="json-login-valid-admin-credentials-with-operator-injection" src="https://github.com/user-attachments/assets/2d3ebd81-e893-45e9-9798-9562a5e1353d" />
