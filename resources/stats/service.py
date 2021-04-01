import logging
from flask_restful import abort

from resources.dal import Dal

logger = logging.getLogger()


def search_for_word(word):
    db = Dal()

    if not isinstance(word, str):
        error_msg = "bad word input {} ".format(word)
        logger.error(error_msg)
        abort(405, message=error_msg)

    word_count = db.get_by_key(word.lower())

    if not word_count:
        error_msg = "word not found: {} ".format(word)
        abort(404, message=error_msg)

    logger.info("The word {} appears {} times ".format(word, word_count))

    return {"word": word, "count": int(word_count)}, 200
