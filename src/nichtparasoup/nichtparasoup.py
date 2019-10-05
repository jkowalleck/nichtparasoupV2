__all__ = ['NichtParasoup', 'CrawlerWeight', 'Crawler', 'Crawlers', 'BlackList']

import typing

from .crawler import Images, Image, ImageUri, ImageCrawler

CrawlerWeight = typing.Union[int, float]


class BlackList(typing.Set[ImageUri]):
    pass


_IsImageAddable = typing.Callable[[Image], bool]

_OnImageAdded = typing.Callable[[Image], typing.Any]


class Crawler(object):

    def __init__(self,
                 imagecrawler: ImageCrawler, weight: CrawlerWeight,
                 is_image_addable: typing.Optional[_IsImageAddable] = None,
                 on_image_added: typing.Optional[_OnImageAdded] = None
                 ):
        self.imagecrawler = imagecrawler
        self.weight = weight if weight > 0 else 1
        self.images = Images()
        self._is_image_addable = is_image_addable
        self._image_added = on_image_added

    def crawl(self):
        images_crawled = self.imagecrawler.crawl()
        for image_crawled in images_crawled:
            image_is_addable = self._is_image_addable(image_crawled) if self._is_image_addable else True
            if not image_is_addable:
                continue  # for
            self.images.add(image_crawled)
            if self._image_added:
                self._image_added(image_crawled)


class Crawlers(typing.Set[Crawler]):
    pass


class NichtParasoup(object):

    def __init__(self) -> None:
        self.crawlers = Crawlers()
        self.blacklist = BlackList()

    def _is_image_not_in_blacklist(self, image: Image) -> bool:
        # must be compatible to: _IsImageAddable
        return image.uri not in self.blacklist

    def _add_image_to_blacklist(self, image: Image) -> None:
        # must be compatible to: _OnImageAdded
        self.blacklist.add(image.uri)

    def add_imagerawler(self, imagecrawler: ImageCrawler, weight: CrawlerWeight):
        self.crawlers.add(Crawler(
            imagecrawler, weight,
            self._is_image_not_in_blacklist, self._add_image_to_blacklist
        ))
