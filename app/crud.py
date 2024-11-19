import pymongo

from app.config import settings
from app.schemas import ConversationCreate, ConversationResponse

client = pymongo.MongoClient(f"mongodb://{settings.HOST}:{settings.PORT}/")
db = client[settings.DB_NAME]
collection = db[settings.COLLECTION_NAME]


async def create_conversation(
    conversation: ConversationCreate,
) -> ConversationResponse:
    """Create a new conversation.

    Args:
        conversation (ConversationCreate): The conversation to create

    Returns:
        ConversationResponse: The created conversation
    """
    conversation_dict = conversation.dict()
    result = collection.insert_one(conversation_dict)
    return {**conversation_dict, "id": str(result.inserted_id)}


async def get_conversation(conversation_id: str) -> ConversationResponse | None:
    """Get a conversation by ID.

    Args:
        conversation_id (str): The ID of the conversation

    Returns:
        ConversationResponse | None: The conversation if found, else None
    """
    document = collection.find_one({"_id": pymongo.ObjectId(conversation_id)})
    if document:
        document["id"] = str(document["_id"])
        del document["_id"]
        return document
    return None
