from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import os
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Ensure the uploads directory exists
os.makedirs("./uploads", exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_path = f"./uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Process the file (e.g., extract CSV data)
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            file_content = df.to_string()  # Convert DataFrame to string
        elif file_path.endswith(".zip"):
            file_content = "ZIP file detected. Unzipping not implemented yet."
        else:
            file_content = "Unsupported file type."
        
        return JSONResponse(content={"filename": file.filename, "content": file_content})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Serve the frontend HTML file
    with open("app/static/index.html", "r") as f:
        return HTMLResponse(content=f.read())