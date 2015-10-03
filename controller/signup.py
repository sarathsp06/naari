from flask import request
from flask_restful import Resource
from model import  User

class Signup(Resource):
    def post(self):
        data = request.get_json()
        requirements = ['name','phone','age','gender']
        if all([data.has_key(k) for k in requirements]) is True:
            ok = User().setProfile(data).save()
            if ok:
                return {'error' : False, 'user_id' : ok}
            else:
                return {'error' : True, 'reason' : "Invalid profile information"}
        else:
            return {'error' : True, 'reason' : "Mandatory information is missing " + (",").join
            (requirements)}
