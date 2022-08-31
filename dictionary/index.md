**Python Dictionary**
===
- [**Python Dictionary**](#python-dictionary)
  - [Creating a Dictionary](#creating-a-dictionary)
  - [Nested Dictionary](#nested-dictionary)
  - [Adding elements to a Dictionary](#adding-elements-to-a-dictionary)
    - [Adding Items](#adding-items)
    - [Update Dictionary](#update-dictionary)
  - [Removing Items](#removing-items)
  - [Loop Through a Dictionary](#loop-through-a-dictionary)
  - [Copy a Dictionary](#copy-a-dictionary)
  - [Accessing elements of a Dictionary](#accessing-elements-of-a-dictionary)
  - [Accessing Items](#accessing-items)
    - [Get Keys](#get-keys)
    - [Get Values](#get-values)
    - [Get Items](#get-items)
    - [Check if Key Exists](#check-if-key-exists)
  - [Accessing an element of a nested dictionary](#accessing-an-element-of-a-nested-dictionary)
  - [Change Values](#change-values)
  - [Update Dictionary](#update-dictionary-1)
  - [Dictionary methods](#dictionary-methods)

---

Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

**Example of Dictionary in Python** 
Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized. 
```py
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
```
Output:
```
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
```

## Creating a Dictionary
In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

> **Note – Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.** 

```py
# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
```
Output:
```
Dictionary with the use of Integer Keys: 
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Dictionary with the use of Mixed Keys: 
{'Name': 'Geeks', 1: [1, 2, 3, 4]}
```

Dictionary can also be created by the built-in function `dict()`. An empty dictionary can be created by just placing to curly braces{}. 

```py
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Creating a Dictionary with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
  
# Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
```
Output:
```
Empty Dictionary: 
{}
Dictionary with the use of dict(): 
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Dictionary with each item as a pair: 
{1: 'Geeks', 2: 'For'}
```

**Complexities for Creating a Dictionary:**
```
Time complexity: O(len(dict))
Space complexity: O(n)
```




## Nested Dictionary

```py
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
  
print(Dict)
```
Output:
```
{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

```
## Adding elements to a Dictionary
Addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. `Dict[Key] = ‘Value’`. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary. 

> **Note- While adding a value, if the key-value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.**

```py
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
  
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
```

Output:
```
Empty Dictionary: 
{}
Dictionary after adding 3 elements: 
{0: 'Geeks', 2: 'For', 3: 1}
Dictionary after adding 3 elements: 
{0: 'Geeks', 2: 'For', 3: 1, 'Value_set': (2, 3, 4)}
Updated key value: 
{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}
Adding a Nested Key: 
{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4), 5: 
{'Nested': {'1': 'Life', '2': 'Geeks'}}}
```
**Complexities for Adding elements in a Dictionary:**
```
Time complexity: O(1)/O(n)
Space complexity: O(1)
```


### Adding Items
**Adding an item to the dictionary is done by using a new index key and assigning a value to it:**

Example
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```

### Update Dictionary
The `update()` method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example
**Add a color item to the dictionary by using the update() method:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

```

## Removing Items
There are several methods to remove items from a dictionary:

Example
**The `pop()` method removes the item with the specified key name:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```
Example
**The `popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead):**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```

Example
**The `del` keyword removes the item with the specified key name:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```

Example
**The `del` keyword can also delete the dictionary completely:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
```
Example
**The `clear()` method empties the dictionary:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```

## Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example
**Print all key names in the dictionary, one by one:**
```py
for x in thisdict:
  print(x)
```
Example
**Print all values in the dictionary, one by one:**
```py
for x in thisdict:
  print(thisdict[x])
```
Example
**You can also use the values() method to return values of a** dictionary:
```py
for x in thisdict.values():
  print(x)
```
Example
**You can use the keys() method to return the keys of a dictionary:**
```py
for x in thisdict.keys():
  print(x)
```
Example
**Loop through both keys and values, by using the items() method:**
```py
for x, y in thisdict.items():
  print(x, y)
```

## Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Example
**Make a copy of a dictionary with the copy() method:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```

Another way to make a copy is to use the built-in function dict().

Example
**Make a copy of a dictionary with the dict() function:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```




## Accessing elements of a Dictionary
In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. 

```py
# Python program to demonstrate
# accessing a element from a Dictionary
  
# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
  
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])
```
**Output:**
```
Accessing a element using key:
For
Accessing a element using key:
Geeks
```
There is also a method called `get()` that will also help in accessing the element from a dictionary.This method accepts key as argument and returns the value.

**Complexities for Accessing elements in a Dictionary:**
```
Time complexity: O(1)
Space complexity: O(1)
```

```py
# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))
```
Output:
```
Accessing a element using get:
Geeks
```


## Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
```
There is also a method called `get()` that will give you the same result:

**Get the value of the "model" key:**
```py
x = thisdict.get("model")
```

### Get Keys
The keys() method will return a list of all the keys in the dictionary.

**Get a list of the keys:**
```py
x = thisdict.keys()
```

The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

**Add a new item to the original dictionary, and see that the keys list gets updated as well:**
```py
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
```

### Get Values
The values() method will return a list of all the values in the dictionary.

**Get a list of the values:**
```py
x = thisdict.values()
```
The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

Example
Make a change in the original dictionary, and see that the values list gets updated as well:
```py
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```

Example
**Add a new item to the original dictionary, and see that the values list gets updated as well:**
```py
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```
### Get Items
The items() method will return each item in a dictionary, as tuples in a list.

Example
Get a list of the key:value pairs
```py
x = thisdict.items()
```
The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

**Make a change in the original dictionary, and see that the items list gets updated as well:**

```py
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```

Example
Add a new item to the original dictionary, and see that the items list gets updated as well:

```py
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```

### Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

**Check if "model" is present in the dictionary:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```  



## Accessing an element of a nested dictionary
In order to access the value of any key in the nested dictionary, use indexing [] syntax.

```py
# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
  
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
```

Output:
```
{1: 'Geeks'}
Geeks
For
```

## Change Values
You can change the value of a specific item by referring to its key name:

Example
Change the "year" to 2018:
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```

## Update Dictionary
The `update()` method will update the dictionary with the items from the given argument.

> The argument must be a dictionary, or an iterable object with key:value pairs.

Example
**Update the "year" of the car by using the update() method:**
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```




## Dictionary methods
Method|description
--|--
`clear()` |Remove all the elements from the dictionary
`copy()` |Returns a copy of the dictionary
`get()` |Returns the value of specified key
`items()` |Returns a list containing a tuple for each key value pair
`keys()` |Returns a list containing dictionary’s keys
`pop()` |Remove the element with specified key
`popitem()` |Removes the last inserted key-value pair
`update()` |Updates dictionary with specified key-value pairs
`values()` |Returns a list of all the values of dictionary
`fromkeys()`	|Returns a dictionary with the specified keys and value
`setdefault()`	|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

```py
# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  
# copy() method
dict2 = dict1.copy()
print(dict2)
  
# clear() method
dict1.clear()
print(dict1)
  
# get() method
print(dict2.get(1))
  
# items() method
print(dict2.items())
  
# keys() method
print(dict2.keys())
  
# pop() method
dict2.pop(4)
print(dict2)
  
# popitem() method
dict2.popitem()
print(dict2)
  
# update() method
dict2.update({3: "Scala"})
print(dict2)
  
# values() method
print(dict2.values())
```
Output:
```
{1: 'Python', 2: 'Java', 3: 'Ruby', 4: 'Scala'}
{}
Python
dict_items([(1, 'Python'), (2, 'Java'), (3, 'Ruby'), (4, 'Scala')])
dict_keys([1, 2, 3, 4])
{1: 'Python', 2: 'Java', 3: 'Ruby'}
{1: 'Python', 2: 'Java'}
{1: 'Python', 2: 'Java', 3: 'Scala'}
dict_values(['Python', 'Java', 'Scala'])
```

---
