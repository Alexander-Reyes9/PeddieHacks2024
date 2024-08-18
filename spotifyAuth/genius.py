import requests
from bs4 import BeautifulSoup
text = "https://genius.com/"
# "https://genius.com/Kendrick-lamar-not-like-us-lyrics"
# Format of the song
def generate_genius_url(artist: str, song_name: str) -> str:
    # Convert artist name and song name to lowercase and replace spaces with hyphens
    artist_slug = artist.lower().replace(' ', '-')
    song_slug = song_name.lower().replace(' ', '-')
    
    # Construct the URL
    url = f"https://genius.com/{artist_slug}-{song_slug}-lyrics"
    
    return url
def getLyrics (artist, name):
    text = generate_genius_url(artist, name)
    html = requests.get(text).text

    soup = BeautifulSoup(html, "html.parser")

    lyrics_containers = soup.find_all(class_="ReferentFragmentdesktop__Highlight-sc-110r0d9-1")

    lyrics = []

    for element in lyrics_containers:
        split_text = element.decode_contents().split("<br/>")
        lyrics += split_text

    print("\n".join(lyrics))