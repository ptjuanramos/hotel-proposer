from typing import List, TypedDict, NotRequired, Optional, Dict, Any

from src.models.workflow_step import WorkflowStep
from src.states.hotel import Hotel

class HotelResearchState(TypedDict):
    hotels: Optional[List[Hotel]]
    validations: Optional[Dict[str, str]]
    marketing_insights: Optional[Dict[str, str]]
    proposals: Optional[Dict[str, str]]

    # hotel_list: NotRequired[List[Hotel]]
    # quality_score: NotRequired[int]
    # research_data: Optional[Dict[str, Any]]
    #
    # #debugging properties
    # current_step: WorkflowStep
    # retry_count: NotRequired[int]
    # errors: NotRequired[list[str]]
    #
    # # Metadata
    # created_at: str
    # updated_at: str