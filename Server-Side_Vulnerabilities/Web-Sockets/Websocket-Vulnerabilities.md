<h1>WebSockets Security Vulnerabilities</h1>

In principle, practically any web security vulnerability might arise in relation to WebSockets:

<ul>
  <li>User-supplied input transmitted to the server might be processed in unsafe ways, leading to vulnerabilities such as SQL injection or XML external entity injection.</li>
  <li>Some blind vulnerabilities reached via WebSockets might only be detectable using out-of-band (OAST) techniques.</li>
  <li>If attacker-controlled data is transmitted via WebSockets to other application users, then it might lead to XSS or other client-side vulnerabilities.</li>
</ul>

<mark>The majority of input-based vulnerabilities affecting WebSockets can be found and exploited by tampering with the contents of WebSocket messages.</mark>

<h2>XSS Via A Websocket Message - Chat Functionality</h2>

Suppose you are using an application that uses websocket messages when users send chat messages to eachother.

```{"message":"Wuzzzaaaaaaa6942031337"}```

then the user's message would show in the chat box as:

```<td>Wuzzzaaaaaaa6942031337</td>```

An attacker might try to achieve XSS in a victim's browser by sending the following XSS payload as a websocket message:

```{"message":"<img/src/onerror=alert('xss-in-a-websocket-message')>"}```

<img width="1905" height="342" alt="xss-in-a-websocket-message-educational-example" src="https://github.com/user-attachments/assets/72c74bc4-c51f-4887-8e75-a82abe78f572" />
