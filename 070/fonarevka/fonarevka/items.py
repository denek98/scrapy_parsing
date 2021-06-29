# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join


class FonarevkaItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    image = scrapy.Field(output_processor = Join(','))
    # brand = scrapy.Field()
    # name = scrapy.Field()

