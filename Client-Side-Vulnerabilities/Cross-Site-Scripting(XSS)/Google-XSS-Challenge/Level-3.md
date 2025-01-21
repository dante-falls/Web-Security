<h1>Level 3 - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/63082962-648b-4d98-b5d9-dbbd37ff4938)

![image](https://github.com/user-attachments/assets/ac1332e5-cc7d-482d-bcab-9437abad30af)

<h2>Scenario</h2>

Level Three is an example of DOM-Based XSS. Let's analyze the context of the JavaScript execution.

1. Because there are no forms or parameters to inject input into, we must inject our input directly into the URL. Notice that when you click Image 1, 2 or 3, the number of the image is in the URL after
   the hash (#). For example, if you click Image 1, this will be the URL: https://xss-game.appspot.com/level3/frame#1
   
![image](https://github.com/user-attachments/assets/e7142437-a252-434d-b327-6820b070369e)

2. Let's inject a random alphanumeric string "TEST69420" instead of a number and see if we break the image reflection.
   
![image](https://github.com/user-attachments/assets/23b7662c-1bdd-47da-9a13-6ccb5396788e)

3. So the value after the # likely needs to be a number. Let's analyze the page source to see how the # value in the URL is processed.

![image](https://github.com/user-attachments/assets/b6d96469-267f-4a6d-b834-ba23fc3600c7)

4. Notice that the window.location.hash object is used to create the 'num' variable. This means that whatever number is after the # in the URL will be placed into the 'num' variable. The num variable
is then used to create an HTML image tag that will display the respective image to the screen. Here is what the image tag will look like for this URL:

URL = https://xss-game.appspot.com/level3/frame#1

Image Tag = ```<img src='/static/level3/cloud1.jpg' />```

5. Let's try and break out of the image tag and display the highlighted text "TEST69420" onto the page instead. Here is the payload we will use: ```'/><mark>TEST69420</mark>```

With the above payload, the URL will be: ```https://xss-game.appspot.com/level3/frame#'/><mark>TEST69420</mark>```

![image](https://github.com/user-attachments/assets/83f98169-0337-4432-b331-6806c1c3cf08)

6. Awesome! From the above images, we can see that our payload successfully broke out of the dynamically created image tag and we were able to inject a mark tag to highlight text.
   Now let's try to inject a payload that triggers JavaScript execution. Our payload will be: ```'/><img src='a' onerror=alert(1)>```

   With the above payload, the URL will be: ```https://xss-game.appspot.com/level3/frame#'/><img src='a' onerror=alert(1)>```

![image](https://github.com/user-attachments/assets/a181ac0b-ff5b-4cbd-93cf-1f78a7111dde)

7. Awesome, we were able to achieve Javascript execution, confirming that XSS is possible because the window.location.hash object is collected and processed without any sanitization.

<h3>A Better XSS Payload</h3>
If you're smarter then me, then you realized that I did this the hard way. Obviously, when testing for XSS, we want the shortest payload possible. Because our input is dynamically injected into
a HTML img tag, we can actually just inject an onerror event handler to achieve XSS (JavaScript execution). Remember, if we inject a #1 into the URL, we will see Image 1 on the page. See URL and dynamically generated image tag, below.

URL = https://xss-game.appspot.com/level3/frame#1

Image Tag = ```<img src='/static/level3/cloud1.jpg' />```

So, instead of injecting a new image element, we can just inject this payload to achieve JavaScript Execution: ```' onerror='alert(1)'```

The URL and Generated Image Tag will then be:


URL = https://xss-game.appspot.com/level3/frame#' onerror='alert(1)'

Image Tag = ```<img src='/static/level3/cloud' onerror='alert(1)'.jpg' />```

See Successfull XSS in the image below:

![image](https://github.com/user-attachments/assets/02c2de04-672e-4745-bfe7-486964b395f9)






