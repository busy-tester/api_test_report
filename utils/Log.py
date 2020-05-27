import logging
import logging.config
from config.config_global import *



logging.config.fileConfig(current_path+"//config//Logger.conf")


logger=logging.getLogger('example02')


def debug(message):

    logging.debug(message)

def warning(message):

    logging.warning(message)

def info(message):

    logging.info(message)
