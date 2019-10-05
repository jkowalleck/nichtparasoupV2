__all__ = ["ImageCrawler", "Images", "Image", "ImageUri", "ImageSource"]

import abc
import typing

ImageUri = str

ImageSource = str


class Image(object):

    def __init__(self, uri: ImageUri, source: typing.Optional[ImageSource] = None, **more) -> None:
        self.uri = uri
        self.source = source
        self.more = more

    def __hash__(self) -> int:
        """ the uri is the identifier of Image """
        return hash(self.uri)


class Images(typing.Set[Image]):
    pass


class ImageCrawler(abc.ABC):

    def __init__(self, site: str) -> None:
        self.site = site

    @abc.abstractmethod
    def crawl(self) -> Images: pass
