from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
from SpellingCorrection.pipeline.prediction import PredictionPipeline
import uvicorn
import os
app = FastAPI()
templates = Jinja2Templates(directory="templates")

from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
from SpellingCorrection.pipeline.prediction import PredictionPipeline
import uvicorn
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/predict-text", response_class=HTMLResponse)
async def predict_text(request: Request, text: str = Form(...)):
    pipeline = PredictionPipeline()
    prediction = pipeline.predict(text)
    return templates.TemplateResponse("result.html", {"request": request, "input_text": text, "output_text": prediction})

@app.post("/upload-file", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    try:
        # Save the file to a temporary location
        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as f:
            f.write(await file.read())

        # Process the file and correct spelling errors
        pipeline = PredictionPipeline()
        corrected_text = pipeline.process_file(temp_file_path, file.content_type)

        # Return the corrected text
        return templates.TemplateResponse("result.html", {"request": request, "input_text": "Uploaded file content", "output_text": corrected_text})
    except Exception as e:
        return HTMLResponse(content=f"An error occurred: {str(e)}", status_code=500)

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)