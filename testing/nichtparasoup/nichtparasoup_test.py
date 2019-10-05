import unittest

from nichtparasoup.nichtparasoup import *
from nichtparasoup.crawler import ImageCrawler, Images, Image


class NichtParasoupTest(unittest.TestCase):
    class ImageCrawlerForTesting(ImageCrawler):
        """ implementation for testing & mocking """

        def crawl(self) -> Images: pass

    def test__is_image_not_in_blacklist(self):
        # arrange
        image1 = Image('test1')
        image2 = Image('test2')
        nichtparasoup = NichtParasoup()

        # act
        nichtparasoup.blacklist.add(image1.uri)

        # assert
        self.assertTrue(nichtparasoup._is_image_not_in_blacklist(image2))
        self.assertFalse(nichtparasoup._is_image_not_in_blacklist(image1))

    def test__add_image_to_blacklist(self):
        # arrange
        image1 = Image('test1')
        image2 = Image('test2')
        nichtparasoup = NichtParasoup()

        # act
        nichtparasoup._add_image_to_blacklist(image1)

        # assert
        self.assertIn(image1.uri, nichtparasoup.blacklist)
        self.assertNotIn(image2.uri, nichtparasoup.blacklist)

    def test_add_imagerawler(self):
        # arrange

        nichtparasoup = NichtParasoup()
        imagecrawler = self.ImageCrawlerForTesting('test')

        # act
        nichtparasoup.add_imagerawler(imagecrawler, 1)

        # assert
        self.assertIn(imagecrawler, [crawler.imagecrawler for crawler in nichtparasoup.crawlers])
