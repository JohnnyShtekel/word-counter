import os
import re
import multiprocessing

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

WORD_SPLIT_REGEX = r'([a-zA-Z]+(?:_[a-zA-Z]+)*)'
URL_REGEX = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

DB_PORT = os.environ.get('DB_PORT', 6379)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
PROCESS_COUNT = multiprocessing.cpu_count()
