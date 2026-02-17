# # myapp.py
# import logging
# import mylib
# logger = logging.getLogger(__name__)

# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logger.info('Started')
#     mylib.do_something()
#     logger.info('Finished')

# if __name__ == '__main__':
#     main()




import logging
import mylib

# Configure logging FIRST
logging.basicConfig(
    filename='myapp.log',
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
