import logging
from flask_restful import Resource
from flask_restful_swagger import swagger

from resources.models import WordModel
from resources.word.service import count_words
from flask_restful import reqparse

logger = logging.getLogger()

parser = reqparse.RequestParser()
parser.add_argument("word", type=str)


class WordResource(Resource):
    @swagger.operation(
        notes="Receives a text input and counts the number of appearances for each word in the input.",
        nickname="post",
        parameters=[
            {
                "name": "word",
                "description": "count words from 3 options, system file path, valid url, simple url",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "word",
            }
        ],
        responseMessages=[
            {
                "code": 201,
                "message": "success to parse words"
            },
            {
                "code": 405,
                "message": "Invalid Word input"
            }
        ]
    )
    def post(self):
        words_dict = parser.parse_args()
        try:
            words = words_dict.get("word")
            if words:
                count_words(words)
                return "success to parse words", 201
            else:
                return "Invalid Word input", 405

        except Exception as ex:
            logger.info("Failed to parse words, error: {}".format(ex))
            return "Failed to parse words", 501
