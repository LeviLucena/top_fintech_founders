from pydantic import BaseModel

class FounderOut(BaseModel):
    name: str
    startup: str
    bio: str
    score: float
    country: str | None = None
