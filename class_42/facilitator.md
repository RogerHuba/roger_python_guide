# Pythonisms

## Jokes

- Which is faster, hot or cold? Hot, because you can catch a cold.
- Where do baby cats learn to swim? The kitty pool.
- What do you call your grandma’s number on speed dial? Instagram

## Warmup

- Create a function that takes a linked_list and an action

## Whiteboards

- Whiteboards are in progress now.  Give pass / fail statistics.

## Lecture

- > Review the Lab for today.
- > Pythonisms, pythonista, these are real things. Simple and elegant. The creator of Python created pyhon to mimic art and poetry, hence all the indentation and whitespace. In poems, spacing matters for contenxt. Sounds cooky, you can see some of the design decisions that are make along the way. They don't get all the way there of course, but I have yet to see a language closer than Python does.
- > Today we are going to expore some of the language features to show our command of the lanugage. We dove into some of this with your reseach on libraries but we can look a little deeper and the language itself.
- > When are you a TRUE Pythonista? We can compare this to people that know multiple languages. How does one know when they truly understand the second language. One of the best ways I have heard is when you can tell or understand jokes in another language. Jokes have so many twists and innuendos , also relying on slang in the language. Unless you have a full understanding of the lanuguage you may not fully understand a joke. Today we are going to dig a little depper into the python language and get closer to being a true pythonista.

## Demo

- > Today's lab asks you to use interators / generators on a custom collection to do some things.
- > I am going to do this using a linked list (hence the warm up to get your mind fresh). I am going to apply some pythonic features so that we can interact with that list in a condenced and concise way. In fact, I am going to make it so that we can iterate thought a linkedlist and not have to traverse. With that said lets do some code.

- create a poetry environment
  - create a `linked_list_iterator.py` file.
  - shell up
  - Copy the test file over.
  - code .

- Have the test_linked_list_interator.py file open and so we can go through the tests.
- Copy the linked_list class, node class, __init__, append, and insert methodsinto the file. Show the reversed method and how it is quickly creating a linked list.

Should like like this:

```python
class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): 
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_
```

- Comment out all but the first test.
- Run the test.
- > We fail. Of course we fail because a linked_list is not iterable, at least not yet. How do we make it iterable?  The readings talk about that a little.  Let's explore this.
- Open the Iterators Reading
- > This was the first way that Python discovered how to do this. And it works, you may see this in code on the job, but this is a little wordy, not quite as pythonic as we would like. There is a better way with a fusion of generators and iterators. So what am I talking about here?
- > A Generator sounds like a confusing concept but it is pretty slim in how it works.

What is a Generator

- Generator functions differ from regular functions as they have one or more yield statments.
- When they are called, it returns an object (iterator) but does not start execution immediately.
- Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- Finally, when the function terminates, StopIteration is raised automatically on further calls.

- Add the following to the end of your `linked_list_iterator.py`

```python
if __name__ == "__main__":

    def gen():
        for i in range(10):
            yield i
    
    num_gen = gen()
    print(num_gen)
```

- > When we run this we get generator object printed. The yield in the gen() function turns the return into a generator object. Yield is like a return, but a return that pauses things. It gives us back one item at a time. First time this runs, it will yield 0 because our range is 0 to 9. Then next time we call it, it will return us 1, the next time we call, 2, so forth and so on until it gets to the end. Lets look at the next value.

- add this after the print(num_gen)

```python
print(next(num_gen))
```

- > Next is a builtin method that operates on an iterator.
- Run the code and show it printing 0. Run it 2 or 3 times.
- Every time it yields 0. What can you infer from what we just did?
  - Trying to get them to talk about the generator resets everytime the code is run.
- In VS Code using `shift-option down` duplicate the line uo to 9.  Run it and see the full list
- Add one more line and show we get an StopIternation error

- Add a try except to show this:

```python
try:
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
except StopIteration:
    print('All Done')
```

- > What would happen if we add a generator outside of the try catch?
- > Generators are one and done. If you want do another set, then you have to re-generate.

`add this to the end of the function`

```python
      num_gen = gen()
    print(next(num_gen))
```

- > When we create a generator, we are limited on the the range.  What if we wanted to keep a counter going forever?

- Add a new function of code:

```python

def gen2():
    i = 0
    while True:
        yield i
        i += 1
```

- Then change the prints to:

```python
num_gen = gen2()
for i in range(10):
    print(next(num_gen))
```

- > This gives us an infinate loop, but not really an infinate loop becase we are calling it one item at a time. Push the envelope to 100k then to 1 million and watch the speed.

- > Let's see how we can use these generators to help us with passing our test.

- Run `pytest` again and show the LinkedList is not iterable.
-> But we want this to be iterabel. We really really want this to be iterable in a for in loop. How do we do this? There are many things in python that are iterable. The way they define themselves as iterable is by overriding a `__dunder` method. That `__dunder` method is `__iter__`.

- add to code under __init__

```python
# it is a method so it needs self.
__iter__(self):
```

- > It needs something to be returned that represents that iterableness. It needs a notion of what is next. If we tap into the power of generators we can make this happen.

- > Make an inner function.

```python
def __iter__(self):

    def value_generator():

        current = self.head
        while current:
            yield current.value
            current = current.next
        
    return value_generator()
```

- > What we have here is a value generator that will yield one linked list node at a time for us. value_generator can be whatever you want (potatoe).  __iter__ needs to be called. Let's see if this is enough to pass our test. Success. Using a generator and a few lines of code, we can now iterate through a linked list.
- > It turns out just by being iterable, we get some other things for free. (free is always good). What do I mean by that.  Lets look at our next test.

- > Lets add a new test to check on todays warmup.  Sum tthe total of a LL.

- Add the following:

```python
# @pytest.mark.skip("pending")
def test_sum_values():
    ll_values = LinkedList((10,20,30))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 60
```

- > By being iterable we can use it inside of a list comprehension. Just a silly little test that convets sith to uppercase.  sith_lords is a linked list. So we can now use a linked list in a for in loop as well as a for loop with list comprehension.  Could be a tuple comprehension as well. What else do we get.

- Uncomment out the next test.

We can turn a linked list into a list presentation.  We can already do something like that with a string.

- Add to main method to show.

```python
list('abc') - > ['a', 'b', 'c']
```

- > Now what happens when we run list on our LinkedList?  Sure enough we get a passing test.

- > What else can we do.  

- Un comment next test.
- > Now we are passing in a range.  Will we be able to convert range.  Yes, range under the hood uses a __iter__ method.  That is not the problem with our test.  Our test is looking for a len method. We don't have that yet. Any thoughts how we can add a len in?  __len__()

- add the following under __iter__():

- > We could do a few things here like keep track of the len with a counter and return the counter. Not as pythonic as I would like.  I'm going to do something else.

```python
def __len__(self):
    return len(iter(self))
```

- > Still not quite working. What does __iter__ return?  It returns a generator.  How do we turn a generator into a list?  list().  One small change for us.

```python
def __len__(self):
    return len(list(iter(self)))
```

- > There we go. Is this the most efficient or the only way.  No, but this is an example of how you can find these notions of using generators and __dunder methods to do some cool things.

- > Whats next.  Can we do filters inside of our list comprehensions? Lets try it out.  Apparently we can and we didn't need to do anything else.  In this canse we didn't need to do anything else.  num in nums with the else of modulo 2. This is a filter to give us just the odd numbers. Checking to see if num mod 2 is truthy. If num mod 2 is 0 then it is even and 0 is not truthy. that gets it into the collection of odds.

- > In our next test we are just iterating over the linked_list one item at a time using next.

- > The next test runs through the linked list until it stops.
- > We can see the power of what a generator can do for us. I did this example on a linked_list, but could we do this on something like a tree?  We absolutely could.

- > You may remember from way back in the day when you were implementing LinkedList (or even perhaps recently when you were reviewing your LL), you had a `__str__` method on your ll class. If we wanted to get a string representation how can we accomplish this. Specifically in a way that builds on some of the pythonic concpets we have covered?

- > Here is a hint. We know we can slowly iterate through our linked list. That functionality already exists in our code. We can just concat it . Something like this.

```python
def __str__(self):

    out = ''
    for value in self:
        out += f'[ {value } ] -> '
    out += 'None'
    return out
```

- > That did not take a lot to do. In fact not just very little code but also very simple to understand.

- > Uncomment the test_equals and talk about wanting the ability to compare LL like we do lists.  Show that out of the box it won't work with the built in because it is just comparing the memory locations which are obviousely different.

- Add the following line. Once we made our LL iterable, it simplifies things for us.

```python
def __eq__(self, other):
    return list(self) == list(other)
```

- Uncomment the Get items test items.
- > I want to treat my ll like a regular list and access them like a list. We could do this like so:

```python
return left(self)[index]
```

```python
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError
```

- Depending on time left, open a deco.py file

- Add this code in to create your own thing.

```python
from functools import wraps
def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Yo mamma says "{orig_val}"'
    return wrapper

def sophisticated_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'It is with a great honor that I hear you say "{orig_val}"'
    return wrapper


# @yo_mamma_decorator
# @sophisticated_decorator
def just_saying(txt):
    return txt


if __name__ == "__main__":
    print(just_saying('I love star wars!'))
```

- > You may want to talk about the difference between *args and **kwargs

```python
sith1 = 'Darth Revan'
sith2 = 'Darth Vader'
sith3 = 'Darth Bane'

# NOTE: args is just a name.  potatoe

def siths(*args):
    for sith in args:
        print(f'{sith} is a Dark Lord of the Sith!')
```
