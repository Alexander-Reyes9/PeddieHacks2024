import { useState } from 'react'
import spotifyLogo from './assets/spotify_logo.png'
import './App.css'

async function fetchApi() {
    const response = await fetch("get_playlist_emotion", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        //body: JSON.stringify({ playlistLink }),
    });
    const data = await response.json();
    return data.playlists;
}

function Playlist({ name, songList}: { name: string, songList: Array<string>}){
    return (
        <div className="bg-blue-900 rounded-lg p-5">
            <h2 className="text-lg font-extrabold underline">{name}</h2>
            <ul>
                {songList.map((song, index) => <li>{index+1}. {song}</li>)}
            </ul>
        </div>
    )
}



function App() {
    const [playlists, setPlaylists] = useState<any>(null)

    return (
        <div className="grid place-items-center">
            <img className="logo select-none" src={spotifyLogo}></img>
            <h1 className="text-5xl font-bold">Song Emotion Website</h1>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold p-4 m-5 rounded" onClick={async () => {
                setPlaylists(await fetchApi())
            }}>Generate emotion playlists</button>
            <div className="">
                <ul className="grid gap-4 grid-cols-4">
                    {playlists?.map((playlist: any) => { <Playlist name={playlist.name} songList={playlist.songList} /> })}
                    <Playlist name="Sad playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                    <Playlist name="Happy playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                    <Playlist name="IDK playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                    <Playlist name="IDK playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                    <Playlist name="IDK playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                    <Playlist name="IDK playlist" songList={['Test song 1', 'Test song 2', 'Test song 3']}/>
                </ul>
            </div>
        </div>
    )
}

export default App
