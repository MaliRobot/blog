from django.test import TestCase
from story.models import Chapter, Choice, ReaderUser


class ModelTestCase(TestCase):
    def setUp(self):
        self.node = Chapter.objects.create(title='Test Node', text='Test Text')
        self.choice = Choice.objects.create(name='Test Choice', money=50, energy=50, node=self.node)
        self.user = ReaderUser.objects.create(username='testuser', energy=100, money=100, current_node=self.node)

    def test_node_choice_connection(self):
        node = Chapter.objects.get(title='Test Node')
        choice = Choice.objects.get(name='Test Choice')
        self.assertIn(choice, node.get_choices())

    def test_node_creation(self):
        node1 = Chapter.objects.create(title='Test Node 1', text='Test Text 1')
        node2 = Chapter.objects.create(title='Test Node 2', text='Test Text 2')
        node1.connections.add(node2)
        self.assertIn(node2, node1.connections.all())

    def tearDown(self):
        self.node.delete()
        self.choice.delete()
        self.user.delete()

    def test_choice_creation(self):
        choice = Choice.objects.get(name='Test Choice')
        self.assertEqual(choice.money, 50)
        self.assertEqual(choice.energy, 50)

    def test_reader_user_creation(self):
        user = ReaderUser.objects.get(username='testuser')
        self.assertEqual(user.energy, 100)
        self.assertEqual(user.money, 100)

    def test_get_choices(self):
        choices = self.node.get_choices()
        self.assertIn(self.choice, choices)

    def test_get_available_choices(self):
        available_choices = self.node.get_available_choices(self.user)
        self.assertIn(self.choice, available_choices)