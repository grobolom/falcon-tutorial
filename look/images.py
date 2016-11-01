import falcon

class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello World!"}'
        resp.status = falcon.HTTP_200
