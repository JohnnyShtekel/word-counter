from resources.word.processor.processor_base import WordProcessBase
from resources.word.utils import timing


class SimpleWordProcess(WordProcessBase):

    @timing
    def count(self, text_input):
        """
       split, count and insert simple text words to db
       :param text_input:
       :return None
        """
        self._process(text_input)