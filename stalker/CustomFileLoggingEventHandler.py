from pathlib import Path
from .Utils import *
from .ErrorHandlers import *

from watchdog.events import FileSystemEventHandler


def analyze_file(src_path):
    full_path = Path(src_path).absolute()
    with open(full_path) as read_file:
        lines = read_file.readlines()
        sub_class = AbstractErrorHandler.__subclasses__()
        for cls in sub_class:
            checker: AbstractErrorHandler = cls()
            checker.lines = lines
            checker.check()
            if len(checker.report) > 0:
                LoggingCustom.log_alert(
                    lines=checker.report,
                    msg=checker.msg
                )


class LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_created(self, event):
        super(LoggingEventHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        LoggingCustom.log_info(level="Start", line=0, msg="Initial")
        analyze_file(src_path=event.src_path)
        LoggingCustom.log_info(level="End", line=0, msg="Terminate")

    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
