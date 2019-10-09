__all__ = ["NichtParasoup", "Crawler", "CrawlerWeight", "Crawlers", "Blacklist"]

from typing import Any, Union, Set, Callable, Optional
from random import choice as random_choice

from .crawler import Images, Image, ImageUri, ImageCrawler

CrawlerWeight = Union[int, float]


class Blacklist(Set[ImageUri]):
    pass


_IsImageAddable = Callable[[Image], bool]

_OnImageAdded = Callable[[Image], Any]


class Crawler(object):

    def __init__(self,
                 imagecrawler: ImageCrawler, weight: CrawlerWeight,
                 is_image_addable: Optional[_IsImageAddable] = None,
                 on_image_added: Optional[_OnImageAdded] = None
                 ) -> None:
        self.imagecrawler = imagecrawler
        self.weight = weight if weight > 0 else 1  # typing: CrawlerWeight
        self.images = Images()
        self._is_image_addable = is_image_addable
        self._image_added = on_image_added

    def crawl(self) -> None:
        images_crawled = self.imagecrawler.crawl()
        for image_crawled in images_crawled:
            image_is_addable = self._is_image_addable(image_crawled) if self._is_image_addable else True
            if not image_is_addable:
                continue  # for
            self.images.add(image_crawled)
            if self._image_added:
                self._image_added(image_crawled)


class Crawlers(Set[Crawler]):
    pass


class NichtParasoup(object):

    def __init__(self) -> None:
        self.crawlers = Crawlers()
        self.blacklist = Blacklist()

    def _is_image_not_in_blacklist(self, image: Image) -> bool:
        # must be compatible to: _IsImageAddable
        return image.uri not in self.blacklist

    def _add_image_to_blacklist(self, image: Image) -> None:
        # must be compatible to: _OnImageAdded
        self.blacklist.add(image.uri)

    def add_imagerawler(self, imagecrawler: ImageCrawler, weight: CrawlerWeight) -> None:
        self.crawlers.add(Crawler(
            imagecrawler, weight,
            self._is_image_not_in_blacklist, self._add_image_to_blacklist
        ))

    def get_random_image(self) -> Optional[Image]:
        if not self.crawlers:
            return None
        crawler = random_choice(list(self.crawlers))  # type: Crawler
        crawler.crawl()
        if not crawler.images:
            return None
        image = random_choice(list(crawler.images))
        crawler.images.discard(image)
        return image
