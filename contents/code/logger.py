# Setup logging globally (ie root logger)
import types
import logging
import logging.handlers

INFO_NO_NEWLINE = logging.INFO + 1

class MultipleFormatHandler(logging.StreamHandler):

    formatters = {  logging.INFO: logging.Formatter(">>> %(message)s\n"),
                    INFO_NO_NEWLINE: logging.Formatter(">>> %(message)s"),
                    logging.DEBUG: logging.Formatter("%(filename)s:%(lineno)d - %(levelname)s - %(message)s\n"),
                    logging.WARN: logging.Formatter("%(filename)s:%(lineno)d - %(levelname)s - %(message)s\n"),
                    logging.CRITICAL: logging.Formatter("%(filename)s:%(lineno)d - %(levelname)s - %(message)s\n"),
                    logging.ERROR: logging.Formatter("%(filename)s:%(lineno)d - %(levelname)s - %(message)s\n")}

    def format(self,record):
        return self.formatters[record.levelno].format(record)

    def emit(self, record):
        try:
            msg = self.format(record)
            fs = "%s"
            if not hasattr(types, "UnicodeType"): #if no unicode support...
                self.stream.write(fs % msg)
            else:
                try:
                    self.stream.write(fs % msg)
                except UnicodeError:
                    self.stream.write(fs % msg.encode("UTF-8"))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

logger = logging.getLogger('AWSPlasmoid')
logger.setLevel(logging.INFO)

mfh = MultipleFormatHandler()
logger.addHandler(mfh)

syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
formatter = logging.Formatter("%(filename)s:%(lineno)d - %(levelname)s - %(message)s\n")
syslog_handler.setFormatter(formatter)
logger.addHandler(syslog_handler)
