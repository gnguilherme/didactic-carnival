from pydantic import BaseModel, Field


class ConversationModel(BaseModel):
    user_id: str = Field(
        ..., title="User ID", description="The user ID of the conversation"
    )
    message: list[str] = Field(
        ..., title="Message", description="The messages of the conversation"
    )
