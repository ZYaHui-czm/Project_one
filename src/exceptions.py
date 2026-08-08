#Api异常类
class ApiError(Exception):
    def __init__(self, status_code, message=""):
        self.status_code = status_code
        self.message = message
        super().__init__(f'ApiError:[{status_code}:{message}]')