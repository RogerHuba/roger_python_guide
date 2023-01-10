# 10000 3

## DAD Jokes

- What do you get from a pampered cow?  
  - Spoiled milk.
- Why did the hacker organize a marathon?
  - He wanted to make money from people who "ran somewhere"

## Warm Up - QUESTION

> Convert tuple into a list of squared values

```python
nums = (1,2,3,4,5)

squares = None # make squares pass test

assert squares == [1,4,9,16,25]
```

## Overview of today's warm-up challenge

```python
nums = [1,2,3,4,5]
squares = [num ** 2 for num in nums]
assert squares == [1,4,9,16,25]
```

## Code Challenge

> Given a 2 linked lists, write a function that returns the count of duplicate values

Sample Data
1 -> 3 -> 8 -> 13 -> None
2 -> 3 -> 8 -> 23 -> None

return 2


```text
Algo
def function count_common_nodes
  current1 assigned to ll1 head
  current2 assigned to ll2 head
  set count to 0

while current1 is not None
   while current2 is not None
      if (current1 == current2):  We want to look at values
          count = count + 1
      Move current2 to current2.next
    increment current1 to current1.next
    current2 to ll_2.head
return count
```

```python
# o(n^2) time
def count_common_nodes(ll_1, ll_2):
    current1 = ll_1.head
    current2 = ll_2.head
    dupes = []

    while current1:
        while current2:
            if current1.value == current2.value:
                dupes.append(current1.value)
            current2 = current2.next
        current1 = current1.next
        current2 = ll_2.head

    return len(dupes)
```

```python
# o(2n) time
def count_common_nodes(ll_1, ll_2):
    current1 = ll_1.head
    current2 = ll_2.head
    list1 = []
    count = 0

    while current1:
        list1.append(current.value)
        current1 = current1.next
    
    while current2:
        if current1.value in list1:
            count += 1
        current2 = current2.next

    return count
```

### Lecture Exit Example

- There is an area in the tests that could give you some un-expected behavior if you have not implemented sys.exit. If you end your script without a true exit, your script stops executing, but the script is still open. Evenutally garbage collection will fix this but we don't like to rely on things like usually, eventually, sometimes. We want things handled. There is a way to catch the code and make sure we get a graceful exit.

```python
import sys

def main():
    name = input('Please Enter your Name: ')
    end_game = 'a'
    while end_game != 'q':
        print(f'{name}, please press q to quit!')
        end_game = input('> ')
    quit_game('Thanks for Playing.')

def quit_game(message):
    sys.exit(message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit_game('Keyboard Interrup Detected')
```

### 10000

> Review the Lab Feature Tasks and Requirements

> Here we are on the hump lecture of module 2. We have been trying to wrap our heads around what being pythonic really is. How do we make pythonic code? Python has very little in the way of rules. Most of the expectations are more conventions.

- Tonight we are going to review a few Classes and methods and discuss what is going on with them.

```python
class Banker:
    """Banker is reponsible for tracking points "on the shelf" and "in the bank"
    version_1
    """
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0
```

```python
    @staticmethod
    def roll_dice(num=6):
        # version_1

        return tuple([randint(1, 6) for _ in range(num)])
```

```python
    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()
```