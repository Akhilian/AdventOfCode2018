from unittest import TestCase

from Day3.Claim import Claim
from Day3.Diplomat import Diplomat


class TestDiplomat(TestCase):
    def test_number_of_conflicts_when_zero_claims(self):
        diplomat = Diplomat([])
        assert diplomat.number_of_conflicts() == 0

    def test_number_of_conflicts_when_1_conflict(self):
        diplomat = Diplomat([
            Claim(123, 1, 1, 0, 0),
            Claim(456, 2, 2, 0, 0),
        ])
        assert diplomat.number_of_conflicts() == 1

    def test_number_of_conflicts_when_2_conflicts(self):
        diplomat = Diplomat([
            Claim(123, 2, 2, 0, 0),
            Claim(456, 2, 2, 1, 1),
            Claim(456, 1, 1, 0, 1),
        ])
        assert diplomat.number_of_conflicts() == 2
