import os
import pandas as pd
import openai
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def process_file(file_path: str) -> str:
    """
    Process the uploaded file (e.g., extract data from CSV).
    """
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df.to_string()  # Convert DataFrame to string
        elif file_path.endswith(".zip"):
            return "ZIP file detected. Unzipping not implemented yet."
        else:
            return "Unsupported file type."
    except Exception as e:
        return f"Error processing file: {str(e)}"


def ask_openai(prompt: str) -> str:
    """
    Send a prompt to OpenAI and return the response.
    """
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use gpt-4o for advanced reasoning
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        raise ValueError(f"OpenAI API error: {str(e)}")


def ask_puter(prompt: str) -> str:
    """
    Send a prompt to Puter.js and return the response.
    Supports streaming if the API allows it.
    """
    try:
        response = requests.post(
            "https://api.puter.com/v2/chat",
            json={
                "prompt": prompt,
                "model": "o3-mini",  # Updated to match the JavaScript example
                "stream": True       # Enable streaming if supported
            },
            stream=True  # Use streaming response
        )
        if response.status_code != 200:
            raise ValueError(f"Puter.js API error: {response.text}")
        
        # Collect streamed response
        result = ""
        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
            result += chunk
        
        return result.strip()
    except Exception as e:
        raise ValueError(f"Puter.js API error: {str(e)}")