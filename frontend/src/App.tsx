import { useState } from 'react'
import spotifyLogo from './assets/spotify_logo.png'
import './App.css'

async function fetchApi(playlistLink: string) {
    const response = await fetch("get_playlist_emotion", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ playlistLink }),
    });
    const data = await response.json();
    return data.emotion;
}

function EmotionDisplay({ emotion }: { emotion: string | null }){
    if (!emotion){
        return (
            null
        )
    }else{
        return (
            <h2>{emotion}</h2>
        )
    }
}

function App() {
    const [emotion, setEmotion] = useState<string | null>(null)

    return (
        <div className="grid place-items-center">
            <img className="logo select-none" src={spotifyLogo}></img>
            <h1>Song Emotion Website</h1>
            <input type="text" id="playlistLink" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 m-5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Playlist link" />
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={async () => {
                let input = document.getElementById("playlistLink") as HTMLInputElement
                setEmotion(await fetchApi(input.value))
            }}>Get new playlist</button>
            <EmotionDisplay emotion={emotion} />
        </div>
    )
}

export default App
