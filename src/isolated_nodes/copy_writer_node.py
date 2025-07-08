import json

from src.states.hotel_research_state import HotelResearchState
from src.tools.google_drive import GoogleDrive


class CopyWriterNode:
    def __init__(self, google_drive: GoogleDrive):
        self.google_drive = google_drive

    def clean_and_parse_proposals(self, state):
        raw = state["proposals"]

        # Remove triple backticks if present
        if raw.startswith("```"):
            raw = raw.strip("` \n")

        # Optional: extract content between triple backticks (if markdown-styled)
        if raw.startswith("json"):
            raw = raw[len("json"):].strip()

        parsed = json.loads(raw)
        state["proposals"] = parsed

        return state

    def create_proposal_doc(self, state: HotelResearchState):
        #folder_id = self.google_drive.create_folder_if_not_exists("Hotel Proposals")

        state = self.clean_and_parse_proposals(state)
        proposals = state["proposals"]
        # If proposals_data is already a string, try to parse it first

        # Now, if proposals_data is a Python object, convert it to a JSON string
        for proposal in proposals:
            print(proposal)
            print("handling proposal {}".format(proposal["id"]))
            #self.google_drive.create_google_doc_in_folder(folder_id, f"{proposal.hotel_name}", str(proposal.email_proposal))

        return state #TODO Better exception handling

