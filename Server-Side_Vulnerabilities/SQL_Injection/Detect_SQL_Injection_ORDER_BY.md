<h1>What The Heck Is SQL Injection In An ORDER BY Clause? - FOR INFORMATIONAL PURPOSES ONLY</h1>
<mark>According To Portswigger:</mark> If user-supplied data is being inserted into the structure of the SQL query itself, rather than an item of data within the query, exploiting SQL injection simply involves directly 
supplying valid syntax. No "escaping" is required to break out of any data context. The most common injection point within the SQL query structure is within an ORDER BY clause. The ORDER BY keyword takes a 
column name or number and orders the result set according to the values in that column. This functionality is frequently exposed to the user to allow sorting of a table within the browser.

<h1>How The Heck Do I Detect SQL Injection In An ORDER BY Clause?</h1>

1. First we need to find an area of the application that lets us sort displayed information on the page. I've seen this a few times as a URL parameter such as 'order_by', 'order' or 'sort'. Let's analyze this
webserver that allows us to sort our To-Do list by Date, Title and Status (completed or not). In our lab-instance, the webserver utilizes a parameter called 'order' to sort the user's To-Do List.

<h3>Below is an image of us sorting our To-Do List by Title</h3>

<img width="1912" height="702" alt="sqli-orderby-find-sorting-parameter" src="https://github.com/user-attachments/assets/bee770c4-1ed5-48ab-8c05-8233441fc0b0" />

2. Next we need to determine if our input is being injected into a SQL Query. Luckily for us, in our lab-instance, we get a nice Internal Server Error when we inject a ' symbol into the 'order' parameter. This
   is a nice indicator that our input is being used in a SQL Query.

<h3>Below is an image of the Internal Server Error from step 2</h3>

<img width="1907" height="703" alt="sqli-orderby-identify-sql-error" src="https://github.com/user-attachments/assets/6c676229-4c12-4a1a-92e9-e57355121b5a" />

3. Now that we know we are in SQL Query and our input effects the order of the displayed tasks, this is a strong indicator that we are injecting input into an ORDER BY Clause via the 'order' parameter.

4. Let's attempt to enumerate the number of columns until we get an error. We can do this by injecting numerical values into the 'order' parameter instead of a string. Let's inject a range of numbers from 1
   through 100 until we get an error. This will tell us the maximum number of columns shown in the response. In our case, we get an error when we send 'order=5', so we know the max number of columns is 4.

<img width="1916" height="694" alt="sqli-orderby-enumerate-max-number-of-columns" src="https://github.com/user-attachments/assets/382b593c-8989-41f2-9089-ca61b0d095ad" />


5. Let's further verify SQL Injection in the ORDER BY Clause by attempting to effect the sorting of data with "ASC" and "DESC". Sending 'order=title+asc' will display my to-do list in ascending order by
   title. Sending 'order=title+desc' will show my to-do list in descending order by title. Analyze the images below to see this behavior


<img width="1911" height="740" alt="sqli-orderby-ascending-order" src="https://github.com/user-attachments/assets/a559a50a-6ac7-4516-8564-a652857c833d" />

<img width="1907" height="699" alt="sqli-orderby-descending-order" src="https://github.com/user-attachments/assets/d722b90b-1aab-46ac-be9c-7518641d661a" />



<h1>How The Heck Do I Exploit SQL Injection In An ORDER BY Clause?</h1>

To use the SQL Injection in the ORDERY BY Clause to gather information from the database, we can use conditional responses. In our lab-instance, we'll use conditional responses to infer the first letter of the flag located in
the 'flag' table under the 'flag' column. We'll send the following payload: <mark>order=(case+when+((select+substring(flag,1,1)+from+flag)='f')+then+title+else+date+end)</mark>

Notice that in the below images, the server responds with a to-do list that is sorted by title, which let's us know the first character in the flag is 'f'. I'll also show what happens when we ask the server if
the first character in the flag is 'a' (which we know to be false) so we can show the difference between a true and false condition.

<h3>To-Do List Sorted by Title - first character in flag = 'f'</h3>

<img width="1911" height="691" alt="sqli-orderby-exploit-true-condition" src="https://github.com/user-attachments/assets/d6e8ed84-3844-4d72-9b8c-3572540c076d" />

<h3>To-Do List Sorted by Date - fist character in the flag is not 'a'</h3>

<img width="1910" height="697" alt="sqli-orderby-exploit-false-condition" src="https://github.com/user-attachments/assets/3eb433e3-afc6-4fbe-af8d-1ae41feb63cc" />


<h1>Resources To Learn SQL Injection In An ORDER BY Clause</h1>

https://portswigger.net/support/sql-injection-in-the-query-structure - Informational Resource That Will Explain SQL Injection In An ORDER BY Clause

https://tryhackme.com/room/prioritise - This is a great TryHackMe Room that involves SQL Injection in an ORDER BY Clause
