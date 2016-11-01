import os
import uuid
import mimetypes

import falcon

class Resource(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_post(self, req, resp):
        ext = mimetypes.guess_extensions(req.content_type)
        filename = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)
        image_path = os.path.join(self.storage_path, filename)

        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break

                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + filename

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello World!"}'
        resp.status = falcon.HTTP_200
