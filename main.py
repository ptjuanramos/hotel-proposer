from src.hotel_workflow import HotelWorkflow
from src.isolated_nodes.copy_writer_node import CopyWriterNode
from src.states.hotel_research_state import HotelResearchState
from src.tools.google_drive import GoogleDrive

if __name__ == "__main__":
    app = HotelWorkflow().app
    initial_state = {}
    app.invoke(initial_state)
    # gd = GoogleDrive()
    # hs = HotelResearchState()
    # CopyWriterNode(gd).create_proposal_doc(hs)
