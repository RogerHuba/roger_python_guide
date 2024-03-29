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
        # TODO: Hash they key value and set to variable
        hashed_key_index = self._hash(key) # silent same as listen => 167

        # TODO: Check if the bucket is empty
        # TODO: If it is empty, create an instance of a linked_list
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        # TODO: If not empty add the key, value to linked_list
        self._buckets[hashed_key_index].add((key, value)) # what about listen vs silent?

    def get(self, requesting_key):
        # TODO: Hash they key value and set to variable
        hashed_key_index = self._hash(requesting_key) # silent same as listen => 167
        # TODO: Assign the index bucket based off hashed value
        bucket = self._buckets[hashed_key_index]

        # TODO: Start iterating through the linked list and check the value(may need to unpack)
        # TODO: Set current, unpack current key:value, check if = key, advance current
        current = bucket.head

        while current:

            pair = current.data # (key, value)
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == requesting_key:
                return stored_value


            current = current.next