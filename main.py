from src.hotel_workflow import HotelWorkflow

if __name__ == "__main__":
    app = HotelWorkflow().app
    initial_state = {}
    app.invoke(initial_state)
