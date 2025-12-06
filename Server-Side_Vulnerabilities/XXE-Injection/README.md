<h1>XML external entity (XXE) Injection</h1>

XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application
server filesystem, and to interact with any back-end or external systems that the application itself can access.  In some situations, an attacker can escalate an XXE attack to compromise the underlying server or other back-end
infrastructure, by leveraging the XXE vulnerability to perform server-side request forgery (SSRF) attacks.

<img width="785" height="394" alt="XXE-Injection-intro-image" src="https://github.com/user-attachments/assets/7511b3b9-88cc-45c8-9102-179a84bc0965" />


<h2>What are External Entities?</h2>

XML external entities are a type of custom XML entity whose defined values are loaded from outside of the DTD in which they are declared. External entities are particularly interesting from a security perspective because they
allow an entity to be defined based on the contents of a file path or URL. 

Entities are placeholders in XML that can reference:

<ul>
  <li>Strings</li>
  <li>Internal Files</li>
  <li>External URLs</li>
</ul>

<h2>How Can This Become Insecure?</h2>

When a parser is misconfigured (or insecure by default), an attacker can supply XML that defines an external entity pointing to local files, remote resources, or even attempts to force the server to perform network operations.

<h2>How Do XXE Vulnerabilities Arise?</h2>

Some applications use the XML format to transmit data between the browser and the server. Applications that do this virtually always use a standard library or platform API to process the XML data on the server. XXE vulnerabilities
arise because the XML specification contains various potentially dangerous features, and standard parsers support these features even if they are not normally used by the application.

<h2>Type of XXE Attacks?</h2>

<ul>
  <li>Exploiting XXE to <b>retrieve files</b>, where an external entity is defined containing the contents of a file, and returned in the application's response.</li>
  <li>Exploiting XXE to <b>perform SSRF attacks</b>, where an external entity is defined based on a URL to a back-end system.</li>
  <li>Exploiting blind XXE <b>exfiltrate data out-of-band</b>, where sensitive data is transmitted from the application server to a system that the attacker controls.</li>
  <li>Exploiting blind XXE to <b>retrieve data via error messages</b>, where the attacker can trigger a parsing error message containing sensitive data.</li>
</ul>
