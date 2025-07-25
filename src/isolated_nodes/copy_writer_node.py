import json
import re

from src.states.hotel_research_state import HotelResearchState
from src.tools.google_drive import GoogleDrive


class CopyWriterNode:
    def __init__(self, google_drive: GoogleDrive):
        self.google_drive = google_drive

    def escape_newlines_in_json_strings(self, json_str):
        string_regex = r'"((?:[^"\\]|\\.)*)"'

        def replacer(match):
            s = match.group(1)
            escaped = s.replace('\n', '\\n').replace('\r', '\\r')
            return f'"{escaped}"'

        return re.sub(string_regex, replacer, json_str)

    def create_proposal_doc(self, state: HotelResearchState):
        folder_id = self.google_drive.create_folder_if_not_exists("Hotel Proposals")

        parsed = self.escape_newlines_in_json_strings(state["proposals"])
        proposals = json.loads(parsed)

        print(f"Loaded {len(proposals)} proposals")
        print(proposals[0])

        for proposal in proposals:
            print("handling proposal {}".format(proposal["hotel_name"]))
            self.google_drive.create_google_doc_in_folder(folder_id, f"{proposal['hotel_name']}", str(proposal['email_proposal']))

        return state #TODO Better exception handling

