# Game of Greed II

## Dad Jokes

- Why are skeletons so chill?  Because nothing gets under their skin.
- Why was the robot so tired after his road trip? He had a hard-drive.
- Why didn't the melons get married?  Because they cantaloupe.
- What kind of egg did the evil chicken lay?  A deviled egg.

## Whitebaord (groups)

- Write a function that takes a linked_list with single letters as values, and returns all the letters in a single string.
`[p] -> [y] -> [t] -> [h] -> [o] -> [n] -> None`
- returns 'python'

## Linked List Deep Dive / Another Whiteboard

- use [Invision](https://rogerhuba592985.invisionapp.com/freehand/linked-list-Y8JWBcq8h)
- Various option shere.  
  - Code from scratch
  - Bring up working code and walk through with truth tables

### Feedback

- There were some grumblings in the learning journal about having to build a game. Some students were asking why we are building a game instead of a more serious application.
- I can give you a great answer there. Games are often a lot more complex because of the randomness and chance that are involved in them.
- When you think about something like Bus Mall or Salmon Cookies, the application was pretty straight forward. There was a small element of randomness with picture that was shown or the total cookies that were sold. In game of greed, the entire app is based of chance and user input. There are so many different paths than can take place.
- There are so many additional moving parts to keep track of and to have to account for.

### Review the Lab Requirements

- Mention that tests will be provided again.
- Mention the automation of testing.
- Talk about making sure to get your commits in.
- Testing is the feature requirements for this lab.
- How do we test input and output and randomness?

### Builtins

- Go over the quick builtin demo on changing things.

```python
import builtins

_print = builtins.print
_input = builtins.input

def alter():
    builtins.print = _input
    builtins.input = _print

def alter_back():
    builtins.print = _print
    builtins.input = _input

print('This is a General Print Statement')
alter()
print('This is a General Print Statement or am I?: ')

input('I Want to grab some info > ')
input('Wait, What just happen there?')

alter_back()

print('Am I back to Print?')
input('Can I grab info again?: ')
```

### Game of Dice

- Show the existing tests.
- Play the game and simulate the tests.

```python
from random import randint

def default_roller():
    return (randint(1, 6,), randint(1, 6,))

def play_dice(roller=default_roller):
    while True:
        print("Enter r to roll or q to quit")
        choice = input("> ")

        if choice == "q":
            print("OK, bye")
            break
        else:
            roll = roller()
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")

if __name__ == "__main__":
    # rolls = [(5, 6), (6, 1)]
  
    def mock_roller():
        # return (1, 1, 1, 1)
        return rolls.pop(0) if rolls else default_roller()

    # play_dice()
    play_dice(mock_roller)
```

pytest -k version_1

You will need this pytest.ini (which will be up in the folder today)

### Pytest Coverage Tests
- pip install pytest-cov
- pytest --cov
https://pytest-cov.readthedocs.io/en/latest/plugins.html
