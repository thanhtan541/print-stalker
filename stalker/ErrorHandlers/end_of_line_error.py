from .abstract_error_handler import AbstractErrorHandler


class EndOfLineError(AbstractErrorHandler):
    @AbstractErrorHandler.error_code.getter
    def error_code(self) -> int:
        return 1

    @AbstractErrorHandler.pattern.getter
    def pattern(self) -> str:
        return "^.*;"

    @AbstractErrorHandler.exception.getter
    def exception(self) -> str:
        return "^[If, For, While, }].*$"

    @AbstractErrorHandler.msg.getter
    def msg(self) -> str:
        return "Missing semi-colon ';' at the end of line"
