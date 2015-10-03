from flask import Flask,request
from flask_restful import Resource, Api
import random
from helpers import exotel

#controllers
from controller import Signup,Verify,OTP

app = Flask(__name__)
api = Api(app)

api.add_resource(Signup, '/signup')
api.add_resource(Verify, '/verify')
api.add_resource(OTP, '/otp')

if __name__ == '__main__':
    app.run(debug=True)
