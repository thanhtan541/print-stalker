import re
from .abstract_error_handler import AbstractErrorHandler


class EndOfLineError(AbstractErrorHandler):
    @AbstractErrorHandler.error_code.getter
    def error_code(self) -> int:
        return 1

    def condition(self) -> bool:
        return "";

    def msg(self) -> str:
        pass

    def exception(self) -> bool:
        pass
