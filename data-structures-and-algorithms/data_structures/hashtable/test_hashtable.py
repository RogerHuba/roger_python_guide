import pytest
from data_structures.hashtable.hashtable import HashTable


class TestHashTable:
    def test_proof_of_life(self):
        assert HashTable

    def test_hash_no_random(self):
        ht = HashTable()
        one = ht.hash('test_key')
        two = ht.hash('test_key')
        three = ht.hash('test_key')
        four = ht.hash('test_key')
        five = ht.hash('test_key')

        assert one == two == three == four == five

    def test_hashtable_size(self):
        ht = HashTable(100)
        assert ht.size == 100

    def test_hash_within_range(self):
        ht = HashTable(100)
        key = ht.hash('test_key')

        assert 0 <= key <= 100

    def test_add_pass(self):
        ht = HashTable()
        bucket_number = ht.add('test_key', 'test_value')

        value = ht.buckets[bucket_number].head.val[1]

        assert value == 'test_value'

    def test_add_collision(self):
        ht = HashTable()
        bucket_number_1 = ht.add('test_key', 'test_value')
        bucket_number_2 = ht.add('tset_key', 'tset_value')
        bucket_number_3 = ht.add('tste_key', 'tste_value')

        assert bucket_number_1 == bucket_number_2 == bucket_number_3
        assert ht.buckets[bucket_number_1].head.val[1] == 'test_value'
        assert ht.buckets[bucket_number_1].head.next.val[1] == 'tset_value'
        assert ht.buckets[bucket_number_1].head.next.next.val[1] == 'tste_value'

    def test_contains_true(self):
        ht = HashTable()
        ht.add('test_key', 'test_value')

        assert ht.contains('test_key') == True

    def test_contains_false(self):
        ht = HashTable()
        ht.add('test_key', 'test_value')

        assert ht.contains('not_test_key') == False

    def test_get_existing(self):
        ht = HashTable()
        ht.add('test_key', 'test_value')

        assert ht.get('test_key') == 'test_value'

    def test_get_with_collision(self):
        ht = HashTable()
        ht.add('test_key', 'test_value')
        ht.add('tset_key', 'tset_value')
        ht.add('tste_key', 'tste_value')

        assert ht.get('test_key') == 'test_value'

    def test_get_not_existing(self):
        ht = HashTable()

        assert ht.get('test_key') == None
