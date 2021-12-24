from modules.baseResource import baseResource
from bson import ObjectId
from mongo.db import db

class ProductUpdate(baseResource):
    def __init__(self):
        super().__init__()

    def put(self,id):
        # Validation        
        
        # UseCase
        product = db().product()
        data = product.updateById(self.query['_id'],{
            'product_name':self.props['product_name'],
            'price':self.props['price'],
            'user_id':ObjectId(self.props['user_id'])})
        # UseCase
        return data