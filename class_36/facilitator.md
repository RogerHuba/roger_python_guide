Group Challenges

## Challenge #1 (20 Min)

Write a function to determine if a sentence is a panagram.  A panagram is a sentence or expression using every letter of the alphabet at least once.  Return 'True' or 'False"

> The quick brown fox jumps over the lazy sleeping dog.
> Five quacking Zephyrs jolt my wax bed.

An 'A' or an 'a' will count as 1.

You CANNOT use the string library

```python
# Usint panagram
  
def ispangram(str: word): -> boolean
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    for char in ALPHA:
        if char not in word.lower():
            return False
  
    return True
```

```python
import string
  
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    return set(string.lower()) >= alphabet
```

```python
def is_panagram(str):
    is_str_pan = True
    for num in range(97, 123):
        if chr(num) not in str.lower():
            return False

    return is_str_pan
```

## Chalenge #2 (35 Min)

Given a LL and an int, delete all nodes where the node value is > the given int.

(ll, 18)

[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[2]-> [1] -> [12] -> None

(ll, 2)

[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[1] -> None

```python
def delete_over(ll, num):

    at_head_node = True
    current = ll.head

    while at_head_node and ll.head:
        if not ll.head.next and ll.head.value > num:
            ll.head = None
            return ll
        elif ll.head.value > num:
            ll.head = current.next
        else:
            at_head_node = False
    
    while current.next:
        previous = current
        current = current.next
        if current.value > num:
            previous.next = current.next
    return ll       
```

## Challenge #3 (40 Min)

Write a function that takes a binary search tree as an argument, as well as some integer. Check if a node value equals the given integer. If there does, return True. Otherwise, return False.

```python
def bst_contains(input_tree, value):
  node = input_tree.root
  while node is not None:
    if value == node.value:
      return True
    elif value < node.value:
      node = node.left
    else:
      node = node.right
  return False
```
