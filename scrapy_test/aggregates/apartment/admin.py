from django.contrib import admin
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.listing.models import Listing


class ListingInline(admin.TabularInline):
  model = Listing


class AuthorAdmin(admin.ModelAdmin):
  inlines = [
    ListingInline,
  ]


admin.site.register(Apartment, AuthorAdmin)
