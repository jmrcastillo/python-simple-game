

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses"""
    def __init__(self, message=''):
        super().__init__(message)
        self.padding = '~'*50 + '\n'
        self.error_message = "Unspecified Error"

        # Alternative approach is to subclass GameUnitError
        # self.error_dict = {
            # 000: "ERROR-000: Unspecified Error!",
            # 101: "ERROR-101: Health Meter Problem!",
            # 102: "ERROR-102: Attack issue! Ignored",
        # }
        # try:
            # self.error_message += self.error_dict[code]
        # except KeyError:
            # self.error_message += self.error_dict[000]
        # self.padding += '\n' + '~'*50


class HealthMeterException(GameUnitError):
    """Custom exception to report health meter proble"""

    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding +
                              "Error: Health Meter Problem" +
                              '\n' + self.padding)
