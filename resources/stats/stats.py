from flask_restful import Resource
from flask_restful_swagger import swagger
from resources.models import StatsModel, WordModel
from resources.stats.service import search_for_word


class StatsResource(Resource):
    @swagger.operation(
        notes='Receives a word and returns the number of times the word appeared so far',
        responseClass=StatsModel.__name__,
        nickname='stats',
        parameters=[
            {
              "name": "body",
              "description": "Search Word",
              "required": True,
              "allowMultiple": False,
              "dataType": StatsModel.__name__,
              "paramType": "body"
            }
          ],
        )
    def get(self, word):
        return search_for_word(word)
