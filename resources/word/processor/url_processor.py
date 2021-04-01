import logging

import requests
from resources.word.processor.processor_base import WordProcessBase
from resources.word.utils import timing

logger = logging.getLogger()


class UrlWordProcess(WordProcessBase):

    @timing
    def count(self, url_input):
        """
        split, count and insert url req of words to db
        :param url_input:
        :return None
         """

        logger.info("start fetch text from url :{} ".format(url_input))
        res = requests.get(url_input)
        if res.status_code == 200:
            text = res.text
            logger.info(" the request successfully received  start process. url: {}".format(url_input))

            if isinstance(text, str):
                self._process(text)
            else:
                raise Exception("Fail to process words from url {}".format(url_input))

        else:
            raise Exception("request failed. url: {} error code: {} ,error message: {}".format(url_input, res.status_code, res.text))
