import logging
import os

PROJECT_NAME = "WAInstitution_YRB_2021"
ROOT = "/Users/songshgeo/Documents/Pycharm/WAInstitution_YRB_2021"

# BASIC logging settings.
LOG_FORMAT = "%(asctime)s %(levelname)s %(filename)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
FILE_LEVEL = 'debug'
CMD_LEVEL = 'warn'

def getLogger(filename):
    logging.basicConfig(
                        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S ',
                        level=logging.INFO)
    # logger = logging.getLogger(os.path.join("../log/",filename))
    logger=logging.getLogger(filename)
    KZT = logging.StreamHandler()
    KZT.setLevel(logging.DEBUG)
    logger.addHandler(KZT)
    return logger


# def set_logger(name, path=None, reset=False, log_format=None, file_level="debug", cmd_level="info"):
#     """
#     Setup a log file for my project.
#     :param name: logger's name
#     :param path: sub-folder path of the log file
#     :param reset: remove the old log file and refresh new one?
#     :param log_format: format of file message.
#     :param file_level: message save level in file.
#     :param cmd_level: message level print in CMD
#     :return: a logger.
#     """
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)
#
#     file_level = getattr(logging, file_level.upper())
#     cmd_level = getattr(logging, cmd_level.upper())
#
#     if path:
#         file_path = os.path.join(ROOT, path, f"{name}.log")
#     else:
#         file_path = os.path.join(ROOT, f"{name}.log")
#     if not log_format:
#         log_format = LOG_FORMAT
#     if reset:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError(f"Logging file not found in {file_path}, no need of reset.")
#         else:
#             os.remove(file_path)
#
#     # 建立一个 FileHandler 来把日志记录在文件里
#     file_handler = logging.FileHandler(file_path)
#     file_handler.setLevel(file_level)
#     file_handler.setFormatter(logging.Formatter(log_format))
#
#     # 建立一个 StreamHandler 来把日志打在CMD窗口上
#     cmd_handler = logging.StreamHandler()
#     cmd_handler.setLevel(cmd_level)
#     cmd_handler.setFormatter(logging.Formatter(log_format))
#
#     logger.addHandler(file_handler)
#     logger.addHandler(cmd_handler)
#     logger.info(f"{name} starts logging.")
#     return logger
#
#
# log = set_logger(PROJECT_NAME, file_level=FILE_LEVEL, cmd_level=CMD_LEVEL)
#
# if __name__ == '__main__':
#     log = set_logger(PROJECT_NAME, reset=True, file_level="info", cmd_level="warn")
#     log.info("LOG reset.")