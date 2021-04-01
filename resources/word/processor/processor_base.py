import logging
import re
from abc import abstractmethod, ABC
from collections import Counter

from config import WORD_SPLIT_REGEX
from resources.dal import Dal

logger = logging.getLogger()


class WordProcessBase(ABC):
    _db = Dal()

    @abstractmethod
    def count(self, text_input):
        """
        split, count and insert words to db
        :param text_input:
        """
        pass

    def _process(self, text_line):
        logger.info("start count text row")
        words_count_dict = self._count_text_to_words(text_line)

        if words_count_dict:
            self._insert(words_count_dict)

        else:
            logger.error("failed to count words from line {}".format(text_line))
            raise Exception("Word Process Failed")

    @staticmethod
    def _count_text_to_words(text):

        try:
            map_func = map(
                lambda word: word.lower(),
                re.findall(WORD_SPLIT_REGEX, text
                           ))

            return Counter(map_func)

        except Exception as ex:
            logger.error("fail to count the row, row text: {} error: {} ".format(text, ex))
            return None

    def _insert(self, words_count_dict):
        self._db.insert(words_count_dict)


