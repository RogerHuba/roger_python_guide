# Class 02

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

We can see the name has changed in first.p. Lets copy that print code from first to second.

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
