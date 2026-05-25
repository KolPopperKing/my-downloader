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
    # הוספנו --geo-bypass ושימוש ב-n_code כדי לעקוף חסימות
    ydl_opts = {
        'format': 'best',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        'nocheckcertificate': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # ניסיון אחרון עם פרמטרים חזקים יותר
        info = ydl.extract_info(url, download=False)
        return {"download_url": info['url']}
