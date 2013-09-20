import datetime
import json

from dateutil.tz import tzoffset
from scrapy_test.libs.django_utils.serialization.flexible_json_serializer import JSONSerializer
from scrapy_test.libs.django_utils.tests import FakeTestClass


def test_serializer_serializes_dict_with_model():
  serializer = JSONSerializer()
  test_class = FakeTestClass(name='Some Name', id=1, url='http://www.test.com', trusted_geo_data=False)
  dict_data = {'attrs': {'city': u'Brooklyn', 'posted_date': datetime.datetime(2013, 8, 29, 12, 55,
                                                                               tzinfo=tzoffset(u'EDT', -14400)),
                         'description': u'Beautiful 3 Bedroom 2 Full bath\n\nAmazing Finishes\n\nHuge '
                                        u'Backyard\n\n100% no fee By owner\n\nAll Bedrooms can fit King and Queen '
                                        u'sized beds\n\nSteps to the G train\n\nLaundry in the Building\n\nClose to '
                                        u'All your needs\n\nNo brokers Please\n\nCall or Text Danny @ 646 338 '
                                        u'3852\n\n3526+56+5',
                         'title': u'$2695 / 3br - 3 Bedroom 2 Full bath + Massive Backyard~Prime Location (bedstuy / '
                                  u'clinton hill)',
                         'url': u'http://newyork.craigslist.org/brk/abo/4033538277.html', 'broker_fee': False,
                         'price': 2695.0, 'state': u'NY', 'contact_phone_number': u'(646) 338-3852',
                         'address': u'Nostrand Avenue & Vernon Avenue', 'lat': 40.6942608, 'bedroom_count': 3,
                         'lng': -73.9523367,
                         'formatted_address': u'Nostrand Avenue & Vernon Avenue, Brooklyn, NY 11205, USA',
                         'contact_name': u'bedstuy / clinton hill', 'listing_source': test_class, 'zip_code': u'11205'}}

  serialized_data = serializer.serialize(dict_data)
  deserialized_data = json.loads(serialized_data)
  x = deserialized_data

def test_serializer_serializes_model_correctly():
  serializer = JSONSerializer()
  test_class = FakeTestClass(name='Some Name', id=1, url='http://www.test.com', trusted_geo_data=False)
  dict_data = {'test_model': test_class}

  serialized_data = serializer.serialize(dict_data)
  deserialized_data = json.loads(serialized_data)
  assert deserialized_data["test_model"]["model"] == u'unit.faketestclass'
