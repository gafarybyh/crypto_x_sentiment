import logging.config
import os
import logging
from .logging_config import logging_config
from dotenv import load_dotenv

# Load variabel from file .env
load_dotenv()
 
# Configure logger
def setup_logging():
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(logging_config["handlers"]["file"]["filename"])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.config.dictConfig(logging_config)

logger = logging.getLogger(__name__)

# X Account Environment Variables
USERNAME = os.getenv("USERNAME")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Cookies Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cookies_path_file = os.path.join(f"{BASE_DIR}", 'cookies.json')

