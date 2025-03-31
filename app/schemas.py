from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    file: Optional[str] = None  # Optional file path or content

class AnswerResponse(BaseModel):
    answer: str