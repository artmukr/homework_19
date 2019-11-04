import unittest
from classes import Artist, Album, Song


class TestArtist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Test started')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Test finished')

    def test_add_song_works_write(self):
        art1 = Artist("Mettalica", "USA")
        alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
        song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
        len_1 = len(art1.songs)
        self.assertEqual(art1.songs, [song1])
        song2 = Song('The End of the Line', 2008, 470, art1, alb1)
        len_2 = len(art1.songs)
        self.assertEqual(len_1, len_2 - 1)

    def test_add_album_works_write(self):
        art1 = Artist("Mettalica", "USA")
        alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
        len_1 = len(art1.albums)
        self.assertEqual(art1.albums, [alb1])
        alb2 = Album('St. Anger', 2003, 'Thrash metal', art1)
        len_2 = len(art1.albums)
        self.assertEqual(len_1, len_2 - 1)

    def test_song_number_works_correct(self):
        art1 = Artist("Mettalica", "USA")
        alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
        song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
        song2 = Song('The End of the Line', 2008, 470, art1, alb1)
        self.assertEqual(art1.songs_number, 2)

    def test_album_number_works_correct(self):
        art1 = Artist("Mettalica", "USA")
        alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
        alb2 = Album('St. Anger', 2003, 'Thrash metal', art1)
        self.assertEqual(art1.album_number, 2)

