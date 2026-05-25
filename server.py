from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download")
def download(url: str):
    with yt_dlp.YoutubeDL({'format': 'best'}) as ydl:
        info = ydl.extract_info(url, download=False)
        return {"download_url": info['url']}
