# Generics

In Python, generics is a mechanism with which you to define functions, classes, or methods that can operate on multiple types while maintaining type safety. With the implementation of Generics enable it is possible to write reusable code that can be used with different data types. It ensures promoting code flexibility and type correctness.

Normally, in Python programming, you don't need to declare a variable type. The type is determined dynamically by the value assigned to it. Python's interpreter doesn't perform type checks and hence it may raise runtime exceptions.

Python introduced generics with type hints in version 3.5, allowing you to specify the expected types of variables, function arguments, and return values. This feature helps in reducing runtime errors and improving code readability.

Generics extend the concept of type hints by introducing type variables, which represent generic types that can be replaced with specific types when using the generic function or class.

## Defining a Generic Function
Let us have a look at the following example that defines a generic function −

```py
from typing import List, TypeVar, Generic
T = TypeVar('T')
def reverse(items: List[T]) -> List[T]:
   return items[::-1]
```

Here, we define a generic function called 'reverse'. The function takes a list ('List[T]') as an argument and returns a list of the same type. The type variable 'T' represents the generic type, which will be replaced with a specific type when the function is used.

## Calling the Generic Function with Different Data Types
The function reverse() function is called with different data types −
```py
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse(numbers)
print(reversed_numbers)

fruits = ['apple', 'banana', 'cherry']
reversed_fruits = reverse(fruits)
print(reversed_fruits)
```
It will produce the following output −
```
[5, 4, 3, 2, 1]
['cherry', 'banana', 'apple']
```

## Defining a Generic Class
A generic type is typically declared by adding a list of type parameters after the class name. The following example uses generics with a generic class −
```py
from typing import List, TypeVar, Generic
T = TypeVar('T')
class Box(Generic[T]):
   def __init__(self, item: T):
      self.item = item
   def get_item(self) -> T:
      return self.item
Let us create objects of the above generic class with int and str type
box1 = Box(42)
print(box1.get_item())

box2 = Box('Hello')
print(box2.get_item())
```
It will produce the following output −
```
42
Hello
```

---