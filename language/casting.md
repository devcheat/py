**Python Casting**
===
- [**Python Casting**](#python-casting)
  - [Specify a Variable Type](#specify-a-variable-type)
  - [Integers `int()`](#integers-int)
    - [**Example:**](#example)
  - [Floats `float()`](#floats-float)
    - [**Example:**](#example-1)
  - [Strings `str()`](#strings-str)
    - [**Example:**](#example-2)

---
## Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

## Integers `int()` 
constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

### **Example:**
```py
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```
## Floats `float()` 
constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

### **Example:**
```py
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

## Strings `str()` 
constructs a string from a wide variety of data types, including strings, integer literals and float literals

### **Example:**
```py
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```

---
