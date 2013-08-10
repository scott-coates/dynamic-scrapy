import datetime
import pytz
from dateutil.tz import tzlocal

eastern_time_zone = pytz.timezone('US/Eastern')

# region cl_listing_3952467416
cl_listing_3952467416 = {u'city': [], u'contact_phone_number': [u'\n\t\tHOUSE FOR RENT IN GOOD LOCATION',
                                                                u'\n3 BED ROOM LIVING ROOM DINING ROOM',
                                                                u'\nNEW KITCHEN ',
                                                                u'\nCALL DIANA 718-343-2739', u'\nNO BROKERS FEE\n\t',
                                                                u'Listed By: PRIVATE DEVELOPMENT'],
                         u'description': [u'\n\t\tHOUSE FOR RENT IN GOOD LOCATION',
                                          u'\n3 BED ROOM LIVING ROOM DINING ROOM',
                                          u'\nNEW KITCHEN ', u'\nCALL DIANA 718-343-2739', u'\nNO BROKERS FEE\n\t'],
                         u'title': [u'\n  - $1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)\n'],
                         u'url': u'http://newyork.craigslist.org/que/abo/3952467416.html', u'address1': [],
                         u'price': [u'\n  - $1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)\n'], u'state': [],
                         u'posted_date': [u'2013-08-07,  4:52PM EDT', u'2013-08-07,  4:52PM EDT'],
                         u'last_updated_date': [u'2013-07-22,  3:31PM EDT'],
                         u'contact_email': [u'\n\t\tHOUSE FOR RENT IN GOOD LOCATION',
                                            u'\n3 BED ROOM LIVING ROOM DINING ROOM',
                                            u'\nNEW KITCHEN ', u'\nCALL DIANA 718-343-2739', u'\nNO BROKERS FEE\n\t',
                                            u'Listed By: PRIVATE DEVELOPMENT'], u'lng': [], 'listing_source_id': 1,
                         u'lat': [],
                         u'bedroom_count': [u'\n  - $1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)\n'],
                         u'contact_name': [u'\n\t\tHOUSE FOR RENT IN GOOD LOCATION',
                                           u'\n3 BED ROOM LIVING ROOM DINING ROOM',
                                           u'\nNEW KITCHEN ', u'\nCALL DIANA 718-343-2739', u'\nNO BROKERS FEE\n\t',
                                           u'Listed By: PRIVATE DEVELOPMENT'],
                         u'broker_fee': [u'/que/abo/3952467416.html'],
                         u'sqfeet': [u'\n  - $1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)\n']}

cl_listing_3952467416_expected_title = '$1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)'
cl_listing_3952467416_expected_description = u'HOUSE FOR RENT IN GOOD LOCATION\n3 BED ROOM LIVING ROOM DINING ROOM\nNEW KITCHEN \nCALL DIANA 718-343-2739\nNO BROKERS FEE'
cl_listing_3952467416_expected_posted_date = eastern_time_zone.localize(datetime.datetime(2013, 8, 7, 16, 52))
cl_listing_3952467416_expected_last_updated_date = eastern_time_zone.localize(datetime.datetime(2013, 7, 22, 15, 31))
#endregion


# region cl_listing_3970405942
cl_listing_3970405942 = {u'city': [u'Bronx'], u'contact_phone_number': [
  u'\n\t\t3 Bedroom Apartment with 2 Full Bath (full bath in Master Bedroom)',
  u'\nSpacious Living Room & Dining Room. Brand New Granite Kitchen with Stainless Steel Appliances. Hardwood Floors '
  u'All Throughout Apartment',
  u'\n------Section 8 OK ', u'\n------Available 9/1/13', u'\nWALK DISTANCE TO #2 & #5 TRAINS ',
  u'\n3 Brand New Gas Boilers & Hot Water Tanks. Massive Backyard. Near Shopping & Schools. ',
  u'\nCALL 917-417-7648 (Se Habla Espanol) ', u'Listed By: Jose Rodriguez, Inc'],
                         u'description': [u'\n\t\t3 Bedroom Apartment with 2 Full Bath (full bath in Master Bedroom)',
                                          u'\nSpacious Living Room & Dining Room. Brand New Granite Kitchen with '
                                          u'Stainless Steel Appliances. Hardwood Floors All Throughout Apartment',
                                          u'\n------Section 8 OK ', u'\n------Available 9/1/13',
                                          u'\nWALK DISTANCE TO #2 & #5 TRAINS ',
                                          u'\n3 Brand New Gas Boilers & Hot Water Tanks. Massive Backyard. Near '
                                          u'Shopping & Schools. ',
                                          u'\nCALL 917-417-7648 (Se Habla Espanol) '],
                         u'title': [u'\n  - $1850 / 3br - 3 Bedroom 2 Full Bath Luxury Apartment (Bronx, NY)\n'],
                         u'url': u'http://newyork.craigslist.org/brx/abo/3970405942.html',
                         u'address1': [u'Bristow St', u'Union'],
                         u'price': [u'\n  - $1850 / 3br - 3 Bedroom 2 Full Bath Luxury Apartment (Bronx, NY)\n'],
                         u'state': [u'NY'], u'last_updated_date': [u'2013-08-10,  6:19PM EDT'],
                         u'posted_date': [u'2013-07-30,  7:38PM EDT', u'2013-07-30,  7:38PM EDT'],
                         u'contact_email': [u'\n\t\t3 Bedroom Apartment with 2 Full Bath (full bath in Master Bedroom)',
                                            u'\nSpacious Living Room & Dining Room. Brand New Granite Kitchen with '
                                            u'Stainless Steel Appliances. Hardwood Floors All Throughout Apartment',
                                            u'\n------Section 8 OK ', u'\n------Available 9/1/13',
                                            u'\nWALK DISTANCE TO #2 & #5 TRAINS ',
                                            u'\n3 Brand New Gas Boilers & Hot Water Tanks. Massive Backyard. Near '
                                            u'Shopping & Schools. ',
                                            u'\nCALL 917-417-7648 (Se Habla Espanol) ',
                                            u'Listed By: Jose Rodriguez, Inc'],
                         u'contact_name': [u'\n\t\t3 Bedroom Apartment with 2 Full Bath (full bath in Master Bedroom)',
                                           u'\nSpacious Living Room & Dining Room. Brand New Granite Kitchen with Stainless Steel Appliances. Hardwood Floors All Throughout Apartment',
                                           u'\n------Section 8 OK ', u'\n------Available 9/1/13',
                                           u'\nWALK DISTANCE TO #2 & #5 TRAINS ',
                                           u'\n3 Brand New Gas Boilers & Hot Water Tanks. Massive Backyard. Near Shopping & Schools. ',
                                           u'\nCALL 917-417-7648 (Se Habla Espanol) ',
                                           u'Listed By: Jose Rodriguez, Inc'], 'listing_source_id': 1, u'lat': [],
                         u'bedroom_count': [
                           u'\n  - $1850 / 3br - 3 Bedroom 2 Full Bath Luxury Apartment (Bronx, NY)\n'], u'lng': [],
                         u'broker_fee': [u'/brx/abo/3970405942.html'],
                         u'sqfeet': [u'\n  - $1850 / 3br - 3 Bedroom 2 Full Bath Luxury Apartment (Bronx, NY)\n']}
#endregion
