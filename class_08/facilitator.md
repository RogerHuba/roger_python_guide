# Game of Greed 3

## DAD Jokes

- What do you get from a pampered cow?  
    - Spoiled milk.
- Why did the hacker organize a marathon?
    - He wanted to make money from people who "ran somewhere"



## Warm Up - QUESTION

```python
employees = [
    {'name': 'John Conners', 'seniority': 10},
    {'name': 'River Tam', 'seniority': 3},
    {'name': 'Bilbo Baggins', 'seniority': 12},
    {'name': 'Harry Potter', 'seniority': 7},
    {'name': 'Darth Revan', 'seniority': 19},
    {'name': 'Khan', 'seniority': 6},
    {'name': 'Dobbie', 'seniority': 1},
    {'name': 'R2D2', 'seniority': 6}
]

# Challenge #1
filtered_employees_one = []

if filtered_employees_one == ['John Conners', 'Bilbo Baggins', 'Darth Revan']:
    print('SUCCESS Test One')

# Challenge #2
filtered_employees_two = []

if filtered_employees_two == ['River Tam', 'Bilbo Baggins', 'Khan', 'R2D2']:
    print('SUCCESS Test Two')
```

## Warm Up - QUESTION

```python

# Challenge #1
filtered_employees_one = [
    employee['name'] for employee in employees if employee['senority'] i >= 10]

if filtered_employees_one == ['John Conners', 'Bilbo Baggins', 'Darth Revan']:
    print('SUCCESS Test One')

# Challenge #2
filtered_employees_two = [
    employee['name'] for employee in employee if employee['senority'] i%3 == 0]

if filtered_employees_two == ['River Tam', 'Bilbo Baggins', 'Khan', 'R2D2']:
    print('SUCCESS Test Two')
```

## Code Challenge
> Given a 2 linked lists, return the count of duplicate values

Given 2 ll, return the count of duplicate values

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
    count = 0

    while current1:
        while current2:
            if current1.value == current2.value:
                count += 1
            current2 = current2.next
        current1 = current1.next
        current2 = ll_2.head

    return count
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
### Exit Example

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
### Lecture
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
