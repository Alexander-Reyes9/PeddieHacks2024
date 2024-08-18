from flask import Flask, request, redirect, send_file
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json
load_dotenv()

app = Flask(__name__, static_folder="../frontend/dist/assets")

# Spotify OAuth setup
sp_oauth = SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
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
    sp = spotipy.Spotify(auth=token_info["access_token"], )

    return send_file("../frontend/dist/index.html")

@app.route("/get_playlist_emotion", methods=["POST"])
def get_playlist_emotion():
    code = request.referrer.split("code=")[1]
    token_info = sp_oauth.get_access_token(code)
    sp = spotipy.Spotify(auth=token_info["access_token"])
    playlists = sp.current_user_playlists()

    print(token_info)
    songs = iterate_songs(sp, playlists)
    print(len(songs))
    return json.dumps({
        "emotion": songs
    })

def iterate_songs(sp, playlists):
    all_tracks = []
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
            
            #print(f"Song: {song_name} - Artists: {artist_names} - Album: {album_name}")
            all_tracks.append(song_name)
        
        # Handle pagination for playlists with more than 100 tracks
        while tracks['next']:
            tracks = sp.next(tracks)
            for track in tracks['items']:
                track_info = track['track']
                song_name = track_info['name']
                artist_names = ', '.join([artist['name'] for artist in track_info['artists']])
                album_name = track_info['album']['name']
                
                #print(f"Song: {song_name} - Artists: {artist_names} - Album: {album_name}")
                all_tracks.append(song_name)

    return all_tracks
if __name__ == '__main__':
    app.run(port=8888, debug=True)
