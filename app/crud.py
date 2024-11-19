import pymongo

from app.config import settings
from app.schemas import Conversation, ConversationResponse, Messages

client = pymongo.MongoClient(
    f"mongodb://{settings.USERNAME}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/"
)
db = client[settings.DB_NAME]
collection = db[settings.COLLECTION_NAME]


async def create_conversation(conversation: Conversation) -> ConversationResponse:
    """Create a new conversation.

    Args:
        conversation (Conversation): The conversation to create

    Returns:
        ConversationResponse: The created conversation
    """
    conversation_dict = conversation.model_dump()
    result = collection.insert_one(conversation_dict)
    return {**conversation_dict, "id": str(result.inserted_id)}


async def get_conversation(conversation_id: str) -> ConversationResponse | None:
    """Get a conversation by ID.

    Args:
        conversation_id (str): The ID of the conversation

    Returns:
        ConversationResponse | None: The conversation if found, else None
    """
    query = {"user_id": conversation_id}
    document = collection.find_one(query)
    if document:
        document["id"] = str(document["_id"])
        del document["_id"]
        return document
    return None


async def update_conversation(
    conversation_id: str,
    conversation: Messages,
) -> ConversationResponse | None:
    """Update a conversation by ID.

    Args:
        conversation_id (str): The ID of the conversation
        conversation (Messages): The conversation to update

    Returns:
        ConversationResponse | None: The updated conversation if found, else None
    """
    query = {"user_id": conversation_id}
    update = {"$set": {"message": conversation.message}}
    result = collection.update_one(query, update)

    if result.modified_count:
        return await get_conversation(conversation_id)
    return None
