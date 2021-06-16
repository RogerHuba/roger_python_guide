import pytest

from .left_join import join


class TestLeftJoin:
    def test_proof_of_life(self):
        assert join

    @pytest.fixture
    def ht_1(self):
        ht_1 = {
            'test_1': 'synonym test_1',
            'test_2': 'synonym test_2',
            'test_3': 'synonym test_3',
            'test_4': 'synonym test_4',
            'test_5': 'synonym test_5',
            'test_6': 'synonym test_6',
        }
        return ht_1

    @pytest.fixture
    def ht_2(self):
        ht_2 = {
            'test_2': 'antonym test_2',
            'test_3': 'antonym test_3',
            'test_6': 'antonym test_6',
            'test_7': 'antonym test_7',
            'test_8': 'antonym test_8',
            'test_9': 'antonym test_9',
        }
        return ht_2

    def test_left_join_pass(self, ht_1, ht_2):
        expected = {
            'test_1': ('synonym test_1', None),
            'test_2': ('synonym test_2', 'antonym test_2'),
            'test_3': ('synonym test_3', 'antonym test_3'),
            'test_4': ('synonym test_4', None),
            'test_5': ('synonym test_5', None),
            'test_6': ('synonym test_6', 'antonym test_6'),
        }

        assert join(ht_1, ht_2) == expected

    def test_left_join_no_matches(self, ht_1):
        ht_2 = {
            'test_7': 'antonym test_7',
            'test_8': 'antonym test_8',
            'test_9': 'antonym test_9',
        }

        expected = {
            'test_1': ('synonym test_1', None),
            'test_2': ('synonym test_2', None),
            'test_3': ('synonym test_3', None),
            'test_4': ('synonym test_4', None),
            'test_5': ('synonym test_5', None),
            'test_6': ('synonym test_6', None),
        }

        assert join(ht_1, ht_2) == expected

    def test_left_join_empty_ht(self):
        ht_1 = ht_2 = {}
        assert join(ht_1, ht_2) == {}

    def test_right_join(self, ht_1, ht_2):
        expected = {
            'test_2': ('antonym test_2', 'synonym test_2'),
            'test_3': ('antonym test_3', 'synonym test_3'),
            'test_6': ('antonym test_6', 'synonym test_6'),
            'test_7': ('antonym test_7', None),
            'test_8': ('antonym test_8', None),
            'test_9': ('antonym test_9', None),
        }

        assert join(ht_1, ht_2, 'right') == expected
