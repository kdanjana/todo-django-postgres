from django.test import TestCase

from coreapp.models import Task

# Create your tests here.

class TasTestCase(TestCase):
    
    def setUp(self):
        """ set up necessary data for tests"""
        Task.objects.create(title="test1")

    def test_is_important(self):
        test_task = Task.objects.get(title="test1")
        self.assertEqual(test_task.is_important, "False")