from logging.config import fileConfig
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful_swagger import swagger

from resources.stats.stats import StatsResource
from resources.word.word import WordResource

fileConfig('logger.ini')
app = Flask(__name__)
CORS(app)

api = swagger.docs(
    Api(app),
    apiVersion="0.1",
    basePath="http://localhost:5000",
    resourcePath="/",
    produces=["application/json", "text/html"],
    api_spec_url="/api/spec",
    description="Word counter Service",
)

api.add_resource(WordResource, "/api/word/counter")
api.add_resource(StatsResource, "/api/word/statistics/<string:word>")


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)
