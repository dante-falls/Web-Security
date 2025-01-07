<h1>CSRF where token validation depends on token being present</h1>

Scenario: I am testing the data integrity of a website located at 0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net. I want to know if any
sensitive authenticated actions on the website are vulnerable to Cross Site Request Forgery (CSRF). Let's follow the checks below to find a CSRF 
vulnerability.

1. Check the SameSite attribute of the session cookie(s).
![image](https://github.com/user-attachments/assets/015dd21e-afb2-46a7-9202-60dcc09489b4)

   As you can see, upon logging into the target website, my session cookie has the SameSite attribute set to 'None'. This means my session cookie
   can be used in cross-site requests.

2. Are there any authenticated actions that are not protected with CSRF tokens? Analyze the next 3 images showing the process of changing a user's email
   address on 0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net.

   ![image](https://github.com/user-attachments/assets/bd63943e-9045-48d5-bb6b-f23bee160603)
   ![image](https://github.com/user-attachments/assets/8cf3464b-2464-4e8c-a9c1-e378b9ebbfb2)
   ![image](https://github.com/user-attachments/assets/bef1acbd-e12e-4cda-9448-87cf9fadafa9)

   Notice in the above images that to update their email, the user must send an HTTP POST request to 0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net
   with a CSRF token included in the request. Let's try sending the same request with an invalid CSRF token. Analyze the image below.

   ![image](https://github.com/user-attachments/assets/d8e00be7-1196-40fc-a8f9-0e712577e764)

   Notice that when you send the request to update the user's email address with an invalid CSRF token, the server responds with a 400 Bad Request with the
   error message of "Invalid CSRF token". This means the server is verifying that the CSRF token in the request matches the CSRF token tied to the
   user's session. Let's try to bypass this by not including the token in the request, at all. Analyze the images below.

   ![image](https://github.com/user-attachments/assets/8c68ea6a-4c66-4595-a52a-6d11af870a74)
   ![image](https://github.com/user-attachments/assets/145d2d85-effb-4013-9a15-2db283552c7c)

   As you can see, the server accepted the request to update the user's email address without any CSRF token in the request. The user's email address was then
   successfull updated/changed. This means that the action to update a user's email address on 0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net
   is vulnerable to CSRF. Let's craft a proof of concept to showcase this found vulnerability.

   <h1>Proof Of Concept</h1>

   Because the POST request to update a user's email address can be sent without a CSRF token, we can use the same proof of concept as we would if there were
   no defenses at all. Analyze the proof of concept below. An attacker could host this proof of concept on their malicious domain, and if a user that is logged
   into 0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net visits the attacker's website, their email address will be changed on
   0ac700f10457e2fee5479a1900a50016.web-security-academy[.]net.

   ```
   <!DOCTYPE html>
<html>
<body>
      <form action="https://0ac700f10457e2fee5479a1900a50016.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="yougothacked@evil-user.net">
      </form>
    <script>
        document.forms[0].submit();
    </script>
</body>
</html>
   ```

