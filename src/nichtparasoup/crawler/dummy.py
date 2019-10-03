from . import Crawler, Image

import uuid


class Dummy(Crawler):

    def crawl(self):
        """ find the same image ... every time """
        uri = './images/logo.png#%s' % uuid.uuid4()
        image = Image(uri=uri, this_is_a_dummy=True)
        self.image_found(image)
