from flask import Flask
from flask_restx import Api


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='Algoritmo Djkastra',
                       description='Esta documentação é relacionada para demonstrar o caminho mais curto entre dois pontos, utilizando o algoritmo Djkastra',
                       doc='/docs'
                       )

    def run(self):
        self.app.run(
            debug=True  # enable debug mode for development
        )


server = Server()
