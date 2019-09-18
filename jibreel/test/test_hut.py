

import unittest
from knight import Knight
from hut import Hut


class TestHut(unittest.TestCase):
    """Contains unit tests for the game attack of the orcs"""

    def setUp(self):
        """Called just before the calling each unittest"""
        self.knight = Knight()

    def test_acquire_hut(self):
        """Unittest to veryfy hut occupation after it is acquired"""
        print("\n Calling test_hut.test_acquire_hut..")
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)
