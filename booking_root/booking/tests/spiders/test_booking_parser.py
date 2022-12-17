import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import unittest
from ..helpers import fake_response_from_file
from scrapy.utils.test import get_crawler
from spiders.booking_parser import BookingParserSpider

class TestBookingParser(unittest.TestCase):
    to_test = BookingParserSpider.from_crawler(get_crawler())

    def test_is_not_valid_content(self):
        response = fake_response_from_file('samples/invalid_booking_response.html')
        self.assertFalse(self.to_test._is_valid_content(response))
    
    def test_is_valid_content(self):
        response = fake_response_from_file('samples/valid_booking_response.html')
        self.assertTrue(self.to_test._is_valid_content(response))
    
    def test__get_rooms_categories(self):
        response = fake_response_from_file('samples/valid_booking_response.html')
        rooms = self.to_test._get_rooms_categories(response.xpath('//table[@id="maxotel_rooms"]/tbody/tr'))
        self.assertEqual(len(rooms), 7)

    def test__get_alt_hotels(self):
        response = fake_response_from_file('samples/valid_booking_response.html')
        rooms = self.to_test._get_alt_hotels(response.xpath('//table[@id="althotelsTable"]/tbody/tr/td'))
        self.assertEqual(len(rooms), 4)

if __name__ == '__main__':
    unittest.main()
