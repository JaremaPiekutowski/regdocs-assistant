from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str
    top_k: int = Field(gt=1, lt=5, default=5)


class QuestionResponse(BaseModel):
    document_id: int
    question: str
    top_k: int
    debug: bool


@router.post("/documents/{document_id}/questions", response_model=QuestionResponse)
async def questions(
    document_id: int,
    request: QuestionRequest,
    debug: bool = False,
) -> QuestionResponse:

    response = QuestionResponse(
        document_id=document_id,
        question=request.question,
        top_k=request.top_k,
        debug=debug
    )

    return response
