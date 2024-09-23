from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from server.instance import server

api, app = server.api, server.app

# Create a namespace
routes_ns = Namespace('routes', description='Rotas relacionadas ao algoritmo Djkstra')

# Add the namespace to the API
api.add_namespace(routes_ns)


@api.doc(params={
    'Origem': {
        'description': 'Selecione a cidade de origem',
        'required': True,
        'enum': ['', 'Taió', 'Rio do Sul', 'Rio do Oeste']
    },
    'Destino': {
        'description': 'Selecione a cidade de destino',
        'required': True,
        'enum': ['', 'Taió', 'Rio do Sul', 'Rio do Oeste']
    }
})
@routes_ns.route('/teste')
class Algorithm(Resource):
    def get(self):
        origem = request.args.get('Origem')
        destino = request.args.get('Destino')

        if not origem and not destino:
            return {'message': 'Name and greeting are required!'}, 400

        return {'message': f" A origem é de {origem} até {destino}!"}, 200
