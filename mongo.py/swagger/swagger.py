import os
from dotenv import load_dotenv
load_dotenv('.env', verbose=True)
SERVER_URL = os.getenv('SERVER_URL')

swagger = {
    "openapi": "3.0.0",
    "info": {
        "version": "1.0.0",
        "title": "Product",
        "contact": 'null',
        "description": 'Apis'
        f'''
       <a href="http://{SERVER_URL}:5001/api/docs">Product Service</a>
       '''
    },
    "basePath": "/api",
    "tags": [
        {
            "name": "Product",
        },
        {
            "name": "User",
        }
    ],
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "in": "header"
            }
        }
    },
    "paths": {
        "/product/": {
            "post": {
                'is_admin': True,
                "summary": "Create product",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Product'
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "product_name": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "string"
                                    },
                                    "user_id": {
                                        "type": "string"
                                    }
                                }
                            },
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Template Created"
                    }
                }
            },
            "get": {
                'is_admin': True,
                "summary": "Get All Product",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Product'
                ],
                "responses": {
                    "201": {
                        "description": "Got All Product"
                    }
                }
            }
        },
        "/product/{_id}": {
            "put": {
                'is_admin': True,
                "summary": "Update Product",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Product'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "_id",
                        "description": "_id of Product",
                        "schema": {
                            "type": "string",
                            "required": [
                                "_id"
                            ]
                        }
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": [
                                    "product_name"
                                ],
                                "properties": {
                                    "product_name": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "string"
                                    },
                                    "user_id": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Product Updated"
                    }
                }
            },
            "get": {
                'is_admin': True,
                "summary": "Get One Product",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Product'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "_id",
                        "description": "_id of Product",
                        "schema": {
                            "type": "string",
                            "required": [
                                "_id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Got a Product"
                    }
                }
            },
            "delete": {
                'is_admin': True,
                "summary": "Delete A Product",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Product'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "_id",
                        "schema": {
                            "type": "string",
                            "required": [
                                "_id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Product Deleted"
                    }
                }
            }
        },
        "/user/": {
            "post": {
                'is_admin': True,
                "summary": "Create User",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'User'
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "username": {
                                        "type": "string"
                                    },
                                    "password": {
                                        "type": "string"
                                    }
                                }
                            },
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Template Created"
                    }
                }
            },
            "get": {
                'is_admin': True,
                "summary": "Get All user",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'User'
                ],
                "responses": {
                    "201": {
                        "description": "Got All User"
                    }
                }
            }
        }
    }
}


def generate_swagger(swagger):
    for path in swagger['paths']:
        methods = swagger['paths'][path]
        for method in methods:
            is_public = methods[method].get('is_public')
            if is_public == None or is_public == False:
                methods[method]['security'] = [{'bearerAuth': []}]
    return swagger


generated_swagger = generate_swagger(swagger)
