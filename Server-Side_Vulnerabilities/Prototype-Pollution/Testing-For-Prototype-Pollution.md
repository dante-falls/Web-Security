<h1>Testing For Prototype Pollution - FOR EDUCATIONAL PURPOSES ONLY</h1>

Testing for Prototype pollution involves finding a pollution source and attempting to pollute Object.prototype on the client-side or the server side.

<h2>Client Side Testing</h2>

URL Payloads:

```https://test-fake-website-do-not-interact[.com]/?__proto__[testProperty69420]=testValue31337```

```https://test-fake-website-do-not-interact[.com]/?__proto__.testProperty69420=testValue31337```

```https://test-fake-website-do-not-interact[.com]/#__proto__[testProperty69420]=testValue31337```

```https://test-fake-website-do-not-interact[.com]/#__proto__.testProperty69420=testValue31337```

```https://test-fake-website-do-not-interact[.com]/?__proto__[testProperty69420]=testValue31337```

```https://test-fake-website-do-not-interact[.com]/?constructor[prototype][testProperty69420]=testValue31337```

<h2>Server Side Testing (DANGEROUS - BE SURE TO UTILIZE NON-DESTRUCTIVE METHODS)</h2>

Polluting Object.prototype on the server side can cause major issues for the server if not tested with non-destructive testing methods.

For example, notice in the following images we tried to pollute Object.prototype on the server side (in a Portswigger training lab) in order to make the server include more spaces then normal in the JSON Response Bodies
it returns. This can be reversed by setting the spaces to 0. Of course you'll want to get a base-line of how many spaces the server includes in between json entities before testing this. If the server usually includes
0 spaces, then any change indicates you successfully polluted Object.prototype on the server.

<img width="1420" height="633" alt="server-side-pp-poc-json-spaces-no-spaces" src="https://github.com/user-attachments/assets/d21cc1f1-ed5a-4e56-a9a0-be587ec02ff8" />

<img width="1416" height="633" alt="server-side-pp-poc-json-spaces-with-spaces" src="https://github.com/user-attachments/assets/674dd978-2066-4336-a1ae-1532c664ef27" />



