from fonarevka.items import FonarevkaItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
import scrapy
import json

class A070Spider(scrapy.Spider):
    name = '070'

    with open("links.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]


    def parse(self, response):


        data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        l = ItemLoader(item = FonarevkaItem(), selector = response)
        l.default_output_processor = TakeFirst()
        l.default_input_processor = MapCompose(str.strip)

        l.add_value('link',response.request.url)
        l.add_xpath('image', '//div[@id="productGalleryContent"]//ul//picture/source[2]/@data-href')
        # l.add_xpath('brand','//div[@class="characteristics-title"][contains(text(),"Производитель")]/../div[2]/a/text()')
        # l.add_xpath('name','//h1[@class="page-title"]/text()')


        yield {
        'image': ",".join(data['image']),
        "link": response.request.url,
        }
