# Challenges

## Individual Challenge #1 (15 Min) -> Review (30 Min)

WB only.  Individual. Given 2 numbers and an operator (+-*/), write a function that returns the (sum, difference, product, or quotient). You may get negative and positive ints, and zero.  The problem will be handled like number1 + number2, number1 / number2, number1 + number2, number1 - number2.

Have every individual share their WB and critique items on the WB.  Do not critique the code or algo (not enough time)

## Group Challenge #2 (20 Min) -> Review Possible Solutions (10 Min)

Write a function to determine if a sentence is a panagram.  A panagram is a sentence or expression using every letter of the alphabet at least once.  Return 'True' or 'False"


> The quick brown fox jumps over the lazy sleeping dog. -> True
> Five quacking Zephyrs jolt my wax bed. -> True
> The quick brown fox ->

An 'A' or an 'a' will count as 1.

You CANNOT use the string library

```python
# Usint panagram
  
def is_pangram(word):
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    for char in ALPHA:
        if char not in word.lower():
            return False
      return True
```

```python
def is_panagram(word):
    for num in range(97, 123):
        if chr(num) not in word.lower():
            return False

    return True
```

## New Group Chalenge #3 (30 Min) - Review (10 Min)

Given a list and an int, where each index in the list is is a LL, write a function that deletes all nodes where the node value is greater than the given int.

(lst, 18)
[ll1, ll2, ll3]
 
 ll: Int: 10
[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[2]-> [1] -> None

(lst, 2)
[ll1, ll2, ll3]

ll1:
[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[1] -> None

```python
def delete_over(ll, num):

    for ll in lst:
        at_head_node = True
        current = ll.head

        while at_head_node and ll.head:
            if not ll.head.next and ll.head.value > num:
                ll.head = None

            elif ll.head.value > num:
                ll.head = current.next
            
            else:
                at_head_node = False
        
        while current:
            previous = current
            current = current.next
            if current.value > num:
                previous.next = current.next
    return lst       
```

## Group Challenge #4a (30 Min)

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

## Group Challenge #4b (30 Min)

Write a function that takes 2 linked lists, of single digit, positive numbers, and add the "numbers" represented by the LL's.

ll1: [1]->[0]->[0]-> None
ll2: [2]->[2]->[2]-> None
100 + 222 = 322

```python
def ad_ll(ll1, ll2):
    ll1_num = ''
    ll2_num = ''
    current1 = ll1.head
    current2 = ll2.head
    if not ll1.head and ll2.head:
        return 0
    while current1 or current2:
        if current1:
            ll1_num += str(current1.value)
            current1 = current1.next
        if current2:
            ll2_num += str(current2.value)
            current2 = current2.next
    return int(ll1_num) + int(ll2_num)

```