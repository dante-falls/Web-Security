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

<h1>Lab 1: Unprotected Admin Functionality [WITHOUT BurpSuite]</h1>

This lab has an unprotected admin panel. Solve the lab by deleting the user carlos. Using BurpSuite for this lab is inefficient because you don't need to proxy any requests to exploit the access vulnerability.

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/a8d99707-de6f-48dd-9762-84e70778c6ed)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/5cb2739f-6e7e-45a0-9ec4-b7356d9d95ff)

<h2>Finding The Vulnerable Admin Panel</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/5e13f61a-96ba-4494-8d60-a8cf1860de8b)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/21c1ef17-303d-431f-9ae2-483527608c80)

<h2>Deleting The User "Carlos" [LAB COMPLETE]</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/38788d3c-bcb4-4c4e-bbb0-ca7d788c0d30)

<h1>Lab 2: Unprotected Admin Functionality With Unpredictable URL [WITHOUT BurpSuite]</h1>

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

<h1>Lab 3: User Role Controlled By Request Parameter [WITHOUT BurpSuite]</h1>

This lab has an admin panel at /admin, which identifies administrators using a forgeable cookie. Solve the lab by accessing the admin panel and using it to delete the user carlos. You can log in to your own account using the following credentials: **wiener:peter** 

<h2>The Vulnerable Website</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/98497fdc-c666-493a-9502-7f0f536bad5a)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/bdf3c47c-49df-4bb6-a441-926d76dfc77d)

<h2>Navigating Towards The Admin Panel (/admin)</h2>

**Here we try to access the /admin page on the website and we are denied access because we are not logged in as an admin**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/810f940b-04e7-42b4-9407-7204b13e282a)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/15a50497-bcef-4d65-b446-2694fa61f345)


<h2>Logging Into Our Trusted Account wiener:peter</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/555de79e-3c29-465a-922e-0dea8e7d2312)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/9b6e69e4-4123-42a3-817f-015bac67d3a5)

<h2>Analyzing The Admin Cookie</h2>

**If you open the developer tools and look at the request that is made when you log into your account, you will notice a cookie that let's the web server determine if you are an admin or not. We can set this cookie to "true" and try to get access to the /admin page.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/18cd9509-d3a3-48db-a20c-232389193ecc)

<h2>Setting The Admin Cookie To True And Accessing The /admin page</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/400c5f78-05a2-48ff-9ed9-39ff75bc2880)

![image](https://github.com/dante-falls/Web-Security/assets/29386604/9013bba7-d160-42a2-9286-b3ec58538ecb)

![image](https://github.com/dante-falls/Web-Security/assets/29386604/e535ec80-6834-4261-9617-4731536f6ae8)

![image](https://github.com/dante-falls/Web-Security/assets/29386604/e210656c-1482-4d49-bcc0-310afea5e679)

<h2>Deleting The User "Carlos" [LAB COMPLETE]</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/3afbca62-2602-4375-8c2e-70e09e3402ff)

<h1>Lab 7: User ID controlled by request parameter with data leakage in redirect [WITH BurpSuite]</h1>

This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response. To solve the lab, obtain the API key for the user carlos and submit it as the solution. You can log in to your own account using the following credentials: wiener:peter  

<h2>The Vulnerable Website</h2>

**For this lab, I will use the Burp Proxy to intercept requests so I can manipulate the values with burp repeater. Keep in mind, I am manually forwarding all requests, but I will only show the most important requests in BurpSuite.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/d32019e1-1c82-43d1-a492-780278d26c1f)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/e252ea78-56c7-45d6-bfc3-e7fee45b17a4)

<h2>Logging Into Our Trusted Account wiener:peter</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/1c4fc5c9-18ae-4ebe-8f34-9af7dfbea17d)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/dd1b78dd-0437-4c49-9eee-783c33419f3f)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/aa5bd0d8-8117-42ae-8ddd-5eb029d24eb6)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/562bf4d8-274c-4cec-86ea-cac7701c6c6c)

<h2>Successful Login Of My Account Page With My API Key</h2>

**I have now successfully logged into my wiener:peter account and can see my API Key.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/2ba8609f-df12-489c-b596-ab8181e16e44)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/84801f72-7207-48ae-b715-87248a6921c6)

<h2>Sending the /my-account?id=wiener request to Burp Repeater so we can change the values and resend the request</h2>

**If you look at the successful /my-account?id=wiener request in the BurpSuite Proxy HTTP History, you will notice we can manipulate the GET request and try to get carlos's account, instead.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/ab8481fa-6274-41f8-a3b8-06788a3339df)

<h2>Changing the request to /my-account?id=carlos in Burp Repeater</h2>

**When you manipulate the request in Burp Repeater and send it, you will successfully get access to Carlos's acccount and API Key**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/da3a353f-1f3b-4caf-b4df-9bb6d790ed90)

<h2>Submitting Carlos's API Key [LAB COMPLETE]</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/dae86699-2060-4796-9839-c3d145e3a7c0)
![image](https://github.com/dante-falls/Web-Security/assets/29386604/08039804-8f9f-4438-afc4-ac4fadb3566e)
