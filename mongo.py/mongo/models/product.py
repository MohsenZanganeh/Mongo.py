from mongo.models.AbstractRepository import AbstractRepository


def Create_Product_Schema(db):
    db.create_collection('product', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'properties': {
                'product_name': {
                    'bsonType': 'string',
                    'description': 'name of product'
                },
                'price': {
                    'bsonType': 'string',
                    'description': 'price of product'
                },
                'user_id': {
                    'bsonType': 'objectId',
                    'description': 'id of user that created user'
                }
            }
        }
    })


class ProductModel(AbstractRepository):
    def __init__(self, db):
        relations = [
            {'field': 'user_id', 'model': 'user'},
        ]
        self.model = db.get_collection('product')
        super().__init__(db, self.model,relations = relations)

# "fields": {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             # for example key-orderValue => title-1
#             "([A-Za-z]+-[0-9]+)": {
#                 "type": "object",
#                 "properties": {
#                    "id": {
#                        "type_id": "ObjectId"
#                    },
#                    "title": {
#                        "type": "string"
#                    },
#                    "value": {
#                        "type": "string"
#                    },
#                    "amount_type_id": {
#                        "type": "integer"
#                    },
#                    "field_type_id": {
#                        "type": "integer"
#                    }
#                 }
#             }
#         }
#     }
# }
