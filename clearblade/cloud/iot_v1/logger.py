import os
import sys
import logging
from traceback import format_exception


class CbLogger():

    def __init__(self, name):
        self.logger_name = name
        self.log_filename = 'clearblade_python_iot_sdk.log'
        self._create_log_file()
        self._create_logger()

    def _create_log_file(self):
        current_os = sys.platform
        user_dir = os.path.expanduser("~")
        log_dir_path = user_dir

        if current_os == "win32":
            log_dir_path = self._create_logfile_path_for_windows(user_dir)

        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)

        self.log_filename_with_path = os.path.join(log_dir_path, self.log_filename)

    def _create_logfile_path_for_windows(self, user_home_dir):

        documents_dir = os.path.join(user_home_dir, "Documents")
        if not os.path.exists(documents_dir):
            os.mkdir(documents_dir)

        log_dir = os.path.join(documents_dir, "clerblade")
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        return log_dir

    def _create_logger(self):
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(self.log_filename_with_path, mode="a")
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
                    "%(asctime)s %(name)s - %(levelname)s -%(lineno)d- %(message)s")
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
        self.logger.addHandler(stream_handler)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def exception_handler(self, exception_type, value, tb):
        formatted_exception = " ".join(format_exception(exception_type, value, tb))
        self.logger.exception("Uncaught exception: {0} ".format(formatted_exception))
