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

![image](https://github.com/user-attachments/assets/3b0f6d56-d3b9-4c9b-b057-2578fe6587f9)
