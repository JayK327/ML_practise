import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),logging.StreamHandler()
    ]
)

logger=logging.getLogger('appLogger')

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} and {b} and returning the result:{result}")

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} by {b} and returning the result:{result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None
    
add(5,3)
divide(66,3)
divide(2,0)