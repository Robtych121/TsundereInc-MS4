from django.test import TestCase
from .forms import ForumForm, CommentForm


# Create your tests here.
class Test_Pages(TestCase):
    def test_forum__page(self):
        '''
        Checks if the forum page loads the forum template
        correctly
        '''
        page = self.client.get("/forums/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forums.html")


class Test_Forms(TestCase):
    def test_valid_forum_form(self):
        '''
        Makes sure the form form works if its valid
        '''
        form = ForumForm({"name": "Test Post",
                          "description": "this is a forum post"})
        self.assertTrue(form.is_valid())

    def test_invalid_forum_form(self):
        '''
        Makes sure the login form shows error messages if its invalid
        '''
        form = ForumForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"],
                         [u"This field is required."])

    def test_valid_comment_form(self):
        '''
        Makes sure the comment form works if its valid
        '''
        form = CommentForm({"content": "User"})
        self.assertTrue(form.is_valid())
