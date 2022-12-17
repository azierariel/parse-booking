# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_name = scrapy.Field()
    address = scrapy.Field()
    review_points = scrapy.Field()
    number_of_reviews = scrapy.Field()
    description = scrapy.Field()
    rooms = scrapy.Field()
    alt_hotels = scrapy.Field()
