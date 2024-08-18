import spotipy
from spotipy.oauth2 import SpotifyOAuth
from emotext import output
from genius import getLyrics
# Set up your Spotify API credentials
SPOTIPY_CLIENT_ID = 'f6f49efa164b4b1a9e5018bf7274ac90'
SPOTIPY_CLIENT_SECRET = 'cddeff85c6d842b4b86c0aa0ede8ed63'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Set up the scope for accessing playlists
scope = 'playlist-read-private'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Get current user's playlists
playlists = sp.current_user_playlists()
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
        # Get all artist names as a string
        artists = ', '.join([artist['name'] for artist in track['artists']])
        # print(f" - {track['name']} by {artists}")
        # print("artists: " + artists)
        # print("name: " + track['name'])
        currEmotion = output(getLyrics(artists, track['name']))
        if currEmotion == 'Happy':
            happy.append(f"{track['name']} by {artists}")
        if currEmotion == 'Surprise':
            excited.append(f"{track['name']} by {artists}")
        if currEmotion == 'Sad' or currEmotion == 'Fear':
            excited.append(f"{track['name']} by {artists}")
print(happy)
print(sad)
print(excited)        
