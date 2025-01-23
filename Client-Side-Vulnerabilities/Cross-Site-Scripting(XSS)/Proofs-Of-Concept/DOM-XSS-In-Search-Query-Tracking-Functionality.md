<h1>DOM-XSS In Search Query Tracking Functionality</h1>

This lab is an example of Document Object Model (DOM) XSS. Administrators wanted to track user searches on the website so they use the search query inputted by the user to dynamically create an img tag
which we can break out of to achieve XSS.

Let's start up the lab.

![image](https://github.com/user-attachments/assets/f278d8af-b781-42a7-9071-9770de53bf25)

<h2>Blog Home Page</h2>

![image](https://github.com/user-attachments/assets/7cb86cda-e8dc-4a55-ba0e-148a1672fd43)

There is a search bar on the home page. Let's see how user input is handled in the search bar. I will inject ```~!@$%^&*`()_-={}[]|\:;"'<>?,./#``` and then we will inspect both the Page Source and the DOM.

<h3>Special Character Injection Test</h3>

![image](https://github.com/user-attachments/assets/a443e7b8-f0d0-4762-865d-718908d2acaf)

<h4>Broken HTML</h4>
It seems that our query is breaking the HTML on the page. Notice that part of my special character query is reflected onto the page under the search bar. Let's look at the page source to see if there is anything that can explain this.

<h3>Page Source</h3>

![image](https://github.com/user-attachments/assets/cd3c3182-80a0-497a-824e-d6a87db74e36)

<b>It looks like there is a script that dynamically creates an image tag with the user's search query. Let's check out the DOM to analyze img tag created in the DOM</b>

<h3>Document Object Model (DOM)</h3>

So that we can clearly see what is injected into the DOM with the document.write() sink, I will search "TEST69420" in the search bar. Let's inspect the DOM after searching TEST69420 in the search bar.

![image](https://github.com/user-attachments/assets/f460fe66-9589-487d-9fa2-a2639b06766e)

<h3>Context Breakout To Achieve XSS</h3>

Now that we know that the DOM is creating an img tag with out user input, let's try to breakout of the img tag and create a new HTML element with an event handler that triggers an XSS alert(1).

<mark>This payload will breakout of the dynamically created image tag and achieve XSS</mark> ```"><svg/onload=alert(1)>```

Analyze the following images where we achieve XSS with the above svg payload injected into the search parameter in the URL.

![image](https://github.com/user-attachments/assets/a21e56d1-4555-4c55-8860-d1fb42d950dc)

![image](https://github.com/user-attachments/assets/d8b4ba98-2f30-45b6-9e03-243845010bc7)

<h4>DOM Analysis After Successful XSS</h4>

![image](https://github.com/user-attachments/assets/c620635a-1ada-45ea-8775-df802bbcb20e)

<b>Notice that after we inject our payload into the search parameter in the URL and the DOM loads the page, an entirely new <svg> element with our alert(1) payload is created.
