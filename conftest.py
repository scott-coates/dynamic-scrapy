import os

#set the DJ settings module: http://pytest-django.readthedocs.org/en/latest/configuring_django.html#using-django-configurations
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapy_test.settings.dev")

#this line is required in order to use the db_with_migrations fixture
#http://pytest.org/latest/plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file
pytest_plugins = "scrapy_test.libs.django_utils.testing.utils"
