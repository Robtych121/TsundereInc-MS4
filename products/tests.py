from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Product models
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


class Test_Pages(TestCase):
    def test_products_page(self):
        '''
        Checks if the store page loads the products template
        correctly
        '''
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
