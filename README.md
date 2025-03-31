# Tools in Data Science - Project 2

This project builds an API that answers questions from graded assignments using OpenAI's GPT.

## Features
- Accepts a question and optional file attachments.
- Processes files (e.g., CSV, ZIP) and extracts relevant information.
- Uses OpenAI to generate answers.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Add your OpenAI API key to `.env`.
4. Run the app: `uvicorn app.main:app --reload`.

## Deployment
Deploy the app to a platform like Vercel or Render.

## API Endpoint
POST `/api/`
- Form Data:
  - `question`: The question to answer.
  - `file`: Optional file attachment.