import logging
import logstash


logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('34.235.152.184', 5959, version=1))

def check_multiple(x, y):
    
    if y == 0:
        logger.error('Division by 0 is not allowed')
    elif x % y == 0:
        message = 'Yes, {} is a multiple of {}'.format(x,y)
        logger.info(message)
    else:
        message = 'No, {} is not a multiple of {}'.format(x,y)
        logger.warning(message)
        
    

check_multiple(1, 2)
check_multiple(2, 3)
check_multiple(3, 4)
check_multiple(0, 4)
check_multiple(6, 2)
check_multiple(9, 3)
check_multiple(12, 4)
check_multiple(12, 0)

