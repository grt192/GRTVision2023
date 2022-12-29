import logging


logger = logging.getLogger('grt_vision')
logger.setLevel(logging.DEBUG)

# Log INFO and above to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Log everything to file
fh = logging.FileHandler('vision.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s - %(module)s %(levelname)s]: %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)
