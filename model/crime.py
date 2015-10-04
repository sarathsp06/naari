import random
from  model import Model
from helpers import exotel
from pymongo import  GEOSPHERE
class Crime(Model):
    def __init__(self,id = None):
    	Model.__init__(self)
    	self.collection = self.db['crime']
        self.collection.create_index([("loc", GEOSPHERE)])
    	if id is not None:
    		self.update(self.getDoc(id))
    def location(self, lat = None ,long = None):
        if lat is not None and long is not None:
            self['loc'] = map(float,[lat,long]) or self['loc']
        print repr(self)
        return self
