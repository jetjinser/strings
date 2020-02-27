from os import path

# import logging
import nonebot
# from nonebot.log import logger

import config
# logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins')
    # logger.info('Starting')
    nonebot.run(host='127.0.0.1', port=8080)
