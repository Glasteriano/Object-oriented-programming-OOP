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
  - In a file I use both Basic and Multi-level Inheritance as example.
  - There are two other files using Multiple Inheritance, the first is simple and just report the actions of the smartphone to a text file that I call log. The second is a bit more complex because reports every action in another fille called log2 separating them between the device and the smartphone throught Tab space.

### super() Function

  - Super() function is related about Inheritance yet. When a subclass has the same method name of a Superclass, the subclass still no longer able to access that method in Superclass. If I still willing to access and use the Superclass method in the same function name of subclass I should use super() function.
  - In this file I still having access of Superclass method but the subclasses do more than only call a previous method.
  
### Abstract Class

  - It's a class that you cannot instantiate directly, only who inherits it. This type of class act like a blueprint for their heirs giving some methods that they might have to work properly.
  - In the file I used it in a "Bank Account" example. As every type of account has its own way of withdrawal, that method would be abstract and the heirs would set it in a proper way.
  
### Polymorphism

  - When two or more functions/methods have the same name but perform different things we call it polymorphism. In Python there is only one type of polymorphism, the overriding one, that means in different or even in the same class method/function when they have the same name we will only be able to call the last method. That can also happens in inheritance when subclasses override a method of a Superclass, not being able to call that Superclass method unless it uses the super() function.
  - In the file I created a abstract method that its heirs override for their own purpose just to notice the difference between them. It's not that complex, it is to observe the polymorphism in action.
  
### Custom Exceptions

  - We can create our own error message when there is no pre-built error in the language. It's a good way to print customised errors for developers/customers.
  - In the file if there is no parameter in the class, it will print the error on screen. The second example raises the error and print on screen too.

### Operator Overloading

  - We can change how an operator will act for certain types of instances. We cannot sum two classes to become only one class parameter as default, but in Python we can modify this just setting correctly how that operator will interpreter the data it will receive. Doing this we are able to sum, subtract, divide, etc a previous parameter/variable we were not able to do before, become easier to manipulate better our code and results.
  
### Magic Methods

  - These methods are those with double underline (__) in the beginning an in the end. They are used like Operator Overloading to modify a certain action of the code.
  - In the file I just describe some of them using examples.
  
### Context Manager

  - We use this when we want to open, connect and close that after doing what was needed, can be text file, databases and so on.
  - In the file I wrote three different ways to do it, two of them in a class and the last one just in a function.

### Metaclass

  - A type of class that creates another class, it is useful to check whether or not some class has an important object to work properly or make it mandatory to run code with no errors.
