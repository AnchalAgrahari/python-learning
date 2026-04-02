import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

logging.info(f"the value of x  is {x}")

# import logging

# logging.basicConfig(
#     level=logging.INFO,
#    # format="%(asctime)s - %(levelname)s - %(message)s"
# )
# # formant bacically modify the output
# logging.info("Application started")
# logging.error("Something failed")