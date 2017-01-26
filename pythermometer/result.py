class Result:
    '''A class representing a successful or failed operation'''
    
    def __init__(self, success, message, value):
        '''Initialize a successful or failed Result

        Args:
            success: A boolean. True if the result is success, false otherwise
            
            message: Optional. A message to return with a failed result.

            value: Optional. Data to be returned with a successful result.abs
        '''

        self._success = success
        self._message = message
        self._value = value

    def success(self):
        return self._success

    def message(self):
        return self._message

    def value(self):
        assert self._success
        return self._value

    @staticmethod
    def Success(value):
        return Result(True, '', value)

    @staticmethod
    def Fail(message):
        return Result(False,message)