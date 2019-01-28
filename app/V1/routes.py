from flask import Blueprint, url_for
from flask_restful import Resource, Api

mod = Blueprint('api_v1', __name__)

class AllRoutes(Resource):
    def get(self):
        routes = []
        from flask import Flask
        mod_temp_app = Flask(__name__)
        mod_temp_app.register_blueprint(mod)
        for route in mod_temp_app.url_map.iter_rules():
            routes.append(str(route))
        del mod_temp_app
        return routes, 200

class TestConnection(Resource):
    def get(self):
        return {'message':"Connection Success"}, 200

mod_api = Api(mod)
mod_api.add_resource(AllRoutes, '/')
mod_api.add_resource(TestConnection,'/test')