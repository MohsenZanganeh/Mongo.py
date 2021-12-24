from .models import product,user
import config
from pymongo import MongoClient


class db():

    def __init__(self):
        self.client = MongoClient(
            config.MONGO['host'],
            config.MONGO['port'],
            username=config.MONGO['username'],
            password=config.MONGO['password'])[config.MONGO['database']]

    def product(self):
        if ('product' in self.client.list_collection_names()) == False:
            product.Create_Product_Schema(self.client)
        return product.ProductModel(self.client)

    def user(self):
        if ('user' in self.client.list_collection_names()) == False:
            user.Create_User_Schema(self.client)
        return user.UserModel(self.client)