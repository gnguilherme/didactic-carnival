from pydantic import BaseModel, Field


class Messages(BaseModel):
    message: list = Field(..., title="Message", description="Messages")


class Conversation(Messages):
    user_id: str = Field(
        ..., title="User ID", description="The user ID of the conversation"
    )


class ConversationResponse(Conversation):
    # Include ID in response schema
    id: str = Field(..., title="ID", description="The ID of the conversation")
