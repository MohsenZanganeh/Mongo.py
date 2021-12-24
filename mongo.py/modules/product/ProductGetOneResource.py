from modules.baseResource import baseResource
from mongo.db import db

class ProductGetOne(baseResource):
    def __init__(self):
        super().__init__()

    def get(self,id):
        # Validation        
        
        # UseCase
        product = db().product()
        
        # UseCase
        return product.get_all(_id=self.query['_id'],is_deleted=False,join=True)