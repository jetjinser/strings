from nonebot.default_config import *
from datetime import timedelta

HOST = '127.0.0.1'
PORT = 8080
DEBUG = True
COMMAND_START = {'', '/', '!', '$'}
NICKNAME = {'五十弦', '弦', 'hello', 'Hello', 'hi', 'Hi'}
TULING_API_KEY = []
SUPERUSERS = {2301583973, 963949236}
SESSION_RUNNING_EXPRESSION = '当前会话未结束'
DEFAULT_VALIDATION_FAILURE_EXPRESSION = '语法错误'
TOO_MANY_VALIDATION_FAILURES_EXPRESSION = (
    '你输错太多次了，会不会玩啊',
    'wdnmd',
    '?'
)
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
