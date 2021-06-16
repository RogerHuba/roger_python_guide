import pytest
from challenges.eeney_meeney_miney_moe.eeney_meeney_miney_moe import (eeney_meeney_miney_moe as emmm,
                                                                      eeney_meeney_miney_moe_math as emmm_math)


class TestEMMM:

    def test_emmm_happy_path(self):
        names = ['A', 'B', 'C', 'D', 'E']
        k = 3
        assert emmm(names, k) == 'D'

    def test_emmm_math_happy_path(self):
        names = ['A', 'B', 'C', 'D', 'E']
        k = 3
        assert emmm(names, k) == 'D'
