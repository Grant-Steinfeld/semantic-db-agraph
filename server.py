from flask import Flask, request
from flask_restplus import Api, Resource, fields
from query import *

app = Flask(__name__)
api = Api(app, version='0.1.24', title='Allegro API', 
description='REST API to Graph')

allegroNS = api.namespace('allegro', 'triple store operations')
debugNS = api.namespace('dbg', 'debugging calls')

@debugNS.route('/pingpost')
class Pingpost(Resource):

    @api.expect(ping_post)
    def post(self):
        '''
        post test responds with what was passed up
        '''
        try:
            json_ = request.get_json()

            if 'param1' in json_ and 'param2' in json_:
                param1 = json_['param1']
                param2 = json_['param2']


                return [param1, param2, str(datetime.now())]
            else:
                raise Exception( "param1 and param2 are required")
        except Exception as genex:
            api.abort(500,genex.message)




@allegroNS.route('/triples/<repo>')
@api.doc(params={'repo':'repository name'})
class Triples(Resource):
    def get(self, repo):
        return getTriples(repo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878)
