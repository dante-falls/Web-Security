<h1>JSON Web Token Attacks - FOR EDUCATIONAL PURPOSES ONLY</h1>

<h2>Server Accepts arbitrary signatures</h2>

JWT libraries typically provide one method for verifying tokens and another that just decodes them. For example, the Node.js library jsonwebtoken has verify() and decode(). Occasionally, developers confuse these two methods
and only pass incoming tokens to the decode() method. This effectively means that the application doesn't verify the signature at all.

In the following image, the application does not verify the JWT signature, allowing us to impersonate an administrator without a valid token signature.

<img width="1851" height="689" alt="jwt-no-signature-verification-allows-for-impersonation-as-admin-user" src="https://github.com/user-attachments/assets/9cd5f698-a628-4a82-9b1a-26b476d46dc5" />


<h2>Server Accepts JWT tokens with no signature</h2>

Among other things, the JWT header contains an alg parameter. This tells the server which algorithm was used to sign the token and, therefore, which algorithm it needs to use when verifying the signature.

```
{
    "alg": "HS256",
    "typ": "JWT"
}
```

JWTs can be signed using a range of different algorithms, but can also be left unsigned. In this case, the alg parameter is set to none, which indicates a so-called "unsecured JWT". Due to the obvious dangers of this, 
servers usually reject tokens with no signature. However, as this kind of filtering relies on string parsing, you can sometimes bypass these filters using classic obfuscation techniques, such as mixed capitalization 
and unexpected encodings.

<img width="1858" height="689" alt="jwt-with-no-algorithm-bypasses-signature-verification-allows-for-impersonation-as-admin-user" src="https://github.com/user-attachments/assets/a76cae0b-76c4-486e-9804-71c383c24f89" />

<h2>Bruteforcing Secret Keys With hashcat</h2>

Some signing algorithms, such as HS256 (HMAC + SHA-256), use an arbitrary, standalone string as the secret key. Just like a password, it's crucial that this secret can't be easily guessed or brute-forced by an attacker. Otherwise, they may be able to create JWTs with any header and payload values they like, then use the key to re-sign the token with a valid signature.

When implementing JWT applications, developers sometimes make mistakes like forgetting to change default or placeholder secrets. They may even copy and paste code snippets they find online, then forget to change a hardcoded secret that's provided as an example. In this case, it can be trivial for an attacker to brute-force a server's secret using a wordlist of well-known secrets. 

<ol>
  <li>Grab a valid JWT after you authenticate and try to bruteforce the secret from a wordlist. Using hashcat, the command is <code>hashcat -a 0 -m 16500 {JWT} {wordlist}</code></li>
  <img width="1890" height="90" alt="hashcat-cracked-jwt-secret-2" src="https://github.com/user-attachments/assets/30388e1b-27fa-4425-af22-3bfd88c050c8" />
  <img width="1889" height="146" alt="hashcat-cracked-jwt-secret" src="https://github.com/user-attachments/assets/4e07821c-d7ef-45d0-8bc5-4bfc4fd7ee74" />
  <li>Create a new Symmetric Token with the secret you just cracked with hashcat from the JWT</li>
  <img width="1897" height="730" alt="generate-symmetric-key-with-secret-that-we-cracked-from-jwt" src="https://github.com/user-attachments/assets/e6c11ca5-1bda-4aed-a1c2-b030a64d8a47" />
  <li>Change the "sub" in the original token and sign the modified token with your new key</li>
  <img width="1418" height="689" alt="sign-your-modified-jwt-with-the-cracked-secret" src="https://github.com/user-attachments/assets/a4978d50-ab9c-445f-a458-d20e6d8438a9" />
  <li>Notice that the server has you authenticated as an administrator with your new token.</li>
  <img width="1862" height="741" alt="successfully-impersonation-of-administration-user-via-modified-jwt" src="https://github.com/user-attachments/assets/9eccc42c-a1e7-4ad9-a7a6-3a1dc18db59d" />
</ol>

<h1>JWT header parameter injections</h1>

 According to the JWS specification, only the alg header parameter is mandatory. In practice, however, JWT headers (also known as JOSE headers) often contain several other parameters. The following ones are of particular interest to attackers.

<ul>
  <li>jwk (JSON Web Key) - Provides an embedded JSON object representing the key.</li>

  <li>jku (JSON Web Key Set URL) - Provides a URL from which servers can fetch a set of keys containing the correct key.</li>

  <li>kid (Key ID) - Provides an ID that servers can use to identify the correct key in cases where there are multiple keys to choose from. Depending on the format of the key, this may have a matching kid parameter.</li>
</ul>

These user-controllable parameters each tell the recipient server which key to use when verifying the signature.


<h2>Injecting self-signed JWTs via the jwk header parameter</h2>

The JSON Web Signature (JWS) specification describes an optional jwk header parameter, which servers can use to embed their public key directly within the token itself in JWK format. A JWK (JSON Web Key) is a standardized format for representing keys as a JSON object.

Here's an example of a JWK in a JWT Header:

```
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```

<ol>
  <li>Generate an RSA Key</li>
  <img width="1906" height="570" alt="generate-new-rsa-key" src="https://github.com/user-attachments/assets/048fe163-1769-42fb-a2bb-7eae0bc26aa0" />
  <li>Modify the "sub" section to "administrator" and click "Attack" on the Burpsuite JWT Editor Extension. Click "Embedded JWK" when prompted and then choose the RSA key you just created</li>
  <img width="1427" height="682" alt="injecting-a-self-signed-jwt-via-the-jwk-header-using-burpsuite-jwt-editor" src="https://github.com/user-attachments/assets/b1f6490d-5866-43d0-b620-c124512942f9" />
  <li>With you new JWT, access the /my-account endpoint and notice you are authenticated as the administrator (the value we put in the "sub" header)</li>
  <img width="1863" height="683" alt="impersonating-admin-with-self-signed-jwt-in-jwk-header" src="https://github.com/user-attachments/assets/ceb54dc2-a80b-4ec5-9892-d0964cf71102" />
</ol>


<h2>Injecting self-signed JWTs via the jku parameter</h2>

Some servers let you use the jku (JWK Set URL) header parameter to reference a JWK Set containing the key. When verifying the signature, the server fetches the relevant key from this URL.

<ol>
    <li>Generate a new key</li>
    <img width="1912" height="698" alt="generate-new-rsa-key-2" src="https://github.com/user-attachments/assets/79975139-78c2-4cea-8ca6-850e79d0567a" />
    <li>Host JWK Set On Your Server</li>
    <img width="1337" height="858" alt="hosting-jwk-set" src="https://github.com/user-attachments/assets/8422f3f7-5ca7-4811-a649-39c959e9f34f" />
    <li>Modify your JWT to impersonate administrator (update "sub" header), add a jku (JWK Set URL) pointing to your JWK Set, and update the kid parameter value to match your key id. Lastly sign your payload with your new key</li>
    <li>Use your new JWT Token to access /my-account and notice you are authenticated as the administrator</li>
    <img width="1420" height="688" alt="impersonating-admin-with-injected-jku-header-param" src="https://github.com/user-attachments/assets/36e0d0c6-f9f0-4a92-a07e-374cec506eed" />
</ol>

<h2>Injecting self-signed JWTs via the kid parameter</h2>

JSON Web Tokens (JWTs) often include a kid (Key ID) header parameter to help servers identify which cryptographic key to use for signature verification. Because the JWS specification does not strictly define the format of this identifier, developers frequently use arbitrary strings or file references, making the parameter susceptible to directory traversal vulnerabilities. If an attacker manipulates the kid parameter to point to an arbitrary file on the server's filesystem, they can force the application to use that file as its verification key.

This security flaw becomes particularly critical when a server supports symmetric signing algorithms, such as HS256. Attackers can exploit this by directing the kid parameter to a predictable, static file—such as the empty /dev/null file found on most Linux systems—and then signing the forged token with a matching empty string. Consequently, the server validates the untrusted signature successfully, allowing unauthorized access and full compromise of the token-based authentication mechanism.

<img width="1857" height="683" alt="path-traversal-in-jwt-kid-header-parameter-points-server-to-dev-null" src="https://github.com/user-attachments/assets/e1d9c37f-64fa-404b-b77a-61c770569b0b" />

<h2>How To Prevent JWT Attacks</h2>

You can protect your own websites against many of the attacks we've covered by taking the following high-level measures:

<ul>
    <li>Use an up-to-date library for handling JWTs and make sure your developers fully understand how it works, along with any security implications. Modern libraries make it more difficult for you to inadvertently implement them insecurely, but this isn't foolproof due to the inherent flexibility of the related specifications.</li>
    <li>Make sure that you perform robust signature verification on any JWTs that you receive, and account for edge-cases such as JWTs signed using unexpected algorithms.</li>
    <li>Enforce a strict whitelist of permitted hosts for the jku header.</li>
    <li>Make sure that you're not vulnerable to path traversal or SQL injection via the kid header parameter.</li>
    <li>Always set an expiration date for any tokens that you issue.</li>
    <li>Avoid sending tokens in URL parameters where possible.</li>
    <li>Include the aud (audience) claim (or similar) to specify the intended recipient of the token. This prevents it from being used on different websites.</li>
    <li>Enable the issuing server to revoke tokens (on logout, for example)</li>
</ul>





    


   
  

