from typing import Dict, List
from pydantic import BaseModel

class Service(BaseModel):
    id: int
    name: str

class ServicesResponse(BaseModel):
    data: Dict[str, List[Service]]  # e.g., "Plumber" -> List[Service]