from abc import ABC, abstractstaticmethod
import re


class AbstractErrorHandler(ABC):
    @property
    def error_code(self) -> int:
        ...

    @property.getter
    def error_code(self) -> int:
        ...

    @property
    def pattern(self) -> str:
        ...

    @property.getter
    def pattern(self) -> str:
        ...

    @property
    def exception(self) -> str:
        ...

    @property.getter
    def exception(self) -> str:
        ...

    @property
    def msg(self) -> str:
        ...

    @property.getter
    def msg(self) -> str:
        ...

    def check(self, line: str) -> bool:
        exception = re.search(self.exception, line)
        if exception is not None:
            return False
        check = re.search(self.pattern, line)
        return False if check is None else True
