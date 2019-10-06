__all__ = ["ImageCrawler", "Images", "Image", "ImageUri", "ImageSource", "_EmptyImageCrawler"]

import abc
import typing

ImageUri = str  # maybe this becomes ab wb class, later

ImageSource = str  # maybe this becomes ab wb class, later


class Image(object):

    def __init__(self, uri: ImageUri, source: typing.Optional[ImageSource] = None, **more: typing.Any) -> None:
        self.uri = uri
        self.source = source
        self.more = more

    def __hash__(self) -> int:
        """ the uri is the identifier of Image. uri determines the hash """
        return hash(self.uri)


class Images(typing.Set[Image]):
    pass


class ImageCrawler(abc.ABC):

    def __init__(self, site: str) -> None:
        self.site = site

    @abc.abstractmethod
    def crawl(self) -> Images:
        raise Exception('this abstract method was not implemented')  # pragma: no cover


class _EmptyImageCrawler(ImageCrawler):
    """ a crawler that finds nothing. use it for mocking... """

    def crawl(self) -> Images:
        return Images()  # pragma: no cover
