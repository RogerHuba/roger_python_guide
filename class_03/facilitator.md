# File I/O

## Dad Joke of the Day

- My wife asked me to sync her phone, so I threw it into the ocean. I don’t know why she’s mad at me.
- Why do you never see elephants hiding in trees? Because they’re so good at it.

### Group Breakout

Given a string, write a function that returns a new string but only has one of each character
Exampe: 'commissioner'
Return: 'comisner'

Example: 'aggressiveness'
Return: 'agresivn'

### When you need help

- [W3Schools](https://www.w3schools.com/python/python_reference.asp)
- [Python Cheatsheet](https://overapi.com/)

### Tuples / Set

- A tuple is one of 4 built-in data types that Python uses. The other 3 are list, set, and Dictionary. A tuple is immutable.

 ```python
my_tuple = (1, 2, 2, 3, 3, 4)
print(f'My Tuple is : {my_tuple}')
my_tuple.insert(0,0)

my_list = [1, 2, 2, 3, 3, 4]
my_list.insert(0,0)
print(my_list)
print(*my_list)

my_set = set(my_tuple)
print(f'My Set is : {my_set}')
my_tuple = tuple(my_set)
print(f'My New Tuple is : {my_tuple}')
```

### Iterating Through a String

```python
my_string = 'This is a string that I have here'

for char in my_string:
    print(char)

# The * will unpack an iterable
# print(*my_string)
```

### Exceptions

> Exceptions handle errors that you can't know about until running the application. They are different than errors that are known about in advance.

```python
print("let's do something totally wrong. See if you can spot me in the output!")
print("Too many parentheses"))
```

```python
print("More wrongness. Do I get printed?")
print("Who has ever "messed up" quotations marks?")
```

> Notice how both failed to execute AND didn't show the initial print. That's what happens with syntax errors. But how about logical errors that ARE syntactically correct?

```python
print("What happens now? Do you see me printed?")
value = 1/0
```

> Got a ZeroDivisionError at runtime. Notice intial print DID display this time. Check out the error. Getting a descriptive error is good. WAY better than getting a non-descriptive or even non-existent one. So always pay attention to anything an error is telling you.

```python
# You can handle these errors in your code``

try:
    print("Divide by zero again", 1 / 0)
except ZeroDivisionError:
    print("Don't divide by zero silly.")

print("handled the exception above, carrying on")
```

> Notice that we "caught" a specific exception. It is a best practice to only catch specific exceptions.
> To put it another way it is a VERY BAD THING to catch generic exceptions. Here is why that's considered an anti-pattern

```python
try:
    print("Divide by zero again", 1 / "spam")
except:
    print("Don't divide by zero silly.")

print("Total lie!. The problem was not dividing by zero. It was a type error")
```

> If you must handle every exception then make sure to retain the relevant error info. For example, you may have requirement that end user never sees a program error. In that case make sure to log/record the error details and then present something more palatable to end user

```python
try:
    spam = "nonsense" / 42
except ZeroDivisionError:
    print("Don't divide by zero silly.")
except Exception as e:  # notice we can refer to the exception using 'as'

    print("So sorry end user. Something broke!")

```

> Python also allows you do a couple more things with exceptions. One is an 'else' block which runs when there was NOT an exception. This is not that commonly used but every now and then is helpful

```python
print("Attempting to create message")
try:
    message = "nothing" + "wrong" + "here"
except TypeError:
    print("Unable to create message")
else:
    print("Message successfully created")
```

> The last piece is the 'finally' block which is run no matter what happened

```python
print("prepare for breakage")

try:
    value = True + " nonsense"  # change to str(True) and see what happens
except TypeError as e:
    print(f"Something broke! Details: {e}")
else:
    print(f"smooth sailing. value is {value}")
finally:
    print("clean up mess as needed")
```

> You can raise exceptions intentionally as well. If there's no better choice can use the Generic Exception. It's a best practice to choose the most appropriate type of Error.

```python
age = 20

if age < 21:
    raise ValueError("Invalid age - Gotta be at least 21 for this Party!")
    # or
    raise Exception("Invalid age - Gotta be at least 21 for this Party!")
```

### Read Files

Show the spam.txt file that there is something in there. Lets do something to it.

```python
file = open('assets/spam.txt')
print(file)
```

> When we print this we get an object in Pyton. Not a lot we can do with that.  Lets adjust.

```python
contents = file.read()
print(contents)
```

> That is all fine and dandy. We opened the file, we read and printed the content.
QUESTION: What is wrong with this scenario?
ANSWER: We left the file open.

> We can verify that with some code.

```python
# The file is still "open"
print('Is file closed?', file.closed)
```

> We have the ability to force it closed.

```python
# let's explicitly close it
file.close()
print('Is file closed?', file.closed)
```

- Often you don't need to worry about closing the file since Python usually handles that.
- But words like 'often' and 'usually' are a programmers constant foe.
- Fortunately, there's an easy way to make sure that it always gets closed up properly.

```python
with open('assets/spam.txt') as file:
    print(file.read())

print('file is closed?', file.closed)
```

- That `with` key word there creates something called a `context manager`
- They are a more advanced topic, but you'll see them used a lot with files because they are so dang handy.

> Quick documentation with help and dir. YOu can see the attributes of a file object easy enough.

```python
help(file)
dir(file)
```

If you dig through the file help you will come across some talk about file modes.

- When you open a file you supply a 'mode' - the default mode is 'r' for 'read'
- so `open('somefile.txt')` is the same as `open('somefile.txt','r')`
- You pretty much have to memorize the modes
- Luckilly there aren't that many. Here are the most popular
  - r for read
  - w for write
  - a for append

```python
with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()

for x in contents[:128]:
    print(type(contents))

with open('assets/brain.copy.jpg', 'wb') as f2:
    f2.write(contents)
```

### Review the Lab for Today

- Show the given sample mad-lib
- Show the same output expected.
