import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song1 = Song("another one bites the dust", "queen", 3.35)
        self.song2 = Song("beat it", "michael jackson", 4.19)
        self.song3 = Song("starman", "david bowie", 4.14)
        self.all_songs = [self.song1, self.song2, self.song3]

       
    # @unittest.skip
    def test_get_name_of_song(self):
        self.assertEqual("another one bites the dust", self.song1.title)
        self.assertEqual("beat it", self.song2.title)
        self.assertEqual("starman", self.song3.title)

    
    # @unittest.skip
    def test_get_artist_of_song(self):
        self.assertEqual("queen", self.song1.artist)
        self.assertEqual("michael jackson", self.song2.artist)
        self.assertEqual("david bowie", self.song3.artist)


    # @unittest.skip
    def test_get_duration_of_song(self):
        self.assertEqual(3.35, self.song1.duration)
        self.assertEqual(4.19, self.song2.duration)
        self.assertEqual(4.14, self.song3.duration)
    

    
