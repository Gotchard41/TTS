
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class TTSRequest(BaseModel):
    text: str

@app.post("/tts")
async def convert_text_to_speech(req: TTSRequest):
    # Đây là phần mô phỏng, bạn có thể tích hợp Google Cloud TTS hoặc gTTS thật ở đây
    text = req.text
    print(f"Received text: {text}")
    
    # Giả lập kết quả trả về
    return JSONResponse(content={
        "result": "Tạo giọng nói thành công",
        "audio_url": "https://example.com/audio/output.mp3"
    })
