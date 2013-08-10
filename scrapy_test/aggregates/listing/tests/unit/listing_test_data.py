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
#endregion

#region cl_listing_3952467416
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
#endregion
