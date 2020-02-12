from abc import ABC, abstractmethod


class AbstractErrorHandler(ABC):
    @property
    def error_code(self) -> int:
        ...

    @property.getter
    def error_code(self) -> int:
        ...

    @abstractmethod
    def condition(self) -> bool:
        pass

    @abstractmethod
    def msg(self) -> str:
        pass

    @abstractmethod
    def exception(self) -> bool:
        pass
