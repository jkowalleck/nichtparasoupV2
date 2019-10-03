__all__ = ['NichtParasoup']

import typing

from .crawler import Image, Crawler, CrawlerError

from .crawler.dummy import Dummy as DummyCrawler

Factor = typing.TypeVar('Factor', int, float)


class ImageList(typing.Set[Image]):
    pass


class BlackList(typing.Set[str]):
    pass


class CrawlerList(typing.List[typing.Tuple[Crawler, Factor, ImageList]]):
    pass


class NichtParasoup(object):

    def __init__(self) -> None:
        self.crawlers = CrawlerList()
        self.blacklist = BlackList()

    def add_crawler(self, crawler: typing.Union[Crawler, str], site: str = None, factor: Factor = None) -> None:
        if isinstance(crawler, Crawler):
            return self._add_crawler_object(crawler, factor)
        else:
            return self._add_crawler_site(crawler, site, factor)

    def _add_crawler_object(self, crawler: Crawler, factor: Factor = None) -> None:
        images = ImageList()
        crawler.image_found = lambda image: images.add(image) if image not in self.blacklist else None

        self.crawlers.append((
            crawler,
            factor if factor is not None and 0 < factor <= 10 else 1,
            images,
        ))

    def _add_crawler_site(self, crawler_name: str, site: str, factor: Factor = None) -> None:
        crawler_name = crawler_name.lower()
        for crawler_subclass in Crawler.__subclasses__():
            if crawler_name == crawler_subclass.__name__.lower():
                return self._add_crawler_object(crawler_subclass(site), factor)
        raise Exception('unknown crawler: %s' % crawler_name)
