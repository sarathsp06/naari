from flask import request
from flask_restful import Resource
from model import User

class Location(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['user_id','lat','long']
        if all([data.has_key(k) for k in requirements]) is True:
            ok = User(data['user_id']).location(data['lat'],data['long']).save()
            if ok :
                return {'error' : False,'message' : "Successfully set location"}
            else:
                return {'error' : True,'message' : "Failed sentting location"}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join(requirements)}
