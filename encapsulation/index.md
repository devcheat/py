# Encapsulation in Python

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP), including abstraction, inheritance, and polymorphism. This lesson will cover what encapsulation is and how to implement it in Python.


## What is Encapsulation in Python?

Encapsulation in Python describes the concept of bundling data and methods within a single unit. So, for example, when you create a class, it means you are implementing encapsulation. A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

```py
class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()
```

Using encapsulation, we can hide an object’s internal representation from the outside. This is called information hiding.

Also, encapsulation allows us to restrict accessing variables and methods directly and prevent accidental data modification by creating private data members and methods within a class.

Encapsulation is a way to can restrict access to methods and variables from outside of class. Whenever we are working with the class and dealing with sensitive data, providing access to all variables used within the class is not a good choice.

For example, Suppose you have an attribute that is not visible from the outside of an object and bundle it with methods that provide read or write access. In that case, you can hide specific information and control access to the object’s internal state. Encapsulation offers a way for us to access the required variable without providing the program full-fledged access to all variables of a class. This mechanism is used to protect the data of an object from other objects.

## Access Modifiers in Python

Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using single underscore and double underscores.

Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, public, and protected.
- Public Member: Accessible anywhere from otside oclass.
- Private Member: Accessible within the class
- Protected Member: Accessible within the class and its sub-classes

```py
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

class Employee(Company):
    def __init__(self,name,salary):
        self.name = name # Public member (accessible within or outside of a class)
        Company.__init__(self) # Protected member (accessile within this class and it's sub-classes)
        self.__salary = salary # Private member (accessible only within a class)

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

    def projectInfo(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)



emp = Employee("adam",10000)

# accessing public data members : 
print("Public data members are accessible within and outside of a class. All member variables of the class are by default public.")
print("Name: ", emp.name)

# accessing private data members
print("Private members are accessible only within the class, and we can’t access them directly from the class objects.")
print('Salary',emp.__salary)

# Public method to access private members
print("Access Private member outside of a class using an instance method")
emp.show()

# Name Mangling to access private members
print("The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, like this _classname__dataMember, where classname is the current class, and data member is the private variable name.")

# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)

# Direct access protected data member
print('Project:', emp._project)

```


## Getters and Setters in Python
To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members and the setter methods to modify the data members.

In Python, private variables are not hidden fields like in other programming languages. The getters and setters methods are often used when:

- When we want to avoid direct access to private variables
- To add validation logic for setting a value

```py
class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())
```

Information Hiding and conditional logic for setting an object attributes

```py
class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    def get_roll_no(self):
        return self.__roll_no

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)


jessa.set_roll_no(25)
jessa.show()
```

## Advantages of Encapsulation
- Security: The main advantage of using encapsulation is the security of the data. Encapsulation protects an object from unauthorized access. It allows private and protected access levels to prevent accidental data modification.

- Data Hiding: The user would not be knowing what is going on behind the scene. They would only be knowing that to modify a data member, call the setter method. To read a data member, call the getter method. What these setter and getter methods are doing is hidden from them.

- Simplicity: It simplifies the maintenance of the application by keeping classes separated and preventing them from tightly coupling with each other.

- Aesthetics: Bundling data and methods within a class makes code more readable and maintainable


https://pynative.com/python-encapsulation/
https://pythonbasics.org/
