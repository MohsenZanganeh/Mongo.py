import json
from bson.objectid import ObjectId
from flask_restful import Resource
from flask import request

class baseResource(Resource):
    def __init__(self):
        data = request.get_json()
        if request.files:
            self.files = request.files.getlist('file')

        if request.form:
            form = {}
            for key in request.form.keys():
                try:
                    form[key] = json.loads(request.form.get(key))
                except:
                    form[key] = request.form.get(key)
            self.props = form
        
        if isinstance(data,dict):
            self.user = data.get('user')
            self.props = data.copy()

            if self.props.get('user'):
                del self.props['user']
            
        self.query = {}
        if request.args:
            request.args = dict(request.args)
            if request.args.get('id'):
               request.args['_id'] = ObjectId(request.args['id'])
               del request.args['id']
            else:
                request.args['_id'] = ObjectId(request.args['_id'])

            self.query = {**request.args,**self.query}
        
        if request.view_args:
            if request.view_args.get('id'):
               request.view_args['_id'] = ObjectId(request.view_args['id'])
               del request.view_args['id'] 
            else:
                request.view_args['_id'] = ObjectId(request.view_args['_id'])
                
            self.query = {**request.view_args,**self.query}