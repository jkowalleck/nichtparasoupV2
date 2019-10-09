__all__ = ["Dummy"]

import uuid
import urllib.parse

from . import ImageCrawler, Images, Image


class Dummy(ImageCrawler):

    def crawl(self) -> Images:
        images = Images()
        images.add(Image(
            "#" + urllib.parse.urlencode({
                # @TODO add data url to the logo or something
                "site": self.site,
                "uuid": str(uuid.uuid4())
            }),
            source=None,
            this_is_a_dummy=True
        ))
        return images
