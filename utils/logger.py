import logging
import allure


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def allure_log(message):
    logger.info(message)
    allure.attach(message, name="Log", attachment_type=allure.attachment_type.TEXT)
