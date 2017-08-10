class ExceptionResponse(Exception):

    def __init__(self, status:int, msg:str):
        self.http_status = status
        self.err_msg = msg

    def __str__(self):
        return repr(self.err_msg)