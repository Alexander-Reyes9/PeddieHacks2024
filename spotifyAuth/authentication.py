import spotipy
from spotipy.oauth2 import SpotifyOAuth
from emotext import output
from genius import getLyrics


with open('secrets.txt', 'r') as file:
    SPOTIPY_CLIENT_ID = file.readline()
    SPOTIPY_CLIENT_SECRET = file.readline()

SPOTIPY_CLIENT_ID = 'f6f49efa164b4b1a9e5018bf7274ac90'
SPOTIPY_CLIENT_SECRET = 'cddeff85c6d842b4b86c0aa0ede8ed63'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

#Scope of what we're reading
scope = 'playlist-read-private'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

#current user's playlists
playlists = sp.current_user_playlists()
#Our custom playlists
happy = []
sad = []
excited = []

# Loop through each playlist and get the track titles and artists
for playlist in playlists['items']:
    print(f"\nPlaylist: {playlist['name']}")
    
    # Get the tracks in the playlist
    results = sp.playlist_tracks(playlist['id'])
    for item in results['items']:
        track = item['track']
        # Formatting
        artists = ', '.join([artist['name'] for artist in track['artists']])
        
        currEmotion = output(getLyrics(artists, track['name']))
        #Organizing
        if currEmotion == 'Happy':
            happy.append(f"{track['name']} by {artists}")
        if currEmotion == 'Surprise':
            excited.append(f"{track['name']} by {artists}")
        if currEmotion == 'Sad' or currEmotion == 'Fear':
            excited.append(f"{track['name']} by {artists}")
#Testing
print(happy)
print(sad)
print(excited)        
