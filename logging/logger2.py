import logging

logging.basicConfig(level=logging.debug, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


x = 2

logging.debug(f"the value of x  is {x}")
