import unittest
from unittest.mock import MagicMock


from nichtparasoup.nichtparasoup import Crawler
from nichtparasoup.crawler import ImageCrawler, Images, Image


class CrawlerTest(unittest.TestCase):

    class ImageCrawlerForTesting(ImageCrawler):
        """ implementation for testing & mocking """
        def crawl(self) -> Images: pass

    def test_crawl(self):
        # arrange
        called_is_image_addable_with = Images()
        called_added_images_with = Images()

        images_addable = {
            Image('test1'): True,
            Image('test2'): False,
        }
        images = Images(images_addable.keys())

        def is_image_addable(crawled_image: Image) -> bool:
            # must be compatible to: _IsImageAddable
            called_is_image_addable_with.add(crawled_image)
            return images_addable[crawled_image]

        def on_image_added(crawled_image: Image):
            # must be compatible to: _OnImageAdded
            called_added_images_with.add(crawled_image)
            pass

        imagecrawler = self.ImageCrawlerForTesting('test')
        imagecrawler.crawl = MagicMock(return_value=images)
        crawler = Crawler(imagecrawler, 1, is_image_addable, on_image_added)

        # act
        crawler.crawl()

        # assert
        self.assertSetEqual(
            called_is_image_addable_with,
            images,
            'called is_image_addable() wrong'
        )
        self.assertSetEqual(
            called_added_images_with,
            Images(image for (image, addable) in images_addable.items() if addable),
            'called added_images() wrong'
        )
        self.assertSetEqual(
            crawler.images,
            set(called_added_images_with),
            'added images wrong'
        )
