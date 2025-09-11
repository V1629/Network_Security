import sys
from network_security.logging import logger
# python -m network_security.exceptions.exception
class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        __,__,exc_tb = error_details.exc_info()


        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in script: {self.filename} at line number: {self.lineno} with error message: {self.error_message}"
    


if __name__ == "__main__":
    try:
        logger.logging.info("Logging has started")
        a = 1/0
        print("this will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)