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
