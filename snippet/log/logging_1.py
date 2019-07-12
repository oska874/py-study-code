import logging
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger_son = logging.getLogger(__name__+".xxx")
logger_son.setLevel(logging.WARN)
hdr = logging.FileHandler("log.txt")
formatter = logging.Formatter('ezio: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
hdr.setFormatter(formatter)
logger_son.addHandler(hdr)

 
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')

logger_son.warning("hello son")

try:
    result = 10 / 0
except Exception:
    logger_son.error('Faild to get result', exc_info=True)
logger_son.info('Finished')