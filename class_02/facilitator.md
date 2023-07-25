# Class 02

## Jokes

- Why is Peter Pan always flying? Because he Neverlands.
- Why did the coach go to the bank? To get his quarterback.
- I lost my job at the bank on my first day. A woman asked me to check her balance, so I pushed her over.

Testing and Modules

## if __name__ == "__main__"

> Lets take a deeper look at `if __name__ == "__main__":`. What is this doing and why do people use it? Let's print out this __name__ and see what it gives us.

```python
# in first.py
print(f'First Modules Name: {__name__}')
```

> I ran first.py you can see that when I printed __name__, it printed __main__. What is going on here? When Python runs a file, before it executes any code it sets a few special internal variables. __name__ is one of those special variables. When a python executes a python file directly, it sets the __name__ to __main__. With Python we are also able to import files to execute. When a module is executed, __name__ is set to the name of the file. Let's try this out.

```python
# in second.py
# When you import the whole file, it executes all code in the file. (Well mostly)
import first
```

Run `python second.py`

We can see the name has changed in first.py. Lets copy that print code from first to second.

```python
# add to second.py
print(f'Second Modules Name: {__name__}')
```

> Let's add a little more code to first.py

```python
def main():
    print('I am running from with the main function')

if __name__ == '__main__':
    main()
```

## Demos: Test Driven Development

Two demos today. One on FizzBuzz to really drill down on the process of TDD. The second on recursion. Both are small amounts of final code but big conceptually.

## FizzBuzz

> `../demo/fizz-buzz`

Solve classic FizzBuzz challenge using Test Driven Development

- > `mkdir fizz-buzz`
- Create/Activate virtual environment.
  - note convention of using hyphen vs. underscore at this level
- `cd fizz-buzz`
  - show tree of generated files
  - `fizz_buzz` sub folder
  - `tests` sub folder
- `pip install pytest`
  - installs dependencies into virtual environment
  - note `.venv` directory
  - note the `(.venv)` in terminal prompt.
  - export requirements
    - > pip freeze > requirements.txt
- run `pytest`
  - should get `bash: pytest: command not found`
- run `pytest` again and see what happens
  - should get on test collected and passing
  - point out that `pytest` was installed by default
  - point out that a single test already included
- pause and talk about FizzBuzz then move on to coding out using TDD
- write first test:

        def test_fizz_buzz_one():
          actual = fizz_buzz(1)
          expected = "1"
          assert actual == expected

- run `pytest`

## Recursion

> `../demo/recursion`

- The demo is very small amount of code. But it's recursive so it can do a lot with a little.
- The problem is computing the factorial of a number.
- Make sure to model stepping through and tracking variable values the way the interpreter would.
- **NOTE:** The code for recursion demo uses wordy folder/file names to make clear distictions between packages and modules.
  - Reiterate to students that you wouldn't see that naming convention used otherwise.
