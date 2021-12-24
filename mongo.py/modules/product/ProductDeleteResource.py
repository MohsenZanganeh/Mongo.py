from modules.baseResource import baseResource
from mongo.db import db
from bson import ObjectId

class ProductDelete(baseResource):
    def __init__(self):
        super().__init__()

    def delete(self,id):
        # Validation        
        
        # UseCase
        product = db().product()
        data = product.delete(self.query['_id'])
        print('====data:',data)
        if data:
            return {'message':'product deleted successfully'}
        return {'message':"product didn't delete"}