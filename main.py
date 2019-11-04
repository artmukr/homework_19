import datetime
from functools import reduce
from typing import List


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

    def add_song(self, song):
        if song not in self.songs:
            return self.songs.append(song)

    def add_album(self, album):
        if album not in self.albums:
            return self.albums.append(album)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def album_number(self):
        return len(self.albums)

    def __repr__(self):
        return self.name


class Album:
    def __init__(self, name: str, year: int, genre: str, artist: Artist):

        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        artist.add_album(self)

    def __repr__(self):
        return f'{self.name} by {self.artist.name}'

    def add_song(self, song):
        if song in self.songs or song.artist != self.artist:
            raise WrongArtistError('This song has another artist')
        return self.songs.append(song)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return reduce(lambda x, y: x.duration + y.duration, self.songs)

    # @property
    # def duration(self):
    #     return datetime.timedelta(
    #         seconds = sum(song.duration.seconds for song in self.songs)
    #     )


class Song:
    def __init__(self, name: str, year: int, duration: int, artist: Artist,
                 album: Album = None, features: List[Artist] = None):

        self.name = name
        self.year = year
        self.artist = artist
        self.duration = datetime.timedelta(seconds=duration)
        self.album = album
        self.features = features or []
        self.features.append(artist)
        artist.add_song(self)
        if self.album:
            if self.album.artist != artist:
                raise WrongArtistError(f'{album.artist} is not {artist}')
            self.album.songs.append(self)

    def add_artist(self, artist):
        if artist not in self.features:
            return self.features.append(artist)


art1 = Artist("Mettalica", "USA")
alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
song1 = Song('That Was Just Your Life', 2008, 426, art1, alb1)
song2 = Song('The End of the Line', 2008, 470,  art1, alb1)
alb2 = Album('St. Anger', 2003, 'Thrash metal', art1)
song3 = Song('Frantic', 2003, 348,  art1, alb2)
art2 = Artist('Motorhead', "USA")
song4 = Song('Enter Sandman', 1991, 330, art1)
song4.add_artist(art2)
# alb3 = Album("Motorhead", 1977, "Hard Rock", art2)
# song5 = Song("Motorhead", 1977, 192, art2, alb1)

print(art1.songs_number, alb1.duration,
      alb1.songs_number, art1.album_number,
      song4.features, art2.album_number)


