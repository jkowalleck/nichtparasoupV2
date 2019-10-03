__all__ = ['NichtParasoupTest']

import unittest
import ddt

from nichtparasoup.nichtparasoup import NichtParasoup

from nichtparasoup.crawler import Crawler


@ddt.ddt
class NichtParasoupTest(unittest.TestCase):

    @ddt.data('dummy')
    def test_add_crawler_site(self, crawler: str):
        # arrange
        nichtparasoup = NichtParasoup()
        crawlers = nichtparasoup.crawlers

        # act
        nichtparasoup._add_crawler_site(crawler, 'test')

        # assert
        self.assertEqual(len(crawlers), 1, 'unexpected crawler count')
        self.assertEqual(crawlers[0][0].__class__.__name__.lower(), crawler.lower(), 'unexpected crawler class')

    def test_add_crawler_object(self):
        # arrange
        crawler = Crawler('test')
        nichtparasoup = NichtParasoup()
        crawlers = nichtparasoup.crawlers

        # act
        nichtparasoup._add_crawler_object(crawler)

        # assert
        self.assertEqual(len(crawlers), 1, 'unexpected crawler count')
        self.assertEqual(crawlers[0][0], crawler, 'unexpected crawler object')
