from flask import Flask
from flask_restful import  Api

#controllers
from controller import Signup,Verify,OTP,Location,Crime

#init the applicaton classes
app = Flask(__name__)
api = Api(app)

#Routes
api.add_resource(Signup, '/signup')
api.add_resource(OTP, '/otp')
api.add_resource(Verify, '/verify')
api.add_resource(Location,'/location')
api.add_resource(Crime,'/crime')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
