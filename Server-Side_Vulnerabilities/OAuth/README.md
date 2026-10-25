<h1>What is OAuth?</h1>

OAuth was developed as a way to share access to specific data with applications. It works by defining a series of interactions between three distinct parties: a client application, a resource owner, and the OAuth service provider.

<ul>
  <li> Client application - The website or web application that wants to access the user's data.</li>
  <li>Resource owner - The user whose data the client application wants to access.</li>
  <li>OAuth service provider - The website or application that controls the user's data and access to it. They support OAuth by providing an API for interacting with both an authorization server and a resource server.</li>
</ul>

<h2>OAuth Flows (Grant Types)</h2>

There are numerous different ways that the actual OAuth process can be implemented. These are known as OAuth "flows" or "grant types". Two very commonly used grant types are the "authorization code" and "implicit grant".

Broadly speaking, both of these grant types involve the following stages:

<ol>
  <li>The client application requests access to a subset of the user's data, specifying which grant type they want to use and what kind of access they want.</li>
  <li>The user is prompted to log in to the OAuth service and explicitly give their consent for the requested access.</li>
  <li>The client application receives a unique access token that proves they have permission from the user to access the requested data. Exactly how this happens varies significantly depending on the grant type.</li>
  <li>The client application uses this access token to make API calls fetching the relevant data from the resource server.</li>
</ol>

<h2>Authorization Code Grant</h2>

Uses a secure server-to-server ("backchannel") exchange. The browser only ever sees a short-lived, single-use code, keeping sensitive tokens hidden from the client-side environment.

<img width="839" height="608" alt="oauth-authorization-code-flow-diagram" src="https://github.com/user-attachments/assets/fa90bbc5-7c4b-4c70-b583-e2f205f0748f" />


<ol>
  <li>The Authorization Request: The client application redirects the user's browser to the authorization server, specifying response_type=code, along with a client ID, redirect URI, and a code challenge (PKCE).</li>
  <li>Authentication & Consent: The user logs into the authorization server (e.g., Google or Okta) and approves the requested scopes.</li>
  <li>The Code Return: The authorization server redirects the user's browser back to the client app's callback endpoint, passing a temporary authorization code in the URL query parameters (/callback?code=AUTH_CODE_123).</li>
  <li>The Backchannel Exchange: The client app's backend server takes that authorization code and makes a direct, secure server-to-server API call back to the authorization server, presenting the code and its client secret.</li>
  <li>Token Delivery: The authorization server validates the code and secret, then issues the Access Token directly to the backend server where it remains safe from browser-based inspection.</li>
</ol>

<h2>Implicit Grant</h2>

Skips the backend exchange and hands the sensitive access token directly to the user's browser via the URL fragment.

<img width="834" height="491" alt="oauth-implicity-grant-flow-diagram" src="https://github.com/user-attachments/assets/69f91e42-f13d-4109-a184-859304c32a0a" />


<ol>
  <li>The Token Request: The client application redirects the user's browser to the authorization server, specifying response_type=token (asking for the access token directly instead of a code).</li>
  <li>Authentication & Consent: The user logs in and approves the request on the authorization server.</li>
  <li>Direct Token Return: The authorization server generates the Access Token immediately and appends it directly to the redirect URL's hash fragment sent back to the browser (/#access_token=SECRET_TOKEN_XYZ).</li>
  <li>Frontend Capture: Client-side JavaScript running in the victim's browser parses the token out of the URL fragment (document.location.hash) to store it in local storage or memory.</li>
</ol>

