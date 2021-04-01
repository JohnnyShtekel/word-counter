from resources.word.processor.path_processor import PathWordProcess
from resources.word.processor.processor_factory import WordProcessorFactory
from resources.word.processor.simple_processor import SimpleWordProcess
from resources.word.processor.url_processor import UrlWordProcess


def test_processor_factory_url():
    url = "https://www.google.com"
    url_processor = WordProcessorFactory.create_word_processor(url)
    assert type(url_processor) is UrlWordProcess


def test_processor_factory_path():
    path = "/var/www/app/bucket/test.txt"
    path_processor = WordProcessorFactory.create_word_processor(path)
    assert type(path_processor) is PathWordProcess


def test_processor_factory_simple_string():
    path = "just a simple string"
    simple_string_processor = WordProcessorFactory.create_word_processor(path)
    assert type(simple_string_processor) is SimpleWordProcess
