import unittest

from nichtparasoup.nichtparasoup import NichtParasoup
from nichtparasoup.crawler import Images, Image, ImageCrawler


class _EmptyImageCrawler(ImageCrawler):
    """ a crawler that finds nothing. use it for mocking ... """

    def crawl(self) -> Images:
        return Images()


class NichtParasoupTest(unittest.TestCase):

    def test__is_image_not_in_blacklist(self) -> None:
        # arrange
        image1 = Image("test1")
        image2 = Image("test2")
        nichtparasoup = NichtParasoup()

        # act
        nichtparasoup.blacklist.add(image1.uri)

        # assert
        self.assertTrue(nichtparasoup._is_image_not_in_blacklist(image2))
        self.assertFalse(nichtparasoup._is_image_not_in_blacklist(image1))

    def test__add_image_to_blacklist(self) -> None:
        # arrange
        image1 = Image("test1")
        image2 = Image("test2")
        nichtparasoup = NichtParasoup()

        # act
        nichtparasoup._add_image_to_blacklist(image1)

        # assert
        self.assertIn(image1.uri, nichtparasoup.blacklist)
        self.assertNotIn(image2.uri, nichtparasoup.blacklist)

    def test_add_imagerawler(self) -> None:
        # arrange
        nichtparasoup = NichtParasoup()
        imagecrawler = _EmptyImageCrawler("test")

        # act
        nichtparasoup.add_imagerawler(imagecrawler, 1)

        # assert
        self.assertIn(imagecrawler, [crawler.imagecrawler for crawler in nichtparasoup.crawlers])

    def test_get_random_image(self) -> None:
        # arrange
        imagecrawler = _EmptyImageCrawler("test")

        nichtparasoup_no_crawler = NichtParasoup()

        nichtparasoup_empty_crawler = NichtParasoup()
        nichtparasoup_empty_crawler.add_imagerawler(imagecrawler, 1)

        nichtparasoup_filled_crawler = NichtParasoup()
        nichtparasoup_filled_crawler.add_imagerawler(imagecrawler, 1)
        image_in_filled_crawler = Image('test')
        list(nichtparasoup_filled_crawler.crawlers)[0].images.add(image_in_filled_crawler)

        # act
        image_from_no_crawler = nichtparasoup_no_crawler.get_random_image()
        image_from_empty_crawler = nichtparasoup_empty_crawler.get_random_image()
        image_from_filled_crawler = nichtparasoup_filled_crawler.get_random_image()

        # assert
        self.assertIsNone(image_from_no_crawler, 'expected no image from an empty crawler set')
        self.assertIsNone(image_from_empty_crawler, 'expected no image from an empty image set')
        self.assertIs(image_from_filled_crawler, image_in_filled_crawler, 'expected the one image that was available')
