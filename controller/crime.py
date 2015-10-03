from flask import request
from flask_restful import Resource
from model import Crime,User
class Crime(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['user_id','lat','long']
        if all([data.has_key(k) for k in requirements]) is True:
            lat,long = data['lat'],data['long']
            del(data['lat'])
            del(data['long'])
            ok = Crime().setData(data).location(lat,long).save()
            police = User(data['user_id']).findPolice()

            if ok :
                return {'error' : False,'message' : "Successfully send notification"}
            else:
                return {'error' : True,'message' : "Failed sending location"}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join(requirements)}
    
