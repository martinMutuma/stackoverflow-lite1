from app import stolite
from flask import Blueprint, url_for
from flask_restful import Resource, Api


class AllAppRoutes(Resource):
    def get(self):
        routes = []
        for route in stolite.url_map.iter_rules():
            routes.append(str(route))
        return {
            'routes':routes,
            'message':'All Methods in the api'}, 200


api = Api(stolite)
api.add_resource(AllAppRoutes, '/')
