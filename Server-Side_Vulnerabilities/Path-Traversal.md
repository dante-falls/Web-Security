<h1>Path Traversal</h1>

<p align="center">
<br/>
<img src="https://i.imgur.com/23gjYcI.png" height="300%" width="300%" alt="Prompt Injection"/>
<br />
<br />
</p>

<h2>Definition</h2>

A **path traversal attack (also known as directory traversal)** aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files. It should be noted that access to files is limited by system operational access control (such as in the case of locked or in-use files on the Microsoft Windows operating system).

This attack is also known as “dot-dot-slash”, “directory traversal”, “directory climbing” and “backtracking”. 
