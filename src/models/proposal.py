from pydantic import BaseModel, Field, EmailStr
from typing import List

class HotelEmailProposal(BaseModel):
    hotel_id: str = Field(description="Hotel list element ID")
    hotel_name: str = Field(description="Name of the hotel")
    hotel_email: EmailStr = Field(description="Hotel contact email address")
    email_proposal: str = Field(description="Personalized email proposal content")

# For the array structure
class HotelEmailProposalResponse(BaseModel):
    proposals: List[HotelEmailProposal] = Field(description="List of hotel email proposals")