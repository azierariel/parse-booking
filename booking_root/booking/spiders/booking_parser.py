import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import scrapy
import logging

from helpers import preprocess
from task_loader import load_tasks
from items import BookingItem


class BookingParserSpider(scrapy.Spider):
    name = "booking-parser"

    def start_requests(self):
        logging.info("searching bucket for tasks ...")
        tasks = load_tasks(self.settings.get("TASKS_STORAGE_BUCKET",""))
        for task in tasks:
            url = self.settings.get("TASKS_STORAGE_BUCKET") + task['name']
            yield scrapy.Request(url)

    def parse(self, response):
        if self._is_valid_content(response):
            item = BookingItem()
            item["hotel_name"] = preprocess(
                response.xpath('//*[@class="details"]/h3/text()').extract()
            )
            item["address"] = preprocess(
                response.xpath('//*[@id="hp_address_subtitle"]/text()').extract()
            )
            item["review_points"] = preprocess(
                response.xpath(
                    '//*[@id="hotel_main_content"]//*[@class="average js--hp-scorecard-scoreval"]/text()'
                ).extract()
            )
            item["number_of_reviews"] = preprocess(
                response.xpath(
                    '//*[@id="hotel_main_content"]//*[@class="trackit score_from_number_of_reviews"]/strong[@class="count"]/text()'
                ).extract()
            )
            item["description"] = preprocess(
                response.xpath(
                    '//*[@class="hotel_description_wrapper_exp "]//p/text()'
                ).extract()
            )
            item["rooms"] = self._get_rooms_categories(
                response.xpath('//table[@id="maxotel_rooms"]/tbody/tr')
            )
            item["alt_hotels"] = self._get_alt_hotels(
                response.xpath('//table[@id="althotelsTable"]/tbody/tr/td')
            )

            return item
        else:
            logging.error(f"{response.url.split('/')[-1]} doesn't contain valid data.")


    def _get_rooms_categories(self, selector):
        rooms = []
        sequence = 0
        for room in selector:
            sequence += 1
            rooms.append(
                {
                    "room_type": preprocess(
                        room.xpath('./td[@class="ftd"]/text()').extract()
                    ),
                    "standard_occupancy": preprocess(
                        room.xpath("./td/i/@title | ./td/span/i/@title").extract()
                    ),
                    "sequence": sequence,
                }
            )
        return rooms

    def _get_alt_hotels(self, selector):
        hotels = []
        sequence = 0
        for hotel in selector:
            sequence += 1
            hotels.append(
                {
                    "alt_hotel_name": preprocess(
                        hotel.xpath('./p[@class="althotels-name"]/a/text()').extract()
                    ),
                    "alt_hotel_url": preprocess(
                        hotel.xpath('./p/a[@class="althotel_link"]/@href').extract()
                    ),
                    "sequence": sequence,
                }
            )
        return hotels

    def _is_valid_content(self, response):
        return len(response.xpath('//*[@class="details"]/h3/text()').extract()) > 0
