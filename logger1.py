import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("DEBUG")
logging.info("INFO")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
