#!/bin/bash/python3
# -*- encoding: utf-8 -*-
import logging

# 创建logger对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建FileHandler对象
fh = logging.FileHandler('log.log')
fh.setLevel(logging.DEBUG)

# 创建Formatter对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 将FileHandler对象添加到Logger对象中
logger.addHandler(fh)

# 记录日志信息
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
