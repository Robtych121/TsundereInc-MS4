from django.test import TestCase


# Create your tests here.
class Test_Pages(TestCase):
    def test_home_page(self):
        '''
        Checks if the home page loads the homepage template
        correctly
        '''
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "homepage.html")
