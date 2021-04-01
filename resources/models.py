from flask_restful_swagger import swagger


@swagger.model
class WordModel:
    def __init__(self, word):
        self.word = word


@swagger.model
class StatsModel:
    def __init__(self, word, count):
        self.word = word
        self.count = count
