import logging
from pathlib import Path

from watchdog.events import FileSystemEventHandler


class LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_moved(self, event):
        super(LoggingEventHandler, self).on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Moved %s: from %s to %s", what, event.src_path,
                     event.dest_path)

    def on_created(self, event):
        super(LoggingEventHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        total_lines = self.analyze_file(src_path=event.src_path)
        logging.info("Created : %s", event.src_path)

    def on_deleted(self, event):
        super(LoggingEventHandler, self).on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)

    def analyze_file(self, src_path):
        full_path = Path(src_path).absolute()
        with open(full_path) as read_file:
            lines = read_file.readlines()
            line_number = 0
            for line in lines:
                line_number  = line_number + 1
                trailing_char = line[-2]
                print(line.count())
                if not trailing_char == ";":
                    logging.info("Line %d: %s", line_number, "missing trailing char \";\" at the end")
        return lines

