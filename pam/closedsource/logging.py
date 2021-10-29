import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter

# Create the logger and set it's logging level
logger = logging.getLogger("logstash")
logger.setLevel(logging.ERROR)        

# Create the handler
handler = AsynchronousLogstashHandler(
    host='logstash.foundation.cloudcix.com', 
    port=443, 
    ssl_enable=True, 
    ssl_verify=False,
    database_path='')
# Here you can specify additional formatting on your log record/message
formatter = LogstashFormatter()
handler.setFormatter(formatter)

# Assign handler to the logger
logger.addHandler(handler)

# Send log records to Logstash 
logger.error('python-logstash-async: test error message.')
logger.info('python-logstash-async: test info message.')
logger.warning('python-logstash-async: test warning message.')
logger.debug('python-logstash-async: test debug message.')