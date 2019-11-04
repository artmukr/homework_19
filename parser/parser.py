import json
import requests
from bs4 import BeautifulSoup


class AlbumsParser:
    def __init__(self, artist_name):
        self.artist = artist_name

    def to_json(self):
        with open(f'{self.artist}.json', "w") as file:
            file.write((json.dumps(self.fetch_albums(), indent=2)))

    def fetch_albums(self):
        albums = []
        page = self.get_albums_page()
        for link in self.fetch_albums_links(page):
            albums.append(self.fetch_album(self.get_album_page(link)))
        return albums

    def get_albums_page(self, page_number: int = 1):
        album_page = requests.get(
            f'https://www.last.fm/music/{self.artist}/'
            f'+albums?page={page_number}').text
        return album_page

    @staticmethod
    def get_album_page(link: str):
        return requests.get(link).text

    @staticmethod
    def fetch_albums_links(albums_page: str):
        soup = BeautifulSoup(albums_page, 'html.parser')
        section = soup.find('section', {'id': 'artist-albums-section'})
        for a in section.findAll('a', {'class': 'link-block-target'}):
            yield f"https://www.last.fm{a['href']}"

    @staticmethod
    def fetch_album(album_page: str) -> dict:
        soup = BeautifulSoup(album_page, 'html.parser')
        album_name = soup.find('h1').text
        year = soup.findAll('dd', {'class': 'catalogue-metadata-description'})[
            1].text
        year = int(year.split(' ')[-1])
        artist_name = soup.find('span', {'itemprop': 'name'}).text
        songs = []
        duration_sum = 0.0
        for tr in soup.find_all('tr', {'class': 'chartlist-row'}):
            duration_sum += convert_to_seconds(tr.find('td', {
                'class': 'chartlist-duration'}).text.replace('\n', '').strip())

            songs.append({
                'name': tr.find(
                    'td', {'class': 'chartlist-name'}
                ).text.replace('\n', '').strip(),
                'artist': artist_name,
                'duration': tr.find(
                    'td', {'class': 'chartlist-duration'}
                ).text.replace('\n', '').strip(),
                'year': year,
                'album': album_name
            }
            )
            return {
                'name': album_name,
                'year': year,
                'genre': None,
                'artist': album_name,
                'duration_sum': duration_sum,
                'songs': songs

            }


def convert_to_seconds(time: str):
    split_time = time.split(':')
    converted_time = round((int(split_time[0]) * 60
                            + int(split_time[1]) * 60/100), 1)
    return converted_time


parser = AlbumsParser('Nirvana')
parser.to_json()
