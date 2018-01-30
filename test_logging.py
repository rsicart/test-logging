import logging

# logger with no config (only warning)
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

print(logger.getEffectiveLevel())
logger.warning('logger: Watch out!')  # will print a message to the console
logger.info('logger: I told you so')  # will not print anything


# logger_1 with console handler
logger_1 = logging.getLogger('logger_1')
logger_1.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger_1.addHandler(ch)

print(logger_1.getEffectiveLevel())
logger_1.warning('logger_1: Watch out!')
logger_1.info('logger_1: I told you so')

# logger_2
# no handler, use root lastResort (overwritten)
logger_2 = logging.getLogger('logger_2')
logger_2.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logging.lastResort = ch

print(logger_2.getEffectiveLevel())
logger_2.warning('logger_2: Watch out!')
logger_2.info('logger_2: I told you so')


# logger_3: using basicConfig to initialise logging
logging.basicConfig(level=logging.INFO)
logger_3 = logging.getLogger('logger_3')

print(logger_3.getEffectiveLevel())
logger_3.warning('logger_3: Watch out!')
logger_3.info('logger_3: I told you so')
