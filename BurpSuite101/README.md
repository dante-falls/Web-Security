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


<h1>The Burp Suite Interface</h1>

**Disk-based projects are only supported on Burp Suite Professional, so we can simply press "Next" to create a Temporary Project. Reference the image below.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/a97c248c-9165-4887-8484-cfb9be4460b5)

**The next page allows you to choose a configuration file to load from. I will choose "Use Burp Defaults" for this demonstration because I don't have any configuration files to load from. You can click "Start Burp" once you've figured out how you want to load up Burp Suite. Reference the image below.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/7d8de475-0a56-440f-b74c-33c3a0c0a5c1)

<h2>The Burp Suite Dashboard</h2>

**Tasks:** The Tasks menu allows you to define background tasks that Burp Suite will perform while you use the application. In Burp Suite Community, the default task is “Live Passive Crawl” and it automatically logs visited pages.

**Event log:** The Event log furnishes details on activities executed by Burp Suite, including the starting of the proxy and specifics on connections established via Burp.

**Issue Activity:** This section is specific to Burp Suite Professional. It displays the vulnerabilities identified by the automated scanner, ranked by severity and filterable based on the certainty of the vulnerability.

**Advisory:** The Advisory section provides more detailed information about the identified vulnerabilities, including references and suggested remediations. This information can be exported into a report. In Burp Suite Community, this section may not show any vulnerabilities ☹️

**Reference the image below to see the Dashboard of the Burp Suite Community Edition**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/17777fdd-0247-4b62-abd3-588d27f67af1)

<h2>Navigating The Burp Suite Interface</h2>

**To navigate the Burp Suite interface and use the different modules/tools, simply click the tabs at the top to switch in between modules. Reference the image below where I switch to the "Intruder" module.**

![image](https://github.com/dante-falls/Web-Security/assets/29386604/871e93f8-d4eb-404b-b381-14725a79c54d)


