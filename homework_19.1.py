
#   Also, you need implement a custom exception WrongArtistError which is
#   raised when you try to add a song to an album and artists don't match.


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
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


class Album:
    def __init__(self, name, year, genre, artist: Artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        artist.add_album(self)

    def add_song(self, song):
        if song in self.songs or song.artist != self.artist:
            raise WrongArtistError('This song has another artist')
        return self.songs.append(song)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        duration = 0
        for song in self.songs:
            duration += song.duration
        return duration


class Song:
    def __init__(self, name, year, duration, artist, album=None,):
        self.name = name
        self.year = year
        self.artist = artist
        self.duration = duration
        self.album = album
        self.author = []
        self.author.append(artist)
        artist.add_song(self)
        if album is not None:
            album.add_song(self)

    def add_artist(self, artist):
        if artist not in self.author:
            return self.author.append(artist)


art1 = Artist("Mettalica", "USA")
alb1 = Album('Death magnetic', 2008, 'Thrash metal', art1)
song1 = Song('That Was Just Your Life', 2008, 7.1, art1, alb1)
song2 = Song('The End of the Line', 2008, 7.86,  art1, alb1)
alb2 = Album('St. Anger', 2003, 'Thrash metal', art1)
song3 = Song('Frantic', 2003, 5.8,  art1, alb2)
art2 = Artist('Motorhead', "USA")
song4 = Song('Enter Sandman', 1991, 5.5, art1)
song4.add_artist(art2)
alb3 = Album("Motorhead", 1977, "Hard Rock", art2)
song5 = Song("Motorhead", 1977, 3.2, art2, alb1)

print(art1.songs_number, alb1.duration,
      alb1.songs_number, art1.album_number,
      song4.author, art2.album_number)


