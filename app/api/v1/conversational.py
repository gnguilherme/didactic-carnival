from fastapi import APIRouter, HTTPException

from app.crud import create_conversation, get_conversation
from app.schemas import ConversationCreate, ConversationResponse

router = APIRouter()


@router.post("/conversations/", response_model=ConversationResponse)
async def create_new_conversation(conversation: ConversationCreate):
    return await create_conversation(conversation)


@router.get("/conversations/{conversation_id}", response_model=ConversationResponse)
async def get_conversation_by_id(conversation_id: str):
    conversation = await get_conversation(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation
