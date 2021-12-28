# Game of Greed

## Today's Dad Jokes

- What’s Forrest Gump’s password? 1forrest1.
- I used to hate facial hair, but then it grew on me.
- Did you know that the first french fries weren’t cooked in France? They were cooked in Greece.
- A panic-stricken man explained to his doctor, “You have to help me, I think I’m shrinking.” “Now settle down,” the doctor calmly told him. “You'll just have to learn to be a little patient.”

## Warm Up

- Run warmup/random.py
- Will result in a circular import error.
- Give students 5 min in breakout rooms to figure out.
- Change the name of the file and run it, everything is will work just fine

## Warm up #2

- Given a linked_list, iterate the linked list and return the largest value
- input_linked_list (7)->(2)->(13)->(9)->(3) expected return (13)

```python
def largest_value(ll):
  largest = 0
  current = ll.head
  while current:
    if current.value > largest:
      largest = current.value
    current = current.next

  # code here, change return to largest number
  return largest
```

## Go over Lab Requirements

- Bring up Online Game first.
- Go through the rules
- Play a few games
- Show different situations that come up

## Show what the game should look like at the end of the week

- Need to pull up Python Guide Game of Greed

## Go through Lab Requirements Again

- This time go through and touch base on Feature Requirements

## Go Through Tests for Lab

- Make sure that tests were copied to class repo.
- Let them know that test will be provided for this this version of game of greed.

## Create a Poetry Project for Game of Greed

- Use `poetry new game-of-greed`
- run `cd game-of-greed`
- run `mv README.rst README.md`
- run `poetry install`
- run `poetry add --dev black flake8`
- run `poetry shell`
- copy tests into test folder
- run `touch game_of_greed/game_of_greed.py`

- Time to talk about black and what it can do for you.
- [Link to Black Site](https://pypi.org/project/black/)
- Create a quick function in the game_of_greed.py.  Be sure to add bad formatting in ther
- run `black game_of_greed\game_of_greed.py` and watch the formater fix things.
- Open for discussion the things that this can do for us.

- Run pytest.

> Look at all of these failing tests!
> Your goal is to get all of these working.
> I would suggest not failing all of these tests because that clutters your screen
> QUESTION: What can we do to not show all of these failing tests?
> ANSWER: @pytest.mark.skip, could comment then out, could make all of the tests one big string

- What do you need to know in order to keep score?
- What do you need to know to calculate the score?
- What do you need to know ot roll the dice?

> Well Roll dice has to do with some randomness. This is something we briefly covered in todays warmup.

- Bring up [Random Module](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)
- the reading that was due today and show the random doc page.

```python
import random
print(dir(random))
# bring up the docs from above

some_random_int = random.randomt(1,10)
print(some_random_int)
```

> If you really do not like the resources from the reading.  Do a quick google search for `python roll dice`
> Talk about starting to look at [coverage](https://coverage.readthedocs.io/en/coverage-5.5/)