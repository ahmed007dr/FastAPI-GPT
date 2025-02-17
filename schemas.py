from pydantic import BaseModel
from typing import List , Dict


# Making sure the data coming from the front end is validated
"""
I always insist on using schemas to have full control of the data flow from fe -> be.
"""

class TranslationRequest(BaseModel):
    text: str
    languages: str

class TaskResponse(BaseModel):
    task_id: int

class TranslationStatus(BaseModel):
    task_id: int
    status: str
    translations: Dict[str, str]
