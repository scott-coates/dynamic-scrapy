import datetime
import pytz

eastern_time_zone = pytz.timezone('US/Eastern')

# region cl_listing_3952467416
cl_listing_3952467416_description = [u'\n\t\tHOUSE FOR RENT IN GOOD LOCATION',
                                     u'\n3 BED ROOM LIVING ROOM DINING ROOM',
                                     u'\nNEW KITCHEN ', u'\nCALL DIANA 718-343-2739', u'\nNO BROKERS FEE\n\t']

cl_listing_3952467416_title = [u'\n  - $1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)\n']

cl_listing_3952467416_posted_date = [u'2013-08-07,  4:52PM EDT', u'2013-08-07,  4:52PM EDT']
cl_listing_3952467416_last_updated_date = [u'2013-07-22,  3:31PM EDT']

cl_listing_3952467416_expected_title = '$1750 / 3br - BEST AREA IN FAR ROCKAWAY (FAR ROCKAWAY)'
cl_listing_3952467416_expected_description = u'HOUSE FOR RENT IN GOOD LOCATION\n3 BED ROOM LIVING ROOM DINING ' \
                                             u'ROOM\nNEW KITCHEN \nCALL DIANA 718-343-2739\nNO BROKERS FEE'
cl_listing_3952467416_expected_posted_date = eastern_time_zone.localize(datetime.datetime(2013, 8, 7, 16, 52))
cl_listing_3952467416_expected_last_updated_date = eastern_time_zone.localize(datetime.datetime(2013, 7, 22, 15, 31))
#endregion

# region cl_listing_4033538277
cl_listing_4033538277 = {u'city': [u'brooklyn'], u'contact_phone_number': [u'bedstuy / clinton hill'],
                         u'description': [u'\n\t\tBeautiful 3 Bedroom 2 Full bath', u'\nAmazing Finishes',
                                          u'\nHuge Backyard',
                                          u'\n100% no fee By owner',
                                          u'\nAll Bedrooms can fit King and Queen sized beds',
                                          u'\nSteps to the G train', u'\nLaundry in the Building',
                                          u'\nClose to All your needs',
                                          u'\nNo brokers Please', u'\nCall or Text Danny @ 646 338 3852 ',
                                          u'\n3526+56+5\n\t'],
                         u'title': [
                           u'\n  - $2695 / 3br - 3 Bedroom 2 Full bath + Massive Backyard~Prime Location (bedstuy / '
                           u'clinton hill)\n'],
                         u'url': u'http://newyork.craigslist.org/brk/abo/4033538277.html', u'state': [u'ny'],
                         u'last_updated_date': [],
                         u'posted_date': [u'2013-08-29, 12:55PM EDT', u'2013-08-29, 12:55PM EDT'],
                         u'contact_email_address': [u'bedstuy / clinton hill'],
                         u'address': [u'vernon ave at nostrand', u'vernon ave', u'nostrand'], u'lat': [u'40.694263'],
                         'listing_source_id': 1,
                         u'lng': [u'-73.952341'], u'broker_fee': [u'/brk/abo/4033538277.html'],
                         u'contact_name': [u'bedstuy / clinton hill']}
#endregion
