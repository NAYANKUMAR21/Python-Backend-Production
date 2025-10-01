import logging
import sys
from app.config import settings

def setup_logging():
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
