from flask import request
from flask_restful import Resource
from model import User
class Verify(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['user_id','otp']
        if all([data.has_key(k) for k in requirements]) is True:
            ok = User(data['user_id']).verify(data['otp'])
            if ok :
                return {'error' : False,'message' : "Successfully verifyied the account"}
            else:
                return {'error' : True,'message' : "Failed verifying the account"}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join(requirements)}
