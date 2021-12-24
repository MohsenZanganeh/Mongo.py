from mongo.models.AbstractRepository import AbstractRepository


def Create_User_Schema(db):
    db.create_collection('user', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'properties': {
                'username': {
                    'bsonType': 'string',
                    'description': 'username of user'
                },
                'password': {
                    'bsonType': 'string',
                    'description': 'password of user'
                }
            }
        }
    })


class UserModel(AbstractRepository):
    def __init__(self, db):
        relations = []
        self.model = db.get_collection('user')
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
