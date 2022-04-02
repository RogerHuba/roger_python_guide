from linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def _hash(self, key):

        sum = 0
        for ch in key:
            sum += ord(ch)
        primed = sum * 19
        index = primed % self._size
        return index


    def set(self, key, value):
        pass
        # TODO: Hash they key value and set to variable
        # TODO: Check if the bucket is empty
        # TODO: If it is empty, create an instance of a linked_list
        # TODO: If not empty add the key, value to linked_list
      
    def get(self, requesting_key):
        pass
        # TODO: Hash they key value and set to variable
        # TODO: Assign the index bucket based off hashed value

        # TODO: Start iterating through the linked list and check the value(may need to unpack)
        # TODO: Set current, unpack current key:value, check if = key, advance current
