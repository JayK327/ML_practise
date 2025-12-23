from logger import logging
def add(a,b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

add(10,15)