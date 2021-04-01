import logging
import os
import multiprocessing as mp
from collections import Counter
from config import PROCESS_COUNT
from resources.word.processor.processor_base import WordProcessBase
from resources.word.utils import timing

logger = logging.getLogger()


class PathWordProcess(WordProcessBase):

    @timing
    def count(self, path_input):
        """
        process files to chucks and count words by chunk and save to db
        :param path_input:
        :return:
        """

        logger.info("start count text row from path: {} ".format(path_input))

        pool = mp.Pool(PROCESS_COUNT)
        jobs = []

        try:
            for chunk_start, chunk_size in self._chunkify(path_input):
                jobs.append(pool.apply_async(self._process_wrapper, (chunk_start, chunk_size, path_input)))

            # wait for all jobs to finish
            for _job in jobs:
                _job.get()

            pool.close()

        except Exception as ex:
            logger.error("fail to count path input error: {}".format(ex))
            pool.close()

    def _process_wrapper(self, chunk_start, chunk_size, file_path):

        count = Counter()

        with open(file_path) as file_obj:
            file_obj.seek(chunk_start)
            lines = file_obj.read(chunk_size).splitlines()
            for line in lines:
                count += self._count_text_to_words(line)

        self._insert(count)

    @staticmethod
    def _chunkify(fname):
        default_size = 10 * 1024
        file_end = os.path.getsize(fname)
        size = file_end if default_size > file_end else default_size

        with open(fname, 'rb') as file_obj:
            chunk_end = file_obj.tell()

            while True:
                chunk_start = chunk_end
                file_obj.seek(size, 1)
                file_obj.readline()
                chunk_end = file_obj.tell()
                yield chunk_start, chunk_end - chunk_start

                if chunk_end > file_end:
                    break
