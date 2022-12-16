import logging
from colorlog import ColoredFormatter
from logging import handlers


process_log = logging.getLogger(__name__)
process_log.setLevel(logging.INFO)

LOG_FORMAT = '%(log_color)s[%(asctime)s][%(levelname)s][File:%(module)s][Function:%(funcName)s][Line:%(lineno)s]' \
             '[%(message)s]'

colored_formatter = ColoredFormatter(LOG_FORMAT)

""" File logging """
r_handler = handlers.TimedRotatingFileHandler(filename='logs/logger.log', when="midnight", backupCount=0)
r_handler.setLevel(logging.INFO)
r_handler.setFormatter(colored_formatter)
process_log.addHandler(r_handler)

""" Stream logging """
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.INFO)
s_handler.setFormatter(colored_formatter)
process_log.addHandler(s_handler)
