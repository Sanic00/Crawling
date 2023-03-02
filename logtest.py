import logging.handlers
import logging
import os
import datetime
def log():
    logger = logging.getLogger()
# 로그의 출력 기준 설정
    logger.setLevel(logging.WARNING)

# log 출력 형식
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info('Warning message!')

# log를 파일에 출력
# file_handler = logging.FileHandler('C:/python_workspace/log')
    file_handler = logging.handlers.TimedRotatingFileHandler(
    filename='test', when='midnight', interval=1, encoding='utf-8'
    )

    file_handler.setFormatter(formatter)
    file_handler.suffix = '%Y%m%d'
    file_handler.setLevel(logging.WARNING)

    logger.addHandler(file_handler)
