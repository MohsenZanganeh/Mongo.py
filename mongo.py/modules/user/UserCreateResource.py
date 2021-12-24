from modules.baseResource import baseResource
from mongo.db import db

class UserCreate(baseResource):
    def __init__(self):
        super().__init__()

    def post(self):
        # Validation        
        user = db().user()
        data = user.insert({'username':self.props['username'],'password':self.props['password']})
        # UseCase
        return data