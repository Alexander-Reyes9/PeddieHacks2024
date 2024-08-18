import { useState } from 'react'
import spotifyLogo from './assets/spotify_logo.png'
import './App.css'

async function fetchApi(playlistLink: string) {
    return playlistLink
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
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={async () => {
                let input = document.getElementById("playlistLink") as HTMLInputElement
                setEmotion(await fetchApi(input.value))
            }}>Get new playlist</button>
            <EmotionDisplay emotion={emotion} />
        </div>
    )
}

export default App
