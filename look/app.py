import falcon

import images

api = application = falcon.API()

storage_path = '/tmp/look'

image_collection = images.Collection(storage_path)
image = images.Resource(storage_path)

api.add_route('/images', image_collection)
api.add_route('/images/{name}', image)
