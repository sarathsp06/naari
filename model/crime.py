from flask import request
from flask_restful import Resource
from model import User

class OTP(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['user_id']
        if all([data.has_key(k) for k in requirements]) is True:
            ok = User(data['user_id']).otp()
            if ok :
                return {'error' : False,'message' : "Successfully sent otp"}
            else:
                return {'error' : True,'message' : "Failed sending otp try after sometime "}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join(requirements)}
