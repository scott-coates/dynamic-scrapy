import pytz

eastern_time_zone = pytz.timezone('US/Eastern')

# region result 1
search_1 = {
  'description': 'I want a great place to live',
  'specified_location': 'Astoria NY',
  'geo_boundary_points': [
    {'point_number': 1, 'lat': 40.78260179999999, 'lng': -73.90221819999999},
    {'point_number': 2, 'lat': 40.7489151, 'lng': -73.9520859},
    {'point_number': 3, 'lat': 40.7623925, 'lng': -73.9301037},
  ],
  'no_fee_preferred': True,
  'bedroom_max': 2,
  'bathroom_max': 1.5,
  'sqfeet_max': 850.50,
  'price_max': 2500.50,
  'amenities': [1, 2]
}

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
