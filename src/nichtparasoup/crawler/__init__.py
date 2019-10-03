__all__ = ["Crawler", "CrawlerCallback", "CrawlerError", "Image", ]

import abc
import typing


class Image(object):

    def __init__(self, uri: str, source: typing.Optional[str] = None, **kwargs) -> None:
        self.uri = str(uri)
        self.source = None if source is None else str(source)
        self.more = dict(**kwargs)


CrawlerCallback = typing.Callable[[Image], None]


def _image_found_noop(_: Image) -> None:
    # must be compatible to: CrawlerCallback
    pass


class Crawler(object):

    def __init__(self, site: str, on_image_found: CrawlerCallback = _image_found_noop) -> None:
        self.site = str(site)
        self.image_found = on_image_found  # type: CrawlerCallback

    @abc.abstractmethod
    def crawl(self) -> None:
        """
        do the crawling
        for each image found: call self.image_found()
        """
        raise CrawlerError('implementation of abstract missing')


class CrawlerError(Exception):
    pass
