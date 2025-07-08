import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Workflow settings
    MAX_RETRIES = 3
    VALIDATION_THRESHOLD = 7.0

    # Logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "logs/hotel_outreach.log"