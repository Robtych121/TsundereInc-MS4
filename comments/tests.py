from django.test import TestCase
from .forms import CommentForm


# Create your tests here.
class Test_Forms(TestCase):
    def test_valid_comment_form(self):
        '''
        Makes sure the comment form works if its valid
        '''
        form = CommentForm({"content": "User"})
        self.assertTrue(form.is_valid())
