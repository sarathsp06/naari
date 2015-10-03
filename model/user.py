import random
from  model import Model
from helpers import exotel
class User(Model):
    def __init__(self,uid = None):
    	Model.__init__(self)
    	self.collection = self.db['user']
    	if uid is not None:
    		self.update(self.getDoc(uid))
        print self

    def setProfile(self,data):
        self.setData(data)
        return self

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
       self['latitude'] = lat or self['latitude']
       self['longitude'] = lat or self['longitude']
       return self
       
    def verify(self,otp):
        if otp is None:
            return false
        if otp == self['otp']:
            return True
        else:
            return False
