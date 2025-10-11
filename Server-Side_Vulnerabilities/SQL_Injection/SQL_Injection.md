<h1>What The Heck Is A SQL Injection?</h1>
<mark>Structured Query Language Injection</mark>, AKA <mark>SQL Injection</mark> is a vulnerability where unsanitized user-input is injected into a SQL Query in order to obtain information about the Database. Web Servers often interact with SQL Databases (on the backend) to display requested data, and they utilize 
user-input to determine what data is requested. For example, your website might have a filter functionality that allows users to filter their search for specific data. The website might then use that filter as an string input inside of a SQL Statement 
to query the SQL Database. If the user input from the filter parameter is not sanitized, it can be injected into the SQL Statement and query the database for information the user is not authorized to know.

Analyze An Example Of Time-Based SQL Injection Below:

In The Following SQL Injection Proof Of Concept, our server response is delayed for 10 seconds, which means we are successfully interacting with the backend SQL Database through our user-input that we inject into the 'category' parameter on the website.

Our Payload: category=Lifestyle';select+pg_sleep(10)--

<img width="1906" height="694" alt="Time-Based-SQLi_Confirmation_10_Second_Delay" src="https://github.com/user-attachments/assets/b90b366d-3ef1-4dca-870d-f9f2cdcb8d1e" />






