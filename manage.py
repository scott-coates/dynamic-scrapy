#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapy_test.settings.dev")
    os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "scrapy_test.apps.web_scraper.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
