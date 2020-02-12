import logging


class LoggingCustom:
    @staticmethod
    def log_info(level: str, line: int, msg: str):
        logging.info("[%s] Line %d: %s", level, line, msg)

    @staticmethod
    def log_alert(line: int, msg: str):
        level = "Alert"
        LoggingCustom.log_info(level=level, line=line, msg=msg)
