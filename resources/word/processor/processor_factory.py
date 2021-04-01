from resources.word.processor.path_processor import PathWordProcess
from resources.word.processor.simple_processor import SimpleWordProcess
from resources.word.processor.url_processor import UrlWordProcess
from resources.word.utils import is_valid_url, is_valid_file_path


class WordProcessorFactory(object):

    @staticmethod
    def create_word_processor(text_input):

        if is_valid_url(text_input):
            return UrlWordProcess()

        elif is_valid_file_path(text_input):
            return PathWordProcess()
        else:
            return SimpleWordProcess()