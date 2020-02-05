'''

Created on Jul 24, 2013

@author: tuna

'''

# python logging example

import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='/tmp/test.log', level=logging.ERROR)
logging.debug('Debug log')
logging.info('Info log')
logging.warning('Warning log')
logging.error('Error log')
logging.critical('Critical log')
