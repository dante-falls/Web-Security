<h1>What is a Web Socket?</h1>

<img width="1536" height="634" alt="websocket-connection" src="https://github.com/user-attachments/assets/17182d51-e35d-4ad5-9588-f11b77c4b617" />


WebSockets are a bi-directional, full duplex communications protocol initiated over HTTP. They are commonly used in modern web applications for streaming data and other asynchronous traffic.

<h2>What is the difference between HTTP and WebSockets?</h2>

Most communication between web browsers and web sites uses HTTP. With HTTP, the client sends a request and the server returns a response. Typically, the response occurs immediately, and the transaction is complete. Even if the network connection stays open, this will be used for a separate transaction of a request and a response.

Some modern web sites use WebSockets. WebSocket connections are initiated over HTTP and are typically long-lived. Messages can be sent in either direction at any time and are not transactional in nature. The connection will normally stay open and idle until either the client or the server is ready to send a message.

WebSockets are particularly useful in situations where low-latency or server-initiated messages are required, such as real-time feeds of financial data.

<h2>How are Web Sockets Established?</h2>

WebSocket connections are normally created using client-side JavaScript like the following:

<code>var ws = new WebSocket("wss://normal-website.com/chat");</code>

<mark>The wss protocol establishes a WebSocket over an encrypted TLS connection, while the ws protocol uses an unencrypted connection.</mark>
