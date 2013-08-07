from django.test import SimpleTestCase
from django.db import models
from scrapy_test.libs.django_utils.models.utils import copy_django_model_attrs


class UtilsTestCase(SimpleTestCase):
  class TestModel(models.Model):
    title = models.TextField()

  def setUp(self):
    self.test_model = UtilsTestCase.TestModel()

  def test_copy_django_model_attrs_copies_correct_attribute(self):
    title = 'hi'
    attrs = {'title': title}
    copy_django_model_attrs(self.test_model, **attrs)
    self.assertEqual(title, self.test_model.title)

