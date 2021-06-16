# Classes

## Dad Jokes
- A ham sandwich walks into a bar and orders a beer. The bartender says, “Sorry, we don’t serve food here.”
- I remember as a kid, my dad got fired from his job as a road worker for theft. I refused to believe he could do such a thing, but when I got home, the signs were all there.
- How do you steal a coat? You jacket.

## Feed Survey Results
 - Show canvas statistics
 - The good
 - The bad

### Student 
 - Given an array, remove all duplicates, and return a new list of non dupes.  You cannot use a set.

 ### Review Lab 04
 - Go over the specifics of the class.
- Point out tests and lab starter files

### Demo
> QUESTION: What is a Class?
> ANSWER: A class creates a new type of object, allowing a new instance. Each instance can 
> ANSWER: have different attributest attached to it.
> If you know anything about me, you know my love for star wars. Today is the first of many Star Wars
> Demos to come. We will be building out the start of what could be a Star Wars Text game.

- Have a student walk you through poetry setup for star-wars
```
poetry new star-wars
cd star-wars-demo
poetry install
poetry shell
touch star-wars/star_wars.py
code .
```

> We are going to run todays Demo similar to your lab. I have tests already written.
> Copy the test file in and make sure that everything is skipped.
> NOTE: May need to poetry add pytest again to import it properly.

```python
pytest
```

- Show all the skipped Tests.  

> We are going to do some TDD, or Test Driven Development.
- Comment out the first pytestskip

> QUESTION: From your reading, how do we create a class?
> ANSWER: We use the class Key word

```python
class JediMaster:
    pass
```
- NOTE: Python classes by convention start with Capitals and are Pascal Case.
- Try to run Pytest. We should get an error because we have not imported anything.

```python
from star-wars.star_wars import JediMaster
```

- rerun pytest and should get a new passing test.
- Uncomment next test. No attribute `Name`

> As of this moment, all we have is an instance of JediMaster.  The instance has no
> attributes. If you remember back to your JS days you may remember this thing called
> a constructor. That is what we are going to build here. In python we call that a 
> __init__. It is short for initializer but ultimately is similar to what you know as 
> This will allow us to creat multiple instances of a jedi master.
> In JS you had a notion of `this`.  Python convention: use `self`. <- This is potatoe.
> Self represents the instance of the class and with this we can access the attributes and
> methods of the class.

```python
def __init__(self, name):
    self.name = name
```
> This gives is a name something to add. Look at the test and see what the test is needing
> In this case we create a JediMaster but do not provide a name but expect it to have one.
> We need to git a default name
> QUESTION: How do we give a parameter a default name?
> ANSWER `def __init__(self, name='Random Master):`

- Then add

```python
if __name__ == '__main__':
    yoda = JediMaster('Yoda')
    print(yoda)
    obi-wan = JediMaster('Obi-Wan')
    print(obi-wan)
```

- Run the file as a script.  `python star_wars/star_wars.py` and see the output objects. 
> We will fix this a little later.

- Uncomment the next test and run it.  PASSED.  Walk through the test.
- Add an additional test to test a fail.

> We are going to jump a little into pytest fixtures. With pytest fixtures.
> Pytest fixtures will initialize test functions and provide us a fixed baseline
> to allow us to produce consistant, repeatable results.

- Look at the next test in the series.
> We have a function that takes expects a parameter, which we name luke.
> Down in our fixtuer, we are creating an instance of JediMaster and passing 'Luke'
> as an argument.
> This will DRY up our code a little. I have a consistant JediMaster I can use. I'll use Luke
> for a few tests.

- Run the next test and we should already be passing.
- Look at the next test to see what it is requiring. Write up a quick method

```python
    def attacking(self) -> str:
        return 'Luke is Force attacking!'
```

> Bada Bing Badda Boom. Test passing.  Of course we don't want to hard code that.
> Our JM will not always be named Luke.

> QUESTION: What can we change to account for different names?
> ANSWER: Change the return to f'{self.name} is attacking!

```python
def attacking(self) -> str:
    return f'{self.name} is attacking!'
```
Once we run pytest with this, to verify everything is working, we go to the next test.

> QUESTION: Get a student to walk through adding the following:
```python
def getting_hit(self) -> str:
    return f'{self.name} is being attacked!'
```

> Now that is working and we look at the next test, and we need a new class SithLord.

```python
class SithLord(ForceUser):
    '''
    Sith Lord Class
    '''

    def __init__(self, name='Random Sith'):
        self.name = name
```

> We get the next 2 tests to pass, one passing in the name, the other with a fixture.
> The 2 tests after that are similar to the JEDI attacking and being attacked.
> Copy the 2 methods from JediMaster to Sith Lord and andter if necessary.
> Run tests, and yes, everything is running.  But this makes me SAAD.  

> QUESTION: What is our area of opportunity here?
> ANSWER: DRY out the code.

> If you know anything about Star Wars what do these 2 classes have in common? They are both 
> Force Users.

> I want to create a new class called ForceUser that will will allow the other to classes to 
> extend the ForceUser class and utelize methods in there. 

> Move the attacking and attacked to the ForceUser and run pytest.

QUESTION: How to I extend a super class in a sub class?
ANSWER: Add it into the parameter of the class.


```python
class JediMaster(ForceUser):
class SithLord(ForceUser):
```

> NOTE: This may bring up a question about multiple inheritance. 
> [MRO - Multipple REsolution Order](https://data-flair.training/blogs/python-multiple-inheritance/)

> This allows us to use the super class methods but we still have the ability to overrwrite the 
> method inside the subclass.

> add a different JediMaster Attacking

```python
def attacking(self) -> str:
    return f'{self.name} is attacking with the Good Force!'
```

> Write some tests to check for this.

> This just adressed methods.  There are ways that I could user the super().__init__() to 
> do an initializer in the super class and pass those attributes to the sub class.
> That I will leave the user of super().__init__() to you to look up.  Here is a good
> resource on that. [Super Class Demo](https://pybit.es/python-subclasses.html)

- Time to talk about Static Methods and Class Methods
- Add a static Method to each.

```python
@staticmethod
def get_code() -> str:
    return 'There is no emotion, there is PEACE.'
```

and

```python
@staticmethod
def get_code() -> str:
    return 'Peace is a lie, there is only PASSION'
```

> A static method is something we use when we don't expect the output / outcome to change.
> A class method or cariable is something that is not tied to any one instance but all of them.
> Looking at my last test I see that I want to track the number of JM and SL's, whould would 
> A total of ForceUsers.  Lets examine how to do this.

- Add this to each sub class

```python
count = 0
```

> QUESTION: Where does it make sense to add the counter to add to count?
> HINT: What runs ever time we create a new instance?
> ANSWER: In the __init__

- Then in the __init__ for each class add this:

```python
JediMaster.count += 1
SithLord.count += 1
```

- Will also need to add a class method to each subclass to 

```python
@classmethod
def get_count(cls) -> int:
    return cls.count
```

> Then I can then add this to the Force user

```python
@classmethod
def get_count(cls) -> int:
    return JediMaster.count + SithLord.count
```

> Running the last test is going to show something weird as we look at our actual 
> count vs expected count?

> QUESTION: Any ideas what happen here?
> ANSWER: Fixtures are tracking each creation because it is a class variable and not an instance.

- Uncomment the following:

```python
@pytest.fixture(autouse=True)
def counter_reset():
    JediMaster.count = 0
    SithLord.count = 0
```

- This will reset the count for us on each instance run.

- Time to run this as a script again and print a JM
-  Now we need to add a __str__ to show printing (USER FACING)

NOTE: Can do a division by 0 in the main gate but the module import will still work

- Bring up __REPR__ (TECHNICAL INFORMATION)
