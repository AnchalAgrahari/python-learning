import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1/0
except ZeroDivisionError as e :
    # logging.error("ZeroDevisionError",exc_info=True)
    # OR
    logging.exception("DevisionError")