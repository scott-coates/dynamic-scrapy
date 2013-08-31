from django.contrib import admin
from scrapy_test.aggregates.apartment.models import Apartment, Amenity
from scrapy_test.aggregates.listing.models import Listing


class ListingInline(admin.TabularInline):
  model = Listing
  max_num = 0


class AmenityInline(admin.StackedInline):
  model = Amenity
  max_num = 0


class ApartmentAdmin(admin.ModelAdmin):
  inlines = [
    ListingInline,
    AmenityInline,
  ]


admin.site.register(Apartment, ApartmentAdmin)
