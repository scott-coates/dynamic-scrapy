from django.contrib import admin
from scrapy_test.apps.web_scraper.models import ListingSourceScraperConfig, ListingCheckerConfig

admin.site.register(ListingSourceScraperConfig)
admin.site.register(ListingCheckerConfig)

