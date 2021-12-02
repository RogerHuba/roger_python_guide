# File I/O

## Dad Joke of the Day

- My wife asked me to sync her phone, so I threw it into the ocean. I don’t know why she’s mad at me.
- Why do you never see elephants hiding in trees? Because they’re so good at it.

## Truth / Falsy

 ```python
 stuff = None

if stuff:
    print('This will evaluate as a Falsy Statement')
else:
    print('This will evaluate as a Truthy Statement')

# Things to check
#1 Empty String
#2 0 
#3 False
#4 True
#5 '0'
#6 []
#7 [False]
#8 {}
```

 ## Tuples / Set

- A tuple is one of 4 built-in data types that Python uses. The other 3 are list, set, and Dictionary. A tuple is immutable.

 ```python
my_tuple = (1, 2, 2, 3, 3, 4)
print(f'My Tuple is : {my_tuple}')

my_set = set(my_tuple)
print(f'My Set is : {my_set}')
my_tuple = tuple(my_set)
print(f'My New Tuple is : {my_tuple}')
```

## Iterating Through a String

```python
my_string = 'This is a string that I have here'

for char in my_string:
    print(char)
```

### Group Breakout

Given a string, write a function that returns a new string but only has one of each character
Exampe: 'commissioner'
Return: 'comisoner'

Example: 'aggressiveness'
Return: 'agresivn'

### Review the Lab for Today

- Show the given sample mad-lib
- Show the same output expected.

### Read Files
