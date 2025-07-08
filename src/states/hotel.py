from dataclasses import dataclass
from src.states.hotel_contact_info import HotelContactInfo


@dataclass
class Hotel:
    hotel_id: int
    hotel_name: str
    hotel_description: str
    hotel_location: str
    hotel_sentiment: str
    hotel_contact_info: HotelContactInfo