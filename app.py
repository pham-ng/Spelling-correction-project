from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from SpellingCorrection.pipeline.prediction import PredictionPipeline

text: str ="Viet Namese Spelling Correction"
app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training completed successfully")
    except Exception as e:
        return Response(f"An error occurred: {str(e)}")
    
@app.get("/predict") 
async def predict_route(text):
    try:
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(text)
        return {"prediction": prediction}
    except Exception as e:
        return Response(f"An error occurred: {str(e)}")   
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)    

