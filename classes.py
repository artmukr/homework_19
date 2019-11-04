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

