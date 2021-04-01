import redis

from config import DB_HOST, DB_PORT


class Dal(object):
    _db = redis.Redis(host=DB_HOST, port=DB_PORT)

    def insert(self, input_dict):
        for word, count in input_dict.items():
            self._db.incr(word, count)

    def get_by_key(self, key):
        return self._db.get(key)
