# Class 1 Introduction to Python

## Dad Joke(s) of the Day

- Why do astronaughts only use Linux? Can't open Windows in space.
- Did you hear about Bill and Melinda Gates Divorce.  Apparently Bill is going to let Melinda keep the house, but he is taking the Windows.

## Presentation Kickoff (30 - 45 Min)

- [401 Kickoff](https://docs.google.com/presentation/d/1CrJZW7G4NA8UCud69IXa1VFlvJxY18wkEqIMQ1J_vvU/edit#slide=id.ge708d69c0a_0_286)

## Introductions

- Who are you?
- What Brought You here?
- What was your target company before you started and what is it now?
- Fun Geeky Thing!

## Misc Things (5-10 Min)

- It is HARD
- Expectations are high (no longer in 201 or 301)
  - No more hand holding
  - More expectations from you.
  - Harder than the day course!
- Plagerism
- Designed for you to Struggle (this is where the learning happens)
  - You will FAIL a lot here as well as on the job.
  - You will work harder here than you will on the job.
  - You Will have to do a lot on your own to meet deadlines.
- Not just problem solving approach, but build toughness (be ok with failure)
- Once you get comfortable with were you are at, you will get promoted and have to start it all over again.

- There will be times where you have to just let a grade go.

## Class Logistics

- Canvas
  - Go through Syllabus
  - Go Over the weekly schedule
- Show Zoom Recording area
- Remo Setup Guide
- Course Repository
  - Review Overall Course breakdown in Course Repo

## Demo of Code

- Talk about following along with coding and instead just take notes.
  - If you fall behind, you lose focus and you may miss something.
  - If there is something you want to go back to, take note of the time so you can skip to that time in the video.
- Venv - Gives us a virtual Environment to be able to use different dependencies but not on a global level, only in the env
- Others, poetry, pipenv, pipx
- Demonstrate each of these commands
  - > python3 -m venv .venv
  - > source ./.venv/bin/activate MAC
  - > .\.venv\Scripts\activate

  -> pip install xxx
  -> pip install -r requirements.txt
  -> pip freeze > requirements.txt

- Open up PyCharm in the Virtual Environment.  Point out that PyCharm knows your in an environment but it may take a min to get there.
- > I'm sure you already know this but IDE's is not perfect.  Venv is not perfect either. There may be times where you are having problems and you need to burn your virtual environment and resetup.  Be ok with doing that. It gives you practice.

- > Now that we are here.  Let's write some code.

```zsh
touch demo/topics.py
```

- In topics add the following

```python
"""Things to cover...
* What is a module
* What is a script
* How to execute it from CLI
* print/input
* string concatenation
* formatted strings
* if __name__ == "__main__": snippet
"""
```

Question: Does anyone remember how to print something out?
Answer: We use the print statment

```python
print('Star Wars is the best')
```

- Print is a builtin function. We don't have to define this
- Let's Execute this as a script. This is calling the file and running it directly.

```bash
python demo/topics.py
```

Question: How about the input command?
Answer: yep. input

```python
print('Star Wars is the best movie?')

input('>')

answer = input('>')
print(answer)

print('Concat')
print('The best SW movie is ' + answer + '.')

print('older')
print('The best SW movie is {}.'.format(answer))

print('newer')
print(f'The best SW movie is {answer}.')
```

- > Lets Talk about functions.

```python
def movie(movie: str) -> str:
    return_string = f'The best SW movie is  {movie}'
    return return_string

print(movie())
```

NOTE: Talk about spacing in Python

- > There may be times where we want to run a file as a script, and other times we want to impoort a specific function

- Create a import_value.py file.
- import files and call it.

- Show `if __name__ == "__main__":`

```python
multi_line = '''
Here is some text
And some more text
And alas there is more
'''


print(mult_line)
better_multiline_string = dedent(multi_line)
print(better_multiline_string)
```

Open guessing game and walk through the code.
