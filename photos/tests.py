from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        self.sport = Category(name = 'Sport')

    def test_instance(self):
        self.assertTrue(isinstance(self.sport, Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_category(self):
        self.sport.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.sport.delete_category('Sport')
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

