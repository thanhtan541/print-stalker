from .abstract_error_handler import AbstractErrorHandler


class WrongStaticCallError(AbstractErrorHandler):
    @AbstractErrorHandler.error_code.getter
    def error_code(self) -> int:
        return 2

    @AbstractErrorHandler.pattern.getter
    def pattern(self) -> str:
        return "^.*\\w::\\w\\.*$"

    @AbstractErrorHandler.exception.getter
    def exception(self) -> str:
        return ""

    @AbstractErrorHandler.msg.getter
    def msg(self) -> str:
        return "Missing double-colon for Static Call"
