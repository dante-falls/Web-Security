<h1>What is Burp Suite?</h1>

<img src="https://i.imgur.com/9aAQG1c.png" height="300%" width="300%" alt="Burp Suite Picture"/>

**This folder is dedicated to learning about Burp Suite's Community Edition (the free version). All information on this page can be found at https://tryhackme.com/room/burpsuitebasics**

<h2>What is Burp Suite?</h2>

![image](https://github.com/dante-falls/Web-Security/assets/29386604/ab40d327-ac99-40f0-a0e2-a4dd72792dad)

<h2>What can you do with Burp Suite Community Edition?</h2>

**Proxy:** The Burp Proxy is the most renowned aspect of Burp Suite. It enables interception and modification of requests and responses while interacting with web applications.

**Repeater:** Another well-known feature. Repeater allows for capturing, modifying, and resending the same request multiple times. This functionality is particularly useful when crafting payloads through trial and error (e.g., in SQLi - Structured Query Language Injection) or testing the functionality of an endpoint for vulnerabilities.

**Intruder:** Despite rate limitations in Burp Suite Community, Intruder allows for spraying endpoints with requests. It is commonly utilized for brute-force attacks or fuzzing endpoints.

**Decoder:** Decoder offers a valuable service for data transformation. It can decode captured information or encode payloads before sending them to the target. While alternative services exist for this purpose, leveraging Decoder within Burp Suite can be highly efficient.

**Comparer:** As the name suggests, Comparer enables the comparison of two pieces of data at either the word or byte level. While not exclusive to Burp Suite, the ability to send potentially large data segments directly to a comparison tool with a single keyboard shortcut significantly accelerates the process.

**Sequencer:** Sequencer is typically employed when assessing the randomness of tokens, such as session cookie values or other supposedly randomly generated data. If the algorithm used for generating these values lacks secure randomness, it can expose avenues for devastating attacks.

