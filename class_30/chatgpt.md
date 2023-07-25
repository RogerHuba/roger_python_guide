A hashtable, also known as a hash map, is a data structure that maps keys to values. It is a common way to implement a dictionary or an associative array. A hashtable uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. The hash function takes the key as input and produces a hash code, which is a fixed-size value that represents the key. The hash code is used to compute the index into the array.

Here's how you can implement a simple hashtable in Python:

```python
class HashTable:
    def __init__(self):
        self.size = 10
        self.hash_table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        A simple hash function that takes a string key and returns a hash code
        """
        hash_code = 0
        for i in range(len(key)):
            hash_code += ord(key[i])
        return hash_code % self.size

    def add(self, key, value):
        """
        Adds a key-value pair to the hashtable
        """
        hash_key = self._hash(key)
        bucket = self.hash_table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key):
        """
        Returns the value associated with the given key
        """
        hash_key = self._hash(key)
        bucket = self.hash_table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __str__(self):
        """
        Returns a string representation of the hashtable
        """
        return '{' + ', '.join([f'{k}: {v}' for bucket in self.hash_table for k, v in bucket]) + '}'
```
Let's go through each method in detail:

__init__(self) - This is the constructor method. It initializes the size of the hashtable to 10 and creates an empty array of that size to hold the key-value pairs. The _hash() method is called to compute the hash code for each key.

_hash(self, key) - This is the hash function. It takes a key as input and returns a hash code. In this implementation, we simply add up the ASCII values of all the characters in the key and take the remainder of that sum when divided by the size of the hashtable. This produces a number between 0 and self.size - 1, which is the index into the array of buckets.

add(self, key, value) - This method adds a key-value pair to the hashtable. It first computes the hash code for the key and finds the corresponding bucket in the array. It then checks if the key already exists in the bucket, and if it does, it updates the value. If not, it adds the key-value pair to the bucket.

get(self, key) - This method returns the value associated with the given key. It first computes the hash code for the key and finds the corresponding bucket in the array. It then checks each key-value pair in the bucket until it finds the one with the matching key. If it doesn't find a matching key, it raises a KeyError.

__str__(self) - This method returns a string representation of the hashtable. It iterates through each bucket in the array and concatenates the key-value pairs into a string.

```python
class HashTable:
```

This line defines a class called HashTable that will contain the implementation of the hashtable.

```python
    def __init__(self):
        self.size = 10
        self.hash_table = [[] for _ in range(self.size)]
```

The __init__ method is called when a new instance of the HashTable class is created. In this method, we set the size of the hashtable to 10 and create an array of that size, self.hash_table, with empty lists in each position. This array will hold the key-value pairs in the hashtable.

```python
    def _hash(self, key):
        """
        A simple hash function that takes a string key and returns a hash code
        """
        hash_code = 0
        for i in range(len(key)):
            hash_code += ord(key[i])
        return hash_code % self.size
```

This is a method that calculates the hash code for a given key string. It computes the hash code by adding up the ASCII values of all the characters in the string and then taking the remainder when divided by the size of the hashtable. The % operator is used to ensure that the resulting hash code is within the range of indices of the hashtable.

```python
    def add(self, key, value):
        """
        Adds a key-value pair to the hashtable
        """
        hash_key = self._hash(key)
        bucket = self.hash_table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
```

This method adds a key-value pair to the hashtable. It first calculates the hash code for the key using the _hash() method. It then finds the bucket in self.hash_table that corresponds to the hash code by indexing into the array. If the key already exists in the bucket, this method updates the corresponding value. Otherwise, it appends the new key-value pair to the bucket.

```python
    def get(self, key):
        """
        Returns the value associated with the given key
        """
        hash_key = self._hash(key)
        bucket = self.hash_table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
```

This method returns the value associated with the given key. It calculates the hash code for the key using the _hash() method and then finds the corresponding bucket in self.hash_table. It then iterates over the key-value pairs in the bucket and returns the value corresponding to the key if found. If the key is not found, it raises a KeyError.

```python
    def __str__(self):
        """
        Returns a string representation of the hashtable
        """
        return '{' + ', '.join([f'{k}: {v}' for bucket in self.hash_table for k, v in bucket]) + '}'
```
This method returns a string representation of the hashtable. It uses a list comprehension to create a list of strings in the format "key: value" for each key-value pair in each bucket of self.hash_table. It then joins these strings with ', ' as a separator and encloses them in curly braces to produce the final string representation of the hashtable.
