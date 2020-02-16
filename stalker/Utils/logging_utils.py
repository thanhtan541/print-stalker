import logging


class LoggingCustom:
    @staticmethod
    def log_info(level: str, line: int, msg: str):
        logging.info("[%s] Line %s: %s", level, line, msg)

    @staticmethod
    def log_alert(lines: list, msg: str):
        level = "Alert"
        LoggingCustom.log_info(
            level=level,
            line=",".join(str(e) for e in lines),
            msg=msg
        )
