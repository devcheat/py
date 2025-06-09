

__Object-oriented Programming__
====

**Summary**: in this tutorial, you'll learn object-oriented programming in Python, including essential concepts such as objects, classes, attributes, methods, inheritances, overriding methods, etc.


Everything in Python is an object. An object has a state and behaviors. To create an object, you define a class first. And then, from the class, you can create one or more objects. The objects are instances of a class.

# Define a class

To define a [class](https://www.pythontutorial.net/python-oop/python-class/), you use the `class` keyword followed by the class name. For example, the following defines a `Person` class:

```py
class Person:
    pass`Code language: Python (python)
```

To create an object from the `Person` class, you use the class name followed by parentheses `()`, like calling a function:

```py
person = Person()
```

In this example, the `person` is an instance of the `Person` class. Classes are callable.

# Define instance attributes

Python is dynamic. It means that you can add an attribute to an instance of a class dynamically at runtime.

For example, the following adds the `name` attribute to the `person` object:

```py
person.name = 'John'
```

However, if you create another `Person` object, the new object won't have the `name` attribute.

To define and initialize an attribute for all instances of a class, you use the `__init__` method. The following defines the `Person` class with two instance attributes `name` and `age`:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age`Code language: Python (python)
```

When you create a `Person` object, Python automatically calls the `__init__` method to initialize the instance attributes. In the `__init__` method, the `self` is the instance of the `Person` class.

The following creates a `Person` object named `person`:

```py
person = Person('John', 25)
```

The `person` object now has the `name` and `age` attributes. To access an instance attribute, you use the dot notation. For example, the following returns the value of the name attribute of the `person` object:

```py
person.name
```

# Define instance methods

The following adds an instance method called `greet()` to the `Person` class:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."
```

To call an instance method, you also use the dot notation. For example:

```py
person = Person('John', 25)
print(person.greet())
```

Output:
```
Hi, it's John
```

# Define class attributes

Unlike instance attributes, class attributes are shared by all instances of the class. They are helpful if you want to define class constants or variables that keep track of the number of instances of a class.

- A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the `__init__()` method.
- Use `class_name.class_attribute` or `object_name.class_attribute` to access the value of the `class_attribute`.
- Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.

For example, the following defines the `counter` class attribute in the `Person` class:

```py
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."
```

You can access the `counter` attribute from the `Person` class:

```py
Person.counter
```

Or from any instances of the `Person` class:

```py
person = Person('John',25)
person.counter
```


To make the `counter` variable more useful, you can increase its value by one once an object is created. To do it, you increase the `counter` class attribute in the `__init__` method:

```py
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."
```

The following creates two instances of the `Person` class and shows the value of the `counter`:

```py
p1 = Person('John', 25)
p2 = Person('Jane', 22)
print(Person.counter)
```

Output:
```
2
```

## When to use class attributes 
Class attributes are useful in some cases such as storing class constants, tracking data across all instances, and defining default values.

### 1 Storing class constants 
Since a constant doesn’t change from instance to instance of a class, it’s handy to store it as a class attribute.

For example, the Circle class has the pi constant that is the same for all instances of the class. Therefore, it’s a good candidate for the class attributes.

### 2) Tracking data across of all instances 
The following adds the circle_list class attribute to the Circle class. When you create a new instance of the Circle class, the constructor adds the instance to the list:
```py
class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2
```

### 3) Defining default values 
Sometimes, you want to set a default value for all instances of a class. In this case, you can use a class attribute.

The following example defines a Product class. All the instances of the Product class will have a default discount specified by the default_discount class attribute:
```py
class Product:
    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


p1 = Product(100)
print(p1.net_price())
 # 100

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())
 # 190
 ```

# Define class method

> By definition, a method is a function that is bound to an instance of a class. This tutorial helps you understand how it works under the hood.

Like a class attribute, a class method is shared by all instances of the class. The first argument of a class method is the class itself. By convention, its name is `cls`. 
Python automatically passes this argument to the class method. Also, you use the `@classmethod` decorator to decorate a class method.

The following example defines a class method that returns an anonymous `Person` object:

```py
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

 @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)
```

The following shows how to call the `create_anonymous()` class method:

```py
anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous
```

# Define static method

A static method is not bound to a class or any instances of the class. In Python, you use static methods to group logically related functions in a class. To define a static method, you use the `@staticmethod` decorator.

- Use static methods to define utility methods or group a logically related functions into a class.
- Use the `@staticmethod` decorator to define a static method.

For example, the following defines a class `TemperatureConverter` that has two static methods that convert from celsius to Fahrenheit and vice versa:

```py
class TemperatureConverter:
 @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

 @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9
```

To call a static method, you use the `ClassName.static_method_name()` syntax. For example:

```py
f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)  # 86
```

Notice that Python doesn't implicitly pass an instance (`self`) as well as class (`cls`) as the first argument of a static method.

## Python static methods vs class methods

Since static methods are quite similar to the class methods, you can use the following to find the differences between them:

| **Class Methods** | **Static Methods** |
| --- | --- |
| Python implicitly pass the `cls` argument to class methods. | Python doesn't implicitly pass the `cls` argument to static methods |
| Class methods **can **access and modify the class state. | Static methods **cannot **access or modify the class state. |
| Use `@classmethod` decorators to define class methods | Use `@staticmethod` decorators to define static methods. |


# Property

The following defines a Person class that has two attributes name and age, and create a new instance of the Person class:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person('John', 18)
```
Since age is the instance attribute of the Person class, you can assign it a new value like this:
```
john.age = 19
```

## Getter and setter 
The getter and setter methods provide an interface for accessing an instance attribute:

- The getter returns the value of an attribute
- The setter sets a new value for an attribute

In our example, you can make the age attribute private (by convention) and define a getter and a setter to manipulate the age attribute.

The following shows the new Person class with a getter and setter for the age attribute:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age
```

## @property decorator

So to get the age of a Person object, you can use either the age property or the `get_age()` method. This creates an unnecessary redundancy.

To avoid this redundancy, you can rename the `get_age()` method to the `age()` method like this:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def age(self):
        return self._age

    age = property(fget=age)
```
The `property()` accepts a callable (age) and returns a callable. Therefore, it is a decorator. Therefore, you can use the `@property `decorator to decorate the `age()` method as follows:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age
```
So by using the @property decorator, you can simplify the property definition for a class.

## Setter decorators 

The `setter()` method accepts a callable and returns another callable (a property object). Therefore, you can use the decorator `@age.setter` for the `set_age()` method like this:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
```

Now, you can change the `set_age()` method to the `age()` method and use the age property in the `__init__()` method:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
```
To summarize, you can use decorators to create a property using the following pattern:
```py
class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value
```

## Readonly Property
- Define only the getter to make a property readonly
- Do use computed property to make the property of a class more natural
- Use caching computed properties to improve the performance.

To define a readonly property, you need to create a property with only the getter. However, it is not truly read-only because you can always access the underlying attribute and change it.

The read-only properties are useful in some cases such as for computed properties.
```py
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(10)
print(c.area)
```



# Single inheritance

A class can reuse another class by inheriting it. When a child class inherits from a parent class, the child class can access the attributes and methods of the parent class.

For example, you can define an `Employee` class that inherits from the `Person` class:

```py
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
```

Inside the `__init__` method of the `Employee` class calls the `__init__`method of the `Person` class to initialize the `name` and `age` attributes. The `super()` allows a child class to access a method of the parent class.

The `Employee` class extends the `Person` class by adding one more attribute called `job_title`.

The `Person` is the parent class while the `Employee` is a child class. To override the `greet()` method in the `Person` class, you can define the `greet()` method in the `Employee` class as follows:

```py 
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."
```

The `greet()` method in the `Employee` is also called the `greet()` method of the `Person` class. In other words, it delegates to a method of the parent class.

The following creates a new instance of the `Employee` class and call the `greet()` method:

```py
employee = Employee('John', 25, 'Python Developer')
print(employee.greet())
```

Output:
```
`Hi, it's John. I'm a Python Developer.
```



# Class Variables
Everything in Python is an object including a class. In other words, a class is an object in Python.

- A class is an object which is an instance of the type class.
- Class variables are attributes of the class object.
- Use dot notation or getattr() function to get the value of a class attribute.
- Use dot notation or setattr() function to set the value of a class attribute.
- Python is a dynamic language. Therefore, you can assign a class variable to a class at runtime.
- Python stores class variables in the __dict__ attribute. The __dict__ attribute is a dictionary.

When you define a class using the class keyword, Python creates an object with the name the same as the class’s name. For example:

```py
class HtmlDocument:
   pass
```

This example defines the HtmlDocument class and the HtmlDocument object. The HtmlDocument object has the __name__ property:
```py
class HtmlDocument:
   pass

print(HtmlDocument.__name__)
```
Output:
```
HtmlDocument
```
And the HTMLDocument has the type of type:
```py
class HtmlDocument:
   pass

print(type(HtmlDocument))
```

Output:
```
<class 'type'>
```

It’s also an instance of the type class:
```py
class HtmlDocument:
   pass

print(isinstance(HtmlDocument, type))
```

Output:
```
True
```

Class variables are bound to the class. They’re shared by all instances of that class.

The following example adds the `extension` and `version` class variables to the HtmlDocument class:

```py
class HtmlDocument:
    extension = 'html'
    version = '5'
```

Both `extension` and `version` are the class variables of the HtmlDocument class. They’re bound to the HtmlDocument class.

## Get the values of class variables 
To get the values of class variables, you use the dot notation (.). For example:

```py
class HtmlDocument:
    extension = 'html'
    version = '5'

print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5
```

Output:
```
html
5
```

If you access a class variable that doesn’t exist, you’ll get an AttributeError exception. For example:
```py
class HtmlDocument:
    extension = 'html'
    version = '5'

print(HtmlDocument.media_type)
```

Error:
```
AttributeError: type object 'HtmlDocument' has no attribute 'media_type'
```

Another way to get the value of a class variable is to use the `getattr()` function. The `getattr()` function accepts an object and a variable name. It returns the value of the class variable. For example:

```py
class HtmlDocument:
    extension = 'html'
    version = '5'

extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')

print(extension)  # html
print(version)  # 5
```

Output:
```
html
5
```

If the class variable doesn’t exist, you’ll also get an AttributeError exception. To avoid the exception, you can specify a default value if the class variable doesn’t exist like this:

```py
class HtmlDocument:
    extension = 'html'
    version = '5'

media_type = getattr(HtmlDocument, 'media_type', 'text/html')
print(media_type) # text/html
```

Output:
```
text/html
```

## Set values for class variables 
To set a value for a class variable, you use the dot notation:

```py
HtmlDocument.version = 10
```
or you can use the `setattr()` built-in function:
```py
setattr(HtmlDocument, 'version', 10)
```

Since Python is a dynamic language, you can add a class variable to a class at runtime after you have created it. For example, the following adds the media_type class variable to the HtmlDocument class:
```py
HtmlDocument.media_type = 'text/html'
print(HtmlDocument.media_type)
```

Similarly, you can use the `setattr()` function:
```py
setattr(HtmlDocument, media_type, 'text/html')
print(HtmlDocument.media_type)
```

## Delete class variables 
To delete a class variable at runtime, you use the delattr() function:
```py
delattr(HtmlDocument, 'version')
```
Or you can use the del keyword:
```py
del HtmlDocument.version
```

## Class variable storage 
Python stores class variables in the __dict__ attribute. The __dict__ is a mapping proxy, which is a dictionary. For example:

```py
from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'


HtmlDocument.media_type = 'text/html'

pprint(HtmlDocument.__dict__)
```

Output:
```
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'media_type': 'text/html',
              'version': '5'})
```

The output indciates that the `__dict__` has three class variables: extension, media_type, and version besides other predefined class variables.

Python does not allow you to change the `__dict__ `directly. For example, the following will result in an error:
```py
HtmlDocument.`__dict__`['released'] = 2008
```
Output:
```
TypeError: 'mappingproxy' object does not support item assignment
```
However, you can use the setattr() function or dot notation to indirectly change the `__dict__` attribute.

Also, the key of the `__dict__` are strings that will help Python speeds up the variable lookup.

Although Python allows you to access class variables through the `__dict__` dictionary, it’s not a good practice. Also, it won’t work in some situations. For example:

```py
print(HtmlDocument.__dict__['type']) # BAD CODE
```

## Callable class attributes 
Class attributes can be any object such as a function.

When you add a function to a class, the function becomes a class attribute. Since a function is callable, the class attribute is called a callable class attribute. For example:

```py
from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'

    def render():
        print('Rendering the Html doc...')


pprint(HtmlDocument.__dict__)
```

Output:
```
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'render': <function HtmlDocument.render at 0x0000010710030310>,
              'version': '5'})
Rendering the Html doc...
```

In this example, the render is a class attribute of the HtmlDocument class. Its value is a function.

# Constructor

When you create a new object of a class, Python automatically calls the `__init__()` method to initialize the object’s attributes.

- Use the `__init__()` method to initialize the object’s attributes.
- The `__init__()` doesn’t create an object but is automatically called after the object is created.

Unlike regular methods, the `__init__()` method has two underscores `__` on each side. Therefore, the `__init__()` is often called dunder init. The name comes abbreviation of the double underscores init.

The double underscores at both sides of the `__init__()` method indicate that Python will use the method internally. In other words, you should not explicitly call this method.

Since Python will automatically call the `__init__()` method immediately after creating a new object, you can use the `__init__()` method to initialize the object’s attributes.

The following defines the Person class with the `__init__()` method:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('John', 25)
print(f"I'm {person.name}. I'm {person.age} years old.")
```

Output:
```
I'm John. I'm 25 years old.
```

When you create an instance of the Person class, Python performs two things:

First, create a new instance of the Person class by setting the object’s namespace such as `__dict__` attribute to empty `{}`.
Second, call the `__init__` method to initialize the attributes of the newly created object.
Note that the `__init__` method doesn’t create the object but only initializes the object’s attributes. Hence, the `__init__()` is not a constructor.

If the `__init__` has parameters other than the self, you need to pass the corresponding arguments when creating a new object like the example above. Otherwise, you’ll get an error.

## The `__init__` method with default parameters 
The `__init__()` method’s parameters can have default values. For example:
```py
class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


person = Person('John')
print(f"I'm {person.name}. I'm {person.age} years old.")
```

Output:
```
I'm John. I'm 22 years old.
```

In this example, the age parameter has a default value of 22. Because we don’t pass an argument to the `Person()`, the age uses the default value.

# Encapsulation

Encapsulation is one of the four fundamental concepts in object-oriented programming including abstraction, encapsulation, inheritance, and polymorphism.

> Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.

A class is an example of encapsulation. A class bundles data and methods into a single unit. And a class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a valid state.

## Python encapsulation example 
The following defines the Counter class:
```PY
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0
```


# Private attributes 
Private attributes can be only accessible from the methods of the class. In other words, they cannot be accessible from outside of the class.

> Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.

By convention, you can define a private attribute by prefixing a single underscore (_):
```
_attribute
```
This means that the _attribute should not be manipulated and may have a breaking change in the future.

The following redefines the Counter class with the current as a private attribute by convention:

```PY
class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0
```

## Name mangling with double underscores 
If you prefix an attribute name with double underscores (__) like this:

```PY
__attribute
```

Python will automatically change the name of the __attribute to:

```py
_class__attribute
```

This is called the __name mangling__ in Python.

By doing this, you cannot access the __attribute directly from the outside of a class like:
```py
instance.__attribute
```
However, you still can access it using the _class__attribute name:
```py
instance._class__attribute
```
The following example redefines the Counter class with the __current attribute:
```py
class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0
```
Now, if you attempt to access __current attribute, you’ll get an error:
```PY
counter = Counter()
print(counter.__current)
```
Output:
```
AttributeError: 'Counter' object has no attribute '__current'
```
However, you can access the __current attribute as _Counter___current like this:
```PY
counter = Counter()
print(counter._Counter__current)
```

# Special methods

## `__str__` method

- Implement the `__str__` method to customize the string representation of an instance of a class.


To customize the string representation of a class instance, the class needs to implement the `__str__` magic method.

Internally, Python will call the `__str__` method automatically when an instance calls the str() method.

Note that the print() function converts all non-keyword arguments to strings by passing them to the str() before displaying the string values.

The following illustrates how to implement the `__str__` method in the Person class:

```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
```

And when you use the `print()` function to print out an instance of the Person class, Python calls the `__str__` method defined in the Person class. For example:

```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'

person = Person('John', 'Doe', 25)
print(person)
```
Output:
```
Person(John,Doe,25)
```


## `__repr__ `magic method

The `__repr__` dunder method defines behavior when you pass an instance of a class to the `repr()`.

- Implement the `__repr__` method to customize the string representation of an object when repr() is called on it.
- The `__str__` calls `__repr__` internally by default.
- Python falls back to `__repr__` if `__str__` is not defined.

The `__repr__` method returns the string representation of an object. Typically, the `__repr__()` returns a string that can be executed and yield the same value as the object.

In other words, if you pass the returned string of the `object_name.__repr__()` method to the `eval()` function, you'll get the same value as the `object_name`. Let's take a look at an example.

First, define the `Person` class with three instance attributes `first_name`, `last_name`, and `age`:

```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
```

Second, create a new instance of the `Person` class and display its string representation:

```py
person = Person('John', 'Doe', 25)
print(repr(person))
```

Output:

```
<__main__.Person object at 0x000001F51B3313A0>
```

By default, the output contains the memory address of the `person` object. To customize the string representation of the object, you can implement the `__repr__` method like this:

```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'
```

When you pass an instance of the `Person` class to the `repr()`, Python will call the `__repr__` method automatically. For example:
```py
person = Person("John", "Doe", 25)
print(repr(person))
```

Output:

```
Person("John","Doe",25)
```

If you execute the return string `Person("John","Doe",25)`, it'll return the `person` object.

When a class doesn't implement the `__str__` method and you pass an instance of that class to the `str()`, Python returns the result of the `__repr__` method because internally the `__str__` method calls the `__repr__` method:

For example:

```py
person = Person('John', 'Doe', 25)
print(person)
```
Output:

```
Person("John","Doe",25)
```

If a class implements the `__str__` method, Python will call the `__str__` method when you pass an instance of the class to the `str()`. For example:

```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'

person = Person('John', 'Doe', 25)
# use str()
print(person)

# use repr()
print(repr(person))` Code language: Python (python)
```


Output:
```
`(John,Doe,25)
Person("John","Doe",25)
```

### `__str__` vs `__repr__` 

The main difference between `__str__` and `__repr__` method is intended audiences.

The `__str__` method returns a string representation of an object that is human-readable while the `__repr__` method returns a string representation of an object that is machine-readable.

## `__eq__` method

Python automatically calls the `__eq__` method of a class when you use the == operator to compare the instances of the class. By default, Python uses the is operator if you don’t provide a specific implementation for the `__eq__` method.

> Implement the Python `__eq__ `method to define the equality logic for comparing two objects using the equal operator `==`.

The following shows how to implement the `__eq__` method in the Person class that returns True if two person objects have the same age:
```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age
```
Now, if you compare two instances of the Person class with the same age, it returns True:
```
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age
    
john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
print(john == jane)  # True    
```
Output:
```
True
```
And if two instances of the Person class don’t have the same age, the `==` operator returns False:

The following compares a Person object with an integer:

```py
john = Person('John', 'Doe', 25)
print(john == 20)
```

It returns an error:
```
AttributeError: 'int' object has no attribute 'age'
```

To fix this, you can modify the `__eq__` method to check if the object is an instance of the Person class before accessing the age attribute.

If the other object isn’t an instance of the Person class, the `__eq__` method returns False, like this:
```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False
```
And you can now compare an instance of the Person class with an integer or any object of a different type:
```py
john = Person('John', 'Doe', 25)
print(john == 20)  # False
```
