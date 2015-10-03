import random
from  model import Model
from helpers import exotel
from pymongo import  GEOSPHERE
class Crime(Model):
    def __init__(self,uid = None):
    	Model.__init__(self)
    	self.collection = self.db['crime']
        self.collection.create_index([("loc", GEOSPHERE)])
    	if uid is not None:
    		self.update(self.getDoc(uid))
        print self

    def notify(self,otp):
        exotel.exotel.sms(self, self.phonefrom_number, to, txt):
