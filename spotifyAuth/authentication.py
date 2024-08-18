import spotipy
from spotipy.oauth2 import SpotifyOAuth
fileReader = open('secrets.txt', 'r')
clientID = fileReader.readline()
clientSecret = fileReader.readline()
# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= clientID,
                                               client_secret= clientSecret,
                                               redirect_uri="http://127.0.0.1:8888/callback",
                                               scope="playlist-read-private"))

# Get current user's playlists
playlists = sp.current_user_playlists()

# Print playlist names
for playlist in playlists['items']:
    print(playlist['name'])