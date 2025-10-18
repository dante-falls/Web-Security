<h1>SQLMAP Tamper Scripts</h1>

<h3>SEE MY FAVORITE TAMPER SCRIPTS AT THE BOTTOM</h3>

* 0eunion - Replaces instances of <int> UNION with <int>e0UNION
* apostrophemask - Replaces apostrophe character (') with its UTF-8 full width counterpart (e.g. ' -> %EF%BC%87)
* apostrophenullencode - Replaces apostrophe character (') with its illegal double unicode counterpart (e.g. ' -> %00%27)
* appendnullbyte - Appends (Access) NULL byte character (%00) at the end of payload
* base64encode - Base64-encodes all characters in a given payload
* between - Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #' and equals operator ('=') with 'BETWEEN # AND #'
* binary - Injects keyword binary where possible
* bluecoat - Replaces space character after SQL statement with a valid random blank character. Afterwards replace character '=' with operator LIKE
* chardoubleencode - Double URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %2553%2545%254C%2545%2543%2554)
* charencode - URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %53%45%4C%45%43%54)
* charunicodeencode - Unicode-URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %u0053%u0045%u004C%u0045%u0043%u0054)
* charunicodeescape - Unicode-escapes non-encoded characters in a given payload (not processing already encoded) (e.g. SELECT -> \u0053\u0045\u004C\u0045\u0043\u0054)
* commalesslimit - Replaces (MySQL) instances like 'LIMIT M, N' with 'LIMIT N OFFSET M' counterpart
* commalessmid - Replaces (MySQL) instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)' counterpart
* commentbeforeparentheses - Prepends (inline) comment before parentheses (e.g. ( -> /**/()
* concat2concatws - Replaces (MySQL) instances like 'CONCAT(A, B)' with 'CONCAT_WS(MID(CHAR(0), 0, 0), A, B)' counterpart
* decentities - HTML encode in decimal (using code points) all characters (e.g. ' -> &#39;)
* dunion - Replaces instances of <int> UNION with <int>DUNION
* equaltolike - Replaces all occurrences of operator equal ('=') with 'LIKE' counterpart
* equaltorlike - Replaces all occurrences of operator equal ('=') with 'RLIKE' counterpart
* escapequotes - Slash escape single and double quotes (e.g. ' -> \')
* greatest - Replaces greater than operator ('>') with 'GREATEST' counterpart
* halfversionedmorekeywords - Adds (MySQL) versioned comment before each keyword
* hex2char - Replaces each (MySQL) 0x<hex> encoded string with equivalent CONCAT(CHAR(),...) counterpart
* hexentities - HTML encode in hexadecimal (using code points) all characters (e.g. ' -> &#x31;)
* htmlencode - HTML encode (using code points) all non-alphanumeric characters (e.g. ' -> &#39;)
* if2case - Replaces instances like 'IF(A, B, C)' with 'CASE WHEN (A) THEN (B) ELSE (C) END' counterpart
* ifnull2casewhenisnull - Replaces instances like 'IFNULL(A, B)' with 'CASE WHEN ISNULL(A) THEN (B) ELSE (A) END' counterpart
* ifnull2ifisnull - Replaces instances like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)' counterpart
* informationschemacomment - Add an inline comment (/**/) to the end of all occurrences of (MySQL) "information_schema" identifier
* least - Replaces greater than operator ('>') with 'LEAST' counterpart
* lowercase - Replaces each keyword character with lower case value (e.g. SELECT -> select)
* luanginx - LUA-Nginx WAFs Bypass (e.g. Cloudflare)
* misunion - Replaces instances of UNION with -.1UNION
* modsecurityversioned - Embraces complete query with (MySQL) versioned comment
* modsecurityzeroversioned - Embraces complete query with (MySQL) zero-versioned comment
* multiplespaces - Adds multiple spaces (' ') around SQL keywords
* ord2ascii - Replaces ORD() occurences with equivalent ASCII() calls
* overlongutf8 - Converts all (non-alphanum) characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. ' -> %C0%A7)
* overlongutf8more - Converts all characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. SELECT -> %C1%93%C1%85%C1%8C%C1%85%C1%83%C1%94)
* percentage - Adds a percentage sign ('%') infront of each character (e.g. SELECT -> %S%E%L%E%C%T)
* plus2concat - Replaces plus operator ('+') with (MsSQL) function CONCAT() counterpart
* plus2fnconcat - Replaces plus operator ('+') with (MsSQL) ODBC function {fn CONCAT()} counterpart
* randomcase - Replaces each keyword character with random case value (e.g. SELECT -> SEleCt)
* randomcomments - Add random inline comments inside SQL keywords (e.g. SELECT -> S/**/E/**/LECT)
* schemasplit - Splits FROM schema identifiers (e.g. 'testdb.users') with whitespace (e.g. 'testdb 9.e.users')
* scientific - Abuses MySQL scientific notation
* sleep2getlock - Replaces instances like 'SLEEP(5)' with (e.g.) "GET_LOCK('ETgP',5)"
* sp_password - Appends (MsSQL) function 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs
* space2comment - Replaces space character (' ') with comments '/**/'
* space2dash - Replaces space character (' ') with a dash comment ('--') followed by a random string and a new line ('\n')
* space2hash - Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')
* space2morecomment - Replaces (MySQL) instances of space character (' ') with comments '/**_**/'
* space2morehash - Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')
* space2mssqlblank - Replaces (MsSQL) instances of space character (' ') with a random blank character from a valid set of alternate characters
* space2mssqlhash - Replaces space character (' ') with a pound character ('#') followed by a new line ('\n')
* space2mysqlblank - Replaces (MySQL) instances of space character (' ') with a random blank character from a valid set of alternate characters
* space2mysqldash - Replaces space character (' ') with a dash comment ('--') followed by a new line ('\n')
* space2plus - Replaces space character (' ') with plus ('+')
* space2randomblank - Replaces space character (' ') with a random blank character from a valid set of alternate characters
* substring2leftright - Replaces PostgreSQL SUBSTRING with LEFT and RIGHT
* symboliclogical - Replaces AND and OR logical operators with their symbolic counterparts (&& and ||)
* unionalltounion - Replaces instances of UNION ALL SELECT with UNION SELECT counterpart
* unmagicquotes - Replaces quote character (') with a multi-byte combo %BF%27 together with generic comment at the end (to make it work)
* uppercase - Replaces each keyword character with upper case value (e.g. select -> SELECT)
* varnish - Appends a HTTP header 'X-originating-IP' to bypass Varnish Firewall
* versionedkeywords - Encloses each non-function keyword with (MySQL) versioned comment
* versionedmorekeywords - Encloses each keyword with (MySQL) versioned comment
* xforwardedfor - Append a fake HTTP header 'X-Forwarded-For' (and alike)

<h1>Interesting Tamper Scripts</h1>

<h2>Time-Based Tampers</h2>
<h3><mark>--tamper=sleep2getlock,space2dash,randomcase,charencode</mark></h3>

sqlmap -u 'https://0a0e00e00384b00d8019766c000600fd.web-security-academy.net/filter?category=Gifts' -p category --tamper=randomcase,sleep2getlock,space2dash,charencode --technique=T

1. Replace SLEEP with GET_LOCK
2. Replace spaces ' ' with '--abcd%0A'
3. Random Character Case on SQL Keywords
4. URL Encode all Characters

SEE IMAGE BELOW TO SEE WHAT THIS TAMPER LOOKS LIKE IN BURPSUITE



<img width="1904" height="330" alt="tamper-script-timebased-sleep2lock-and-space2dash" src="https://github.com/user-attachments/assets/5d9b2930-7680-4268-8f2e-43f85250fb2a" />


<h1>TO BE CONTINUED</h1>
