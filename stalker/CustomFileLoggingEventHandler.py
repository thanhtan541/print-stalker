from pathlib import Path
from .Utils import *

from watchdog.events import FileSystemEventHandler


def analyze_file(src_path):
    full_path = Path(src_path).absolute()
    with open(full_path) as read_file:
        lines = read_file.readlines()
        line_number = 0
        for line in lines:
            line_number = line_number + 1
            if len(line) > 1:
                trailing_char = line[-2]

            check_static_call = line.find(":")
    return lines


class LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_created(self, event):
        super(LoggingEventHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        total_lines = analyze_file(src_path=event.src_path)
        LoggingCustom.log_alert(line=123, msg="ABC")
        logging.info("Created : %s", event.src_path)

    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
