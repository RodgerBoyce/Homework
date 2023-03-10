import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guest1 = Guest("bob", "starman", 25.5)
        self.guest2 = Guest("steve", "starman", 47.5)
        self.guest3 = Guest("dave", "another one bites the dust", 20)



