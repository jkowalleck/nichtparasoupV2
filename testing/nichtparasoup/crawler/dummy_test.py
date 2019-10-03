__all__ = ['CrawlerDummyTest']

import unittest

import typing

from nichtparasoup.crawler import Image
from nichtparasoup.crawler.dummy import Dummy as CrawlerDummy


class CrawlerDummyTest(unittest.TestCase):

    def test_crawl(self) -> None:
        # arrange
        images_crawled: typing.List[Image] = list()
        image_found = images_crawled.append
        crawler = CrawlerDummy('test', image_found)

        # act
        crawler.crawl()

        # assert
        self.assertGreater(len(images_crawled), 0, 'no images crawled')
        self.assertTrue(images_crawled[0].more.get('this_is_a_dummy'), 'this is not a dummy')
