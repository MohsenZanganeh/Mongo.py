from .product import \
ProductCreateResource,\
ProductDeleteResource,\
ProductUpdateResource,\
ProductGetAllResource,\
ProductGetOneResource
from .user import \
UserCreateResource,\
UserGetAllResource

resources_dict = {
    'product':[
        [ProductCreateResource.ProductCreate, '/'],
        [ProductDeleteResource.ProductDelete, '/<string:id>'],
        [ProductUpdateResource.ProductUpdate, '/<string:id>'],
        [ProductGetOneResource.ProductGetOne, '/<string:id>'],
        [ProductGetAllResource.ProductGetAll, '/']
    ],
    'user':[
        [UserCreateResource.UserCreate, '/'],
        [UserGetAllResource.UserGetAll, '/']
    ]
}
