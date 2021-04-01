import os
import re
import logging
from functools import wraps
from time import time
from config import URL_REGEX


def is_valid_file_path(text):
    """
    check if text is valid file path
    :param text:
    :return boolean:
    """
    return isinstance(text, str) and os.path.isfile(text)


def is_valid_url(text):
    """
    check if text is valid url
    :param text:
    :return boolean:
    """
    return isinstance(text, str) and re.match(URL_REGEX, text) is not None


def timing(function):
    """
    timer decorator
    :param function:
    """
    @wraps(function)
    def wrap(*args, **kw):
        logger = logging.getLogger()
        ts = time()
        result = function(*args, **kw)
        te = time()
        logger.info('func:%r args:[%r, %r] took: %2.4f sec' % (function.__name__, args, kw, te - ts))
        return result

    return wrap
