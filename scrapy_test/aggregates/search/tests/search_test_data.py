import pytz

eastern_time_zone = pytz.timezone('US/Eastern')

# region search 1
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
search_1_expected_lat = 40.7623925
search_1_expected_lng = -73.9301037

#endregion
