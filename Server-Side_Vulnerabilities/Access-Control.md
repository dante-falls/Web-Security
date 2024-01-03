<h1>Access Control Vulnerabilities</h1>

![What-are-the-seven-categories-of-access-control-1024x439](https://github.com/dante-falls/Web-Security/assets/29386604/1860defd-cd3b-4440-b501-fa69ea7b214a)


**ChatGPT Explanation:**

Access control vulnerabilities are security flaws that arise when a system fails to properly enforce restrictions on who can access or manipulate its resources. In the context of web security, access control is crucial to prevent unauthorized users from gaining access to sensitive information or performing actions they shouldn't be allowed to do.

Here's a generalized explanation using an example:

**Scenario: Online Banking System**

Imagine you're working on the security aspects of an online banking system, where users have different roles (e.g., regular user, teller, administrator). Each role should have specific permissions, and access to certain functionalities should be restricted based on these roles.

1. **Inadequate Authentication and Authorization:**
   - **Issue:** The system doesn't properly authenticate and authorize users.
   - **Example:** A regular user (Alice) is able to access the administrator panel by simply changing the URL or manipulating parameters in requests.
   - **Consequence:** Unauthorized access could lead to unauthorized transactions or exposure of sensitive data.

2. **Missing Function-Level Access Controls:**
   - **Issue:** The system lacks proper controls to verify if a user has the right to perform a specific action.
   - **Example:** Alice, a regular user, can transfer money to any account by manipulating the form data because the system doesn't check her actual permissions.
   - **Consequence:** Regular users might gain access to functionalities meant only for administrators, leading to security breaches.

3. **Overly Broad Permissions:**
   - **Issue:** Users have more permissions than necessary for their role.
   - **Example:** A teller has access to the customer database, including sensitive information, which is not required for their job.
   - **Consequence:** Increased risk of data breaches and privacy violations as users have unnecessary access to sensitive data.

4. **Insecure Direct Object References (IDOR):**
   - **Issue:** Lack of proper checks to ensure users can only access their own data.
   - **Example:** Alice can access other users' account details by manipulating the account number in the URL.
   - **Consequence:** Breach of confidentiality as users can access and modify data they shouldn't have access to.

<h2>Example(s)</h2>

**Scenario**: Regular users have access to administrative functionalities without proper checks.

Vulnerability: Alice, a regular user, discovers she can access the admin panel at https://insecure-blog[.]com/admin-panel and perform actions meant for administrators.

Consequence: Unauthorized users can manipulate sensitive settings and potentially disrupt the website or access confidential information.

**Scenario**: Users can access other users' blog posts without proper validation.

Vulnerability: Alice can view another user's private blog post by directly entering the post ID in the URL: https://insecure-blog[.]com/view-post?post_id=789.

Consequence: Breach of confidentiality as users can access and view content that should be restricted.

**Sources:**
1. OWASP (Open Web Application Security Project) - [Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
2. "Web Application Security: A Beginner's Guide" by Bryan Sullivan and Vincent Liu. (Book)
3. "The Web Application Hacker's Handbook" by Dafydd Stuttard and Marcus Pinto. (Book)

Understanding and addressing these access control vulnerabilities are crucial for building secure web applications, and proper implementation involves a combination of authentication, authorization, and regular security audits. Always refer to the specific security guidelines and best practices relevant to the programming languages and frameworks you are using.

<h1>⚠️Access Control Vulnerability Labs by PortSwigger👨‍🔬💻</h1>

<h1>Lab: Unprotected Admin Functionality [WITHOUT BurpSuite]</h1>

This lab has an unprotected admin panel. Solve the lab by deleting the user carlos. Using BurpSuite for this lab is inefficient because you don't need to proxy any requests to exploit the access vulnerability.

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/a8d99707-de6f-48dd-9762-84e70778c6ed)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/5cb2739f-6e7e-45a0-9ec4-b7356d9d95ff)

<h2>Finding The Vulnerable Admin Panel</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/5e13f61a-96ba-4494-8d60-a8cf1860de8b)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/21c1ef17-303d-431f-9ae2-483527608c80)

<h2>Deleting The User "Carlos" [LAB COMPLETE]</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/38788d3c-bcb4-4c4e-bbb0-ca7d788c0d30)

<h1>Lab: Unprotected Admin Functionality With Unpredictable URL [WITHOUT BurpSuite]</h1>

This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application. Solve the lab by accessing the admin panel, and using it to delete the user carlos. Using BurpSuite for this lab is inefficient because you don't need to proxy any requests to exploit the access vulnerability.

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/250cfa1a-5daf-48bd-95a8-e1e358a4fa70)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/18b7b6d2-ae60-453e-a27b-0dd631889e62)

<h2>Finding The Vulnerable Admin Panel</h2>

**First we will try to access the /administrator-panel directly through the URL. As you can see, the web server actually tries to access the requested resource, but it is "Not Found".** 

![image](https://github.com/dante-falls/Web-Security/assets/29386604/ab96a6f1-eb8a-4061-9483-107c42ab116b)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/280f644f-9378-439e-a65c-1aebd778771a)

<h2>Checking The Page Source For Clues</h2>

**You can see in the Page Source that there is some code that made it to production that actually leaks the location of the admin-panel which is: "/admin-bi19c3"**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/0689cbae-dcda-4be3-9b47-fa1b3733e63c)


<h2>Navigating To The Admin Panel ( /admin-bi19c3 ) And Deleting The User "Carlos" [LAB COMPLETE]</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/912c8cd0-e3ef-4c51-86fb-71cee94e1b7d)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/e90f2831-c3f9-487f-9c40-6b6c5a2918a3)
