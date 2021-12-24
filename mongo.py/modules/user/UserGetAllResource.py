from modules.baseResource import baseResource
from mongo.db import db

class UserGetAll(baseResource):
    def __init__(self):
        super().__init__()

    def get(self):
        # Validation        
        user = db().user()
        
        # UseCase
        return user.get_all()