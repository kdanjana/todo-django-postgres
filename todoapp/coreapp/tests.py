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
        self.assertEqual(test_task.is_important, False)
        self.assertEqual(test_task.is_complete, False)

      
class ViewsTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        Task.objects.create(title="test1")
        Task.objects.create(title="test2", is_important=True)
        Task.objects.create(title="test3")

    def test_imptasks_response(self):
        # Test the view's response
        number_imp_tasks = len(Task.objects.filter(is_important=True))
        response = self.client.get(reverse('coreapp:imp-tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['tasks_list']), number_imp_tasks)


    def test_donetask_response(self):
        # Test the done task view
        url = reverse('coreapp:done-task', args=[3])
        response = self.client.get(url)
        test_task = Task.objects.get(id=3)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(test_task.is_complete, True)
        self.assertEqual(Task.objects.get(title="test1").is_complete, False)
