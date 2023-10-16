from django.test import TestCase
from django.urls import reverse

from coreapp.models import Task
from coreapp import views

# Create your tests here.

class TaskModelTestCase(TestCase):
    
    def setUp(self):
        """ set up necessary data for tests"""
        Task.objects.create(title="test1")

    def test_is_important(self):
        test_task = Task.objects.get(title="test1")
        self.assertEqual(test_task.is_important, "False")


      
class ViewsTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        Task.objects.create(title="test1")

    def test_imptasks_response(self):
        # Test the view's response
        response = self.client.get(reverse('imp-tasks'))
        self.assertEqual(response.status_code, 200)

    # def test_view_context(self):
    #     # Test the context of the view
    #     response = self.client.get(reverse('your-view-name'))
    #     self.assertEqual(response.context['your_variable'], "Expected Value")
