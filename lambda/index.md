**Python Lambda**
=============

- [**Python Lambda**](#pythonlambda)
  - [**Syntax**](#syntax)
  - [**The expression is executed and the result is returned:**](#the-expression-is-executed-and-the-result-is-returned)
  - [**Lambda functions can take any number of arguments:**](#lambda-functions-can-take-any-number-of-arguments)
  - [**Summarize argument `a`, `b`, and `c` and return the result:**](#summarize-argumentab-andcand-return-the-result)
- [Why Use Lambda Functions?](#why-use-lambda-functions)
- [Python lambda properties:](#python-lambda-properties)
  - [**Program to demonstrate return type of Python lambda keyword**](#program-to-demonstrate-return-type-of-python-lambda-keyword)
  - [**Invoking lambda return value to perform various operations**](#invoking-lambda-return-value-to-perform-various-operations)
  - [**Difference between lambda and normal function call**](#difference-between-lambda-and-normal-function-call)
  - [**The lambda function gets more helpful when used inside a function.**](#the-lambda-function-gets-more-helpful-when-used-inside-a-function)


In Python, an anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
for Example
```py
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))
```

- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.

## **Syntax**
```
lambda *arguments *: *expression*
```

## **The expression is executed and the result is returned:**
```py
# Example

Add 10 to argument `a`, and return the result:

x = lambda a : a + 10\
print(x(5))

```

## **Lambda functions can take any number of arguments:**
```py
# Example

Multiply argument `a` with argument `b` and return the result:

x = lambda a, b : a * b\
print(x(5, 6))

```


## **Summarize argument `a`, `b`, and `c` and return the result:**
```py
### Example
x = lambda a, b, c : a + b + c\
print(x(5, 6, 2))
```


# Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
```py
def myfunc(n):\
  return lambda a : a * n
```

**Use that function definition to make a function that always doubles the number you send in:**
```py
# Example

def myfunc(n):\
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```


Or, use the same function definition to make a function that always *triples* the number you send in:
```py
# Example

def myfunc(n):\
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

```

Or, use the same function definition to make both functions, in the same program:
```py
### Example

def myfunc(n):\
  return lambda a : a * n

mydoubler = myfunc(2)\
mytripler = myfunc(3)

print(mydoubler(11))\
print(mytripler(11))

```

# Python lambda properties:
This function can have any number of arguments but only one expression, which is evaluated and returned.

One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.

It has various uses in particular fields of programming, besides other types of expressions in functions.

## **Program to demonstrate return type of Python lambda keyword**
```py
string = 'GeeksforGeeks'
 
# lambda returns a function object
print(lambda string: string)
```
Output
```
<function <lambda> at 0x7fd7517ade18>
```
> **Explanation:** In this above example, the lambda is not being called by the print function, but simply returning the function object and the memory location where it is stored. So, to make the print to print the string first, we need to call the lambda so that the string will get pass the print.


## **Invoking lambda return value to perform various operations**

Here we have passed various types of arguments into the different lambda functions and printing the result generated from the lambda function calls.

```py
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))
 
do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))
 
find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))
```
Output:
```
filter_nums(): Geeks
do_exclaim(): I am tired!
find_sum(): 2
```

## **Difference between lambda and normal function call**

The main difference between lambda function and other functions defined using def keyword is that, we cannot use multiple statements inside a lambda function and allowed statements are also very limited inside lambda statements. Using lambda functions to do complex operations may affect the readability of the code.

```py
def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y
 
 
lambda_cube = lambda num: num ** 3
 
# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))
```
Output:

```invoking function defined with def keyword:
Finding cube of number:30
27000
invoking lambda function: 27000
```

## **The lambda function gets more helpful when used inside a function.**
We can use lambda function inside map(), filter(), sorted() and many other functions. Here, we have demonstrated how to use lambda function inside some of the most common Python functions.

```py
l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(l, key=lambda x: int(x)))
 
# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:",
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))
 
# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), l)))
```      
Output:
```
Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
Filtered positive even numbers: ['1', '9', '0', '-1', '-2']
Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']
```

---
