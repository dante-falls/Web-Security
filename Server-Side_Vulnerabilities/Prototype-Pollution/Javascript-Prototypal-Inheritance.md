<h1>What is Prototypal Inheritance</h1>

JavaScript uses a prototypal inheritance model, which is quite different from the class-based model used by many other languages. Objects inherit properties and methods from other objects, known as prototypes.

<h2>What is an object in JavaScript?</h2>

Virtually everything in JavaScript is an object under the hood. An object is a collection of key-value pairs (or methods if the values are functions). The following object could represent a user:

```
const user =  {
    username: "wiener",
    userId: 01234,
    exampleMethod: function(){
        // do something
    }
}
```

The example above is an "object literal", which means it was created using curly brace syntax to explicitly declare its properties and their initial values.

You can access the properties of an object by using either dot notation or bracket notation to refer to their respective keys:

```user.username     // "wiener"```

```user['userId']    // 01234```

<h2>What is a prototype in JavaScript?</h2>

Every object in JavaScript is linked to another object of some kind, known as its prototype. By default, JavaScript automatically assigns new objects one of its built-in prototypes.

For example, strings are automatically assigned the built-in **String.prototype**

Here are some other global prototypes:

```
let myObject = {};
Object.getPrototypeOf(myObject);    // **Object.prototype**
```

```
let myString = "";
Object.getPrototypeOf(myString);    // **String.prototype**
```

```
let myArray = [];
Object.getPrototypeOf(myArray);	    // **Array.prototype**
```

```
let myNumber = 1;
Object.getPrototypeOf(myNumber);    // **Number.prototype**
```

Objects automatically inherit all of the properties of their assigned prototype, unless they already have their own property with the same key. This enables developers to create new objects that 
can reuse the properties and methods of existing objects.

The built-in prototypes provide useful properties and methods for working with basic data types. For example, the **String.prototype** object has a **toLowerCase()** method. As a result, all strings automatically have a ready-to-use 
method for converting them to lowercase. This saves developers having to manually add this behavior to each new string that they create.

<h2>How Does Object Inheritance Work In JavaScript?</h2>

Whenever you reference a property of an object, the JavaScript engine first tries to access this directly on the object itself. If the object doesn't have a matching property, the JavaScript engine looks for it on the object's prototype 
instead.

<img width="1200" height="896" alt="javascript-object-inheritance" src="https://github.com/user-attachments/assets/3c2b9931-4238-4665-8885-668cb9124887" />

You can see this in the console by creating a completely empty object. When you later reference the object, the console automatically prompts you to select from a list of properties and methods. Even though your object has no properties
or methods, it still inherits some from the built-in **Object.prototype**

<img width="913" height="456" alt="myEmptyObject-image-1" src="https://github.com/user-attachments/assets/987e7a8e-881d-4da8-9096-029c369efdbd" />

<h2>The Prototype Chain</h2>

Note that an object's prototype is just another object, which should also have its own prototype, and so on. As virtually everything in JavaScript is an object under the hood, this chain ultimately leads back to the 
top-level Object.prototype, whose prototype is simply null.

<img width="960" height="499" alt="javascript-prototype-chain" src="https://github.com/user-attachments/assets/23fbf637-1a2f-4705-bd83-8d5d008679be" />

Crucially, objects inherit properties not just from their immediate prototype, but from all objects above them in the prototype chain. In the example above, this means that the **username object** has access to the properties 
and methods of both **String.prototype** and **Object.prototype**.

<h2>Accessing an object's prototype using __proto__</h2>

Every object has a special property that you can use to access its prototype: **__proto__**

This property serves as both a getter and setter for the object's prototype. This means you can use it to read and modify the prototype and its properties.

As with any property, you can access **__proto__** using either bracket or dot notation:

```username.__proto__```

```username['__proto__']```

You can even chain references to **__proto__** to work your way up the prototype chain:

```username.__proto__                        // String.prototype```

```username.__proto__.__proto__              // Object.prototype```

```username.__proto__.__proto__.__proto__    // null```

<h2>Modifying Prototypes</h2>

It is possible to modify JavaScript's built-in prototypes just like any other object. This means developers can customize or override the behavior of built-in methods, and even add new methods to perform useful operations.

For example, modern JavaScript provides the trim() method for strings, which enables you to easily remove any leading or trailing whitespace. Before this built-in method was introduced, developers sometimes added their own custom 
implementation of this behavior to the String.prototype object by doing something like this:

```
String.prototype.removeWhitespace = function(){
    // remove leading and trailing whitespace
}
```

Thanks to the prototypal inheritance, all strings would then have access to this method:

```
let searchTerm = "  example ";
searchTerm.removeWhitespace();    // "example"
```


