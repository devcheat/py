**Python String Formatting**
===

- [**Python String Formatting**](#python-string-formatting)
  - [String format()](#string-format)
    - [**Add a placeholder where you want to display the price:**](#add-a-placeholder-where-you-want-to-display-the-price)
    - [**Format the price to be displayed as a number with two decimals:**](#format-the-price-to-be-displayed-as-a-number-with-two-decimals)
  - [Multiple Values](#multiple-values)
  - [Index Numbers](#index-numbers)
  - [Named Indexes](#named-indexes)
  - [f-strings](#f-strings)

---
To make sure a string will display as expected, we can format the result with the format() method.

## String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

### **Add a placeholder where you want to display the price:**
```py
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
```
You can add parameters inside the curly brackets to specify how to convert the value:


### **Format the price to be displayed as a number with two decimals:**
```py
txt = "The price is {:.2f} dollars"
```
Check out all formatting types in our String format() Reference.

## Multiple Values
If you want to use more values, just add more values to the format() method:
```
print(txt.format(price, itemno, count))
```
And add more placeholders:

Example
```py
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```

## Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

Example
```py
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```

Also, if you want to refer to the same value more than once, use the index number:

Example
```py
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
```
## Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

Example
```py
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
```

## f-strings

PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler. 

To create an f-string, prefix the string with the letter `f`. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting. 

```py
# Python3 program introducing f-string
val = 'a'
print(f"{val}for{val} is a portal for {val}.")


name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
```

```
afora is a portal for a.
Hello, My name is Tushar and I'm 23 years old.
```

```py
# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
```
```
April 04, 2018
```
> **Note** : F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format(). 
  
