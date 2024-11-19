from pydantic import BaseModel, Field


class ConversationCreate(BaseModel):
    user_id: str = Field(
        ..., title="User ID", description="The user ID of the conversation"
    )
    message: list[str] = Field(
        ..., title="Message", description="The messages of the conversation"
    )


class ConversationResponse(ConversationCreate):
    # Include ID in response schema
    id: str = Field(..., title="ID", description="The ID of the conversation")
