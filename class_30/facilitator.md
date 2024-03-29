# Hashtables

> Let's talk about Hashtables
> NOTE: Pin Reading and Blank WebPage for writing
> HashTables associate a Key: with a value
> QUESTION: What data structure have you used that associates a key with a value?
> ANSWER: Dictionary, JS Objects, even possible arrays / lists
> Turns out these dictionaries are not just handy, they are also VERY efficient.
> QUESTION: What is the BigO of a dictionary?
> ANSWER: o(1)
> Why is it this?  We know there is a list / array involved. This is more of a conceptual array.  Under the hood does a python dictionary literaly use an array? That is not really our business, that is an implementation detail. But it defiantely uses the notion of sequential memory. It may litteraly be an array. It reality, it dosn't matter to us. For the outside user we can get with efficiency a value using a key. We will assume the notion of an array

- Use invision of the appt.  Blue has someone Greed does not
- Talk about placing someone has to be determineistic.
- Checking commer will always be in the first appt.  Clarissa will always be another.
- 
- Draw out an array.  Give a key:value of spam:bacon. We want to get them into the array?  How could we add it in there?

> we could add it in as a tuple.  Not very efficient. (DRAW OUT)+
> Image the efficency needed using tubples?  Could we get o(1) efficiency?
> What would our efficnecy there (o(n))
> We definately know there is something better we can use.
> With HT we get an o(1)* lookup, insert and delete
> We get this because when something get inserted into the table
> it gets added at a certain spot.
> We do this based off of the key which will get hashed?
> What is this notion of hasing.
> [Hash Generator](https://www.md5hashgenerator.com/)
> This is an older hashing algo.  
> Show the reverse hash at
> [crack station](https://crackstation.net/)
> Lets talk about this a little more: We have this notion that a "hashed" key will placed into a specific place in an array.
> For placing something into an array what are some assumptions we need to make?
> Positive whole number and within the index of the array.
> Another think that we need to think a little more about is that our key
> needs to not only lock our value, but also be able to unlock it.
> If we had to define a good return from a hash function that obeys
> certain rules. What would that look like?
> Draw out a hashtable and simulate some hasing. Get to a collision
> This is where buckets come into play.  
> Instead of a key:value we have a bucket that lives at each index
> Draw out an example of many collisions. Then draw out a bigger HT
> Go through the explanation that if we adjust the size of the HT
> There could be some previous "room-mates" that are not going to be mates anymore.
> This is an overview of HT. Lets build out a little code.

## HashTable Code

```python
poetry init -n
touch hashtable.py
touch linked_list.py
touch test_hashtable.py
poetry add pytest
poetry shell
```

- Copy the LL implementation from demo.  No need to write this code out.
- Add a hashtable class and add items needed from implementation with pass

```python
class Hashtable:

    def __init_(self):
        pass

    def set(self):
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.
        pass

    def get(self):
        # Arguments: key
        # Returns: Value associated with that key in the table
        pass

    def has(self):
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.
        pass

    def keys(self):
        # Returns: Collection of keys
        pass
    def hash(self):
        # Arguments: key
        # Returns: Index in the collection for that key
        pass
```

This will give us the base outline.