import unittest
from classes import Artist, Album, Song


class TestArtist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Test started')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Test finished')

    def test_add_song_works_correct(self):
        art1 = Artist("Mettalica", "USA")
        alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
        song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
        len_1 = len(alb1.songs)
        self.assertEqual(alb1.songs, [song1])
        song2 = Song('The End of the Line', 2008, 470, art1, alb1)
        len_2 = len(alb1.songs)
        self.assertEqual(len_1, len_2 - 1)
        song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
        len_3 = len(alb1.songs)
        self.assertEqual(len_2, len_3)
