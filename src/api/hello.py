from flask_restful_swagger_2 import Resource


class Hello(Resource):
    def get(self):
        return {'hello': 'world'}
