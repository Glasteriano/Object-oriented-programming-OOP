# Object-oriented programming (OOP)

Continuing my progress in Python but now starting about OOP much more deeper than before.

In this repository I'll put everything I learn about it and always explained in this README and in the code.

##

### Class Method and Static Method

  - Obtaining some data in the class like age and IDs.
  
### Getter and Setter

  - Ways to modify a previous instance or data in order to avoid errors.
  - In the file the price was a string and not a int or float, so it was setted in a proper way to compute the discount.

### Class Attribute

  - Showing if a instance/attribute will be affected or not if I modify externally.

### Encapsulation

  - This file I just compared the ways to protect an inportant attibute or method in the class to anyone overwrite it.
  
### Association

  - Connecting two classes and using functions of each other as one.
  - Connecting the writer with two other classes and use their functions.

### Aggregation

  - A class access another one to run properly.
  - There are two main files, the first one is simple and only get the price and product name to calculate the sum. The second put it in a dictionary and update the product with the quantity to avoit repeated product in the trolley.
  
### Composition

  - When a object access another another class by reference and this allows it to use their methods.
  - In this files there are a Client that may have one or more address. The address is part of Client, so when CLient is deleted, adresses atached to them also are deleted.
  - The first file just puts it in a list with no separation.
  - The second file puts in a dictionary and the key is the State/County and the cities are inside a list as value.
  
### Inheritance

  - When a class has the same method in another class, allowing to use them. There are many ways to inherit a Superclass:
      - Basic Inheritance - When a subclass inherit only one Superclass.
      - Multi-level Inheritance - When a subclass inherits of another subclass that inherit of a Superclass.
      - Multiple Inheritance - When a subclass inherits more than one Superclass at the same time.
  - In the file I use Basic and Multi-level Inheritance as example.      
