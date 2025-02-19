from pydantic import BaseModel
from typing import Optional

class SimpleMessage(BaseModel):
    msg: str
    answer_language: Optional[str] = "english"