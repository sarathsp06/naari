from flask import request
from flask_restful import Resource
from model import Crime as CrimeModel,User
from helpers import exotel
class Crime(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['user_id','lat','long']
        if all([data.has_key(k) for k in requirements]) is True:
            lat,long = data['lat'],data['long']
            del(data['lat'])
            del(data['long'])
            user =  User(data['user_id'])
            police = user.findPolice()
            ok = CrimeModel().setData(data).location(lat,long).save()
            if ok :
                if len(police) == 0:
                    return {'error' : True,'message' : "No Poilice men available currently try again please"}
                else:
                    exotel.smsPolice(map(lambda x:x['phone'],police),lat,long)
                    exotel.callPolice(user['phone'],police[0]['phone'])
                    return {'error' : False,'message' : "Successfully send notification and calling " + police[0]['name']}
            else:
                return {'error' : True,'message' : "Failed sending crime report "}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join(requirements)}
