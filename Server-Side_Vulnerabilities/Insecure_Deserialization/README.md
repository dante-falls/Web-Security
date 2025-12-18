<h1>What is Insecure Deserialization?</h1>

Insecure deserialization is when user-controllable data is deserialized by a website. This potentially enables an attacker to manipulate serialized objects in order to pass harmful data into the application code.
Objects of any class that is available to the website will be deserialized and instantiated, regardless of which class was expected. For this reason, insecure deserialization is sometimes known as an "object injection"
vulnerability.

<h2>What Is Serialization?</h2>

Serialization is the process of converting complex data structures, such as objects and their fields, into a "flatter" format that can be sent and received as a sequential stream of bytes. 
Serializing data makes it much simpler to: 

<ul>
  <li>Write complex data to inter-process memory, a file, or a database.</li>
  <li>Send complex data, for example, over a network, between different components of an application, or in an API call.</li>
</ul>

<mark>When serializing an object, it's state persists, meaning the object's attributes and assigned values are preserved.</mark>

Serialization is also known as 'Pickling' in Python and 'Marshalling' in Ruby.

<h2>What Is Deserialization?</h2>

Deserialization is the process of restoring this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized. The website's logic can then interact with this deserialized
object, just like it would with any other object.
