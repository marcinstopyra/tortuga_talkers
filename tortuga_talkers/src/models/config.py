from pydantic import BaseModel
from typing import Optional

class Config(BaseModel):
    test_config: Optional[str] =  None