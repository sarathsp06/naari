import random
from  model import Model
from helpers import exotel
from pymongo import  GEOSPHERE
from settings import PoliceNumbers
class User(Model):
    def __init__(self,uid = None):
    	Model.__init__(self)
    	self.collection = self.db['user']
        self.collection.create_index([("loc", GEOSPHERE)])
    	if uid is not None:
    		self.update(self.getDoc(uid))

    def setProfile(self,data):
        if data.has_key('verified'):
            del(data['verified'])
        self.setData(data)
        self.setRole()
        return self

    def setRole(self):
       """
       setRole sets the role for the user which is now  either POLICE or PUBLIC
       For now checking if one is police or not is done by just checking if the mobile number is in the given list in settings
       which will later be changed to may be making an http call to some endpoint which has all the phonenumbers of police men
       """
       print 'POLICENUMBERS',PoliceNumbers
       print 'PHONE', str(self['phone'])
       if str(self['phone']) in PoliceNumbers:
           self['role'] = 'POLICE'
       else:
           self['role'] = 'PUBLIC'

    def otp(self):
        self['otp'] = random.randint(0,100000)
        if  self.save() is not False:
            if exotel.sendOtp(self['phone'],self['otp']) is not False:
                return True
            else:
            	return False
        else:
            return False

    def location(self, lat = None ,long = None):
        if lat is not None and long is not None:
            self['loc'] = map(float,[lat,long]) or self['loc']
        print repr(self)
        return self

    def verify(self,otp):
        if otp is None:
            return False
        if otp == self['otp']:
            self['verified'] = True
            self.save()
            return True
        else:
            return False

    def findPolice(self):
         return [p for p in self.collection.find({"loc": {"$near": self["loc"]},'role':"POLICE"}).limit(10)]
