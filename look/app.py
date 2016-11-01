import falcon

import images

api = application = falcon.API()

storage_path = '/tmp/look'

images = images.Resource(storage_path)
api.add_route('/images', images)
