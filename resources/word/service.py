import logging

from resources.word.processor.processor_factory import WordProcessorFactory

logger = logging.getLogger()


def count_words(text_input):
    word_factory = WordProcessorFactory
    logger.info("start counting words")
    word_processor =  word_factory.create_word_processor(text_input)
    word_processor.count(text_input)


