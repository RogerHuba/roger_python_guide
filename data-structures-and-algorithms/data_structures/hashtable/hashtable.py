from data_structures.linked_list.linked_list import LinkedList


class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * size

    def hash(self, key):
        hashed_key = sum(ord(char) for char in key) * ord(key[0])

        return hashed_key % self.size

    def add(self, key, value):
        hashed_key = self.hash(key)
        bucket = self.buckets[hashed_key]

        if self.buckets[hashed_key] is None:
            self.buckets[hashed_key] = LinkedList()

        self.buckets[hashed_key].append((key, value))
        return hashed_key

    def contains(self, key):
        hashed_key = self.hash(key)
        bucket = self.buckets[hashed_key]
        exist = False

        if bucket:
            curr = bucket.head
            while curr:
                if curr.val[0] == key:
                    exist = True
                curr = curr.next

        return exist

    def get(self, key):
        hashed_key = self.hash(key)
        bucket = self.buckets[hashed_key]
        value = None

        if bucket:
            curr = bucket.head
            while curr:
                if curr.val[0] == key:
                    value = curr.val[1]
                curr = curr.next

        return value
