from django.test import TestCase
from .forms import TicketForm


# Create your tests here.
class Test_Forms(TestCase):
    def test_valid_ticket_form(self):
        '''
        Makes sure the ticket form works if its valid
        '''
        form = TicketForm({"name": "Test Ticket",
                           "description": "this is a test"})
        self.assertTrue(form.is_valid())
