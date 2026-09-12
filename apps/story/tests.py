from django.test import TestCase
from apps.story.models import Chapter, Choice, ReaderUser


class ModelTestCase(TestCase):
    def setUp(self):
        self.node = Chapter.objects.create(title='Test Node', text='Test Text')
        self.target_node = Chapter.objects.create(title='Target Node', text='Target Text')
        self.choice = Choice.objects.create(
            text='Test Choice', 
            money_cost=-50, 
            energy_cost=-50, 
            from_chapter=self.node,
            to_chapter=self.target_node
        )
        self.user = ReaderUser.objects.create(username='testuser', energy=100, money=100, current_chapter=self.node)

    def test_node_choice_connection(self):
        node = Chapter.objects.get(title='Test Node')
        choice = Choice.objects.get(text='Test Choice')
        self.assertIn(choice, node.get_choices())

    def test_node_creation(self):
        node1 = Chapter.objects.create(title='Test Node 1', text='Test Text 1')
        self.assertEqual(node1.title, 'Test Node 1')

    def tearDown(self):
        Chapter.objects.all().delete()
        ReaderUser.objects.all().delete()

    def test_choice_creation(self):
        choice = Choice.objects.get(text='Test Choice')
        self.assertEqual(choice.money_cost, -50)
        self.assertEqual(choice.energy_cost, -50)

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