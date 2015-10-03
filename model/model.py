from pymongo import MongoClient
import settings
import uuid
class Model(dict):
	def __init__(self):
		dict.__init__(self)
		self.client = MongoClient(settings.mongo_host,settings.mongo_port)
		self.db = self.client[settings.mongo_databse]
		self.collection = None
		
	def setData(self,data):
		if data.get('_id',None) is None and self.get('_id',None )is None:
			data['_id'] =  uuid.uuid4().get_hex()
		self.update(data)
		return True

	def save(self):
		return self.collection.save(self)

	def getDoc(self,id):
		return self.collection.find_one({"_id":id}) or {}
