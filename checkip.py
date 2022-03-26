import os
from flask import *
from flask_restful import Resource, Api
from waitress import serve

app = Flask(__name__)
api = Api(app)


class checkip(Resource):
    def get(self):
        return (request.remote_addr)

api.add_resource(checkip,'/checkip')

if __name__ == '__main__':
    #os.environ['FLASK_ENV'] = 'development'
    #app.run(debug=True, host='0.0.0.0',port=5000)
    serve(app, host='0.0.0.0', port=5000)