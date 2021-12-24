from modules.baseResource import baseResource
from mongo.db import db
from bson import json_util, ObjectId

class ProductCreate(baseResource):
    def __init__(self):
        super().__init__()

    def post(self):
        # Validation        
        product = db().product()
        data = product.insert({
            'product_name':self.props['product_name'],
            'price':self.props['price'],
            'user_id':ObjectId(self.props['user_id'])})
        # UseCase
        return data