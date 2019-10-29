import logging
from pathlib import Path

from watchdog.events import FileSystemEventHandler


class LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_created(self, event):
        super(LoggingEventHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        total_lines = self.analyze_file(src_path=event.src_path)
        logging.info("Created : %s", event.src_path)

    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)
        logging.info("===" * 7 + "End" + "===" * 7)

    def analyze_file(self, src_path):
        full_path = Path(src_path).absolute()
        with open(full_path) as read_file:
            lines = read_file.readlines()
            line_number = 0
            for line in lines:
                line_number  = line_number + 1
                if len(line) > 1:
                    trailing_char = line[-2]
                    if not trailing_char == ";":
                        logging.info("Line %d: %s", line_number, "missing trailing char \";\" at the end")
                
                check_static_call = line.find(":")
                print(check_static_call)
                print(line[check_static_call + 1])
                if check_static_call > -1 
                    and check_static_call != line[check_static_call + 1]:
                    logging.info("Line %d: %s", line_number, "missing colon char \":\" for static call")
        return lines

