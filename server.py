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
    # הגדרות שגורמות ל-yt-dlp להזדהות כאפליקציית אנדרואיד
    ydl_opts = {
        'format': 'best',
        'extractor_args': {'youtube': {'player_client': ['android']}}
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {"download_url": info['url']}
    except Exception as e:
        return {"error": "שגיאת שרת: " + str(e)}
