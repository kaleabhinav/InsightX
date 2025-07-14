# logger.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

# # Testing logger
# logger.info("InsightX Starting....")
# logger.debug("This is a DEBUG message (won't show unless level is DEBUG)")
# logger.info("This is an INFO message")
# logger.warning("This is a WARNING message")
# logger.error("This is an ERROR message")
# logger.critical("This is a CRITICAL message")