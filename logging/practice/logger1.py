import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="r")
                   # format="%(asctime)s - %(levelname)s - %(message)s")

# when we use level(outputting or logging at) as INFO it means we use info n above skippin DEBUG only 
# to get to the filename/ filemode="w" : it create the the file every time we use or overwrtie everytime we use  
#



# these are the sequence ....
logging.debug("DEBUG")
logging.info("INFO")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
#