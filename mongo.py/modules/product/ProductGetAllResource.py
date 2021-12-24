from modules.baseResource import baseResource
from bson import ObjectId
from mongo.db import db
class ProductGetAll(baseResource):
    def __init__(self):
        super().__init__()

    def get(self):
        # Validation        
        product = db().product()
        
        # UseCase
        return product.get_all(is_deleted=False,join=True)