__all__ = ["Dummy"]

from . import ImageCrawler, Images, Image

import uuid


class Dummy(ImageCrawler):

    def crawl(self) -> Images:
        images = Images()
        images.add(Image(
            '#%s' % uuid.uuid4(),  # @TODO add data url to the logo or something
            this_is_a_dummy=True
        ))
        return images
