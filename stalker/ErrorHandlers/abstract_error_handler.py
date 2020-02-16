from abc import ABC
import re


class AbstractErrorHandler(ABC):
    def __init__(self):
        self.lines = None
        self.report = []

    @property
    def error_code(self) -> int:
        ...

    @error_code.getter
    def error_code(self) -> int:
        ...

    @property
    def pattern(self) -> str:
        ...

    @pattern.getter
    def pattern(self) -> str:
        ...

    @property
    def exception(self) -> str:
        ...

    @exception.getter
    def exception(self) -> str:
        ...

    @property
    def msg(self) -> str:
        ...

    @msg.getter
    def msg(self) -> str:
        ...

    def check(self) -> None:
        lines = self.lines
        line_number = 0
        for line in lines:
            line_number = line_number + 1
            if self.exception:
                exception = re.search(self.exception, line)
                if exception is not None:
                    continue
            check = re.search(self.pattern, line)
            if check is None:
                self.report.append(line_number)
