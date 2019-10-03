__all__ = ["Crawler", "CrawlerCallback", "CrawlerError", "Image", ]

import typing
import abc


class Image(object):
    def __init__(self, uri: str, source: typing.Optional[str] = None, **kwargs: typing.Any) -> None:
        self.uri: str = str(uri)
        self.source: typing.Union[str, None] = source if source is None else str(source)
        self.more: typing.Dict[str, typing.Any] = dict(**kwargs)


CrawlerCallback = typing.Callable[[Image], None]

_image_found_noop: CrawlerCallback = lambda image: None


class Crawler(object):
    def __init__(self, site: str, on_image_found: CrawlerCallback = _image_found_noop) -> None:
        self.site: str = site
        self.image_found: CrawlerCallback = on_image_found

    @abc.abstractmethod
    def crawl(self) -> None:
        """
        do the crawling
        for each image found: call self.image_found()
        """
        raise CrawlerError('implementation of abstract missing')


class CrawlerError(Exception):
    pass
