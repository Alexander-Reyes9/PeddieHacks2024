from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from genius import *
app = Flask(__name__)

# Load client ID and secret from file
with open('secrets.txt', 'r') as fileReader:
    clientID = fileReader.readline().strip()
    clientSecret = fileReader.readline().strip()

# Spotify OAuth setup
sp_oauth = SpotifyOAuth(client_id=clientID,
                        client_secret=clientSecret,
                        redirect_uri="http://127.0.0.1:8888/callback",
                        scope="playlist-read-private")

@app.route('/')
def login():
    # Redirect user to Spotify's authorization page
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Get the access token from Spotify
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)  # Retrieve the token info

    if not token_info:
        return "Authorization failed."

    # Use the token to access Spotify data
    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Get the current user information
    current_user = sp.current_user()
    playlists = sp.current_user_playlists()

    # Iterate through songs and display them
    iterate_songs(sp, playlists)

    return "Check your console for playlist details."

def iterate_songs(sp, playlists):
    for playlist in playlists['items']:
        playlist_name = playlist['name']
        playlist_id = playlist['id']

        print(f"Playlist: {playlist_name}")
        
        # Get all tracks in the playlist
        tracks = sp.playlist_tracks(playlist_id)
        
        for track in tracks['items']:
            track_info = track['track']
            song_name = track_info['name']
            artist_names = ', '.join([artist['name'] for artist in track_info['artists']])
            album_name = track_info['album']['name']
            
            print(f"Song: {song_name} - Artists: {artist_names} - Album: {album_name}")
        
        # Handle pagination for playlists with more than 100 tracks
        while tracks['next']:
            tracks = sp.next(tracks)
            for track in tracks['items']:
                track_info = track['track']
                song_name = track_info['name']
                artist_names = ', '.join([artist['name'] for artist in track_info['artists']])
                album_name = track_info['album']['name']
                
                print(f"Song: {song_name} - Artists: {artist_names} - Album: {album_name}")
                getLyrics(artist_names, song_name)


if __name__ == '__main__':
    app.run(port=8888, debug=True)
