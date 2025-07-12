# story/tests/test_models.py
from django.test import TestCase
from django.core.exceptions import ValidationError

from story.models import Chapter, Choice, ReaderUser, UserProgress, ChapterConnection


class ChapterModelTest(TestCase):
    def setUp(self):
        self.chapter1 = Chapter.objects.create(
            title="The Beginning",
            text="You wake up in a mysterious forest...",
            is_terminal=False
        )
        self.chapter2 = Chapter.objects.create(
            title="The End",
            text="Your adventure concludes here.",
            is_terminal=True
        )

    def test_chapter_creation(self):
        self.assertEqual(self.chapter1.title, "The Beginning")
        self.assertFalse(self.chapter1.is_terminal)
        self.assertTrue(self.chapter2.is_terminal)
        self.assertIsNotNone(self.chapter1.date_created)

    def test_chapter_str(self):
        self.assertEqual(str(self.chapter1), "The Beginning")

    def test_get_choices(self):
        choice = Choice.objects.create(
            name="Go left",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=10,
            energy_cost=5
        )
        choices = self.chapter1.get_choices()
        self.assertIn(choice, choices)

    def test_get_available_choices(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            money=50,
            energy=30
        )
        reader.set_password("testpass")

        # Affordable choice
        affordable_choice = Choice.objects.create(
            name="Affordable path",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=10,
            energy_cost=5
        )

        # Expensive choice
        expensive_choice = Choice.objects.create(
            name="Expensive path",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=100,
            energy_cost=50
        )

        available = self.chapter1.get_available_choices(reader)
        self.assertIn(affordable_choice, available)
        self.assertNotIn(expensive_choice, available)


class ChoiceModelTest(TestCase):
    def setUp(self):
        self.chapter1 = Chapter.objects.create(title="Start", text="Beginning")
        self.chapter2 = Chapter.objects.create(title="End", text="Ending")

    def test_choice_creation(self):
        choice = Choice.objects.create(
            name="Test Choice",
            description="A test choice",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=10,
            energy_cost=-5  # Gain energy
        )

        self.assertEqual(choice.name, "Test Choice")
        self.assertEqual(choice.money_cost, 10)
        self.assertEqual(choice.energy_cost, -5)

    def test_choice_str(self):
        choice = Choice.objects.create(
            name="Test Choice",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2
        )
        expected_str = f"Test Choice (from {self.chapter1.title})"
        self.assertEqual(str(choice), expected_str)


class ReaderUserModelTest(TestCase):
    def setUp(self):
        self.chapter = Chapter.objects.create(title="Test Chapter", text="Test")

    def test_reader_creation(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        reader.set_password("testpassword")

        self.assertEqual(reader.username, "testuser")
        self.assertEqual(reader.email, "test@example.com")
        self.assertEqual(reader.money, 100)  # Default value
        self.assertEqual(reader.energy, 100)  # Default value
        self.assertTrue(reader.is_active)

    def test_password_handling(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com"
        )
        reader.set_password("testpassword")

        self.assertTrue(reader.check_password("testpassword"))
        self.assertFalse(reader.check_password("wrongpassword"))

    def test_get_full_name(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="John",
            last_name="Doe"
        )
        self.assertEqual(reader.get_full_name(), "John Doe")

        # Test with empty names
        reader2 = ReaderUser.objects.create(
            username="testuser2",
            email="test2@example.com"
        )
        self.assertEqual(reader2.get_full_name(), "testuser2")

    def test_make_choice(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            money=100,
            energy=100,
            current_chapter=self.chapter
        )

        chapter2 = Chapter.objects.create(title="Next Chapter", text="Next")
        choice = Choice.objects.create(
            name="Test Choice",
            from_chapter=self.chapter,
            to_chapter=chapter2,
            money_cost=20,
            energy_cost=10
        )

        reader.make_choice(choice)

        self.assertEqual(reader.money, 80)
        self.assertEqual(reader.energy, 90)
        self.assertEqual(reader.current_chapter, chapter2)

    def test_can_make_choice(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            money=50,
            energy=30
        )

        chapter2 = Chapter.objects.create(title="Next", text="Next")

        # Affordable choice
        affordable_choice = Choice.objects.create(
            name="Affordable",
            from_chapter=self.chapter,
            to_chapter=chapter2,
            money_cost=10,
            energy_cost=5
        )

        # Expensive choice
        expensive_choice = Choice.objects.create(
            name="Expensive",
            from_chapter=self.chapter,
            to_chapter=chapter2,
            money_cost=100,
            energy_cost=50
        )

        self.assertTrue(reader.can_make_choice(affordable_choice))
        self.assertFalse(reader.can_make_choice(expensive_choice))

    def test_generate_session_token(self):
        reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com"
        )

        token = reader.generate_session_token()
        self.assertIsNotNone(token)
        self.assertEqual(reader.session_token, token)


class UserProgressModelTest(TestCase):
    def setUp(self):
        self.reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com"
        )
        self.chapter = Chapter.objects.create(title="Test Chapter", text="Test")
        self.chapter2 = Chapter.objects.create(title="Next Chapter", text="Next")
        self.choice = Choice.objects.create(
            name="Test Choice",
            from_chapter=self.chapter,
            to_chapter=self.chapter2
        )

    def test_progress_creation(self):
        progress = UserProgress.objects.create(
            reader=self.reader,
            chapter=self.chapter,
            choice_made=self.choice
        )

        self.assertEqual(progress.reader, self.reader)
        self.assertEqual(progress.chapter, self.chapter)
        self.assertEqual(progress.choice_made, self.choice)
        self.assertIsNotNone(progress.timestamp)


class ChapterConnectionModelTest(TestCase):
    def setUp(self):
        self.chapter1 = Chapter.objects.create(title="Chapter 1", text="First")
        self.chapter2 = Chapter.objects.create(title="Chapter 2", text="Second")

    def test_connection_creation(self):
        connection = ChapterConnection.objects.create(
            from_chapter=self.chapter1,
            to_chapter=self.chapter2
        )

        self.assertEqual(connection.from_chapter, self.chapter1)
        self.assertEqual(connection.to_chapter, self.chapter2)

    def test_unique_together_constraint(self):
        ChapterConnection.objects.create(
            from_chapter=self.chapter1,
            to_chapter=self.chapter2
        )

        # Try to create duplicate connection
        with self.assertRaises(Exception):  # Should raise IntegrityError
            ChapterConnection.objects.create(
                from_chapter=self.chapter1,
                to_chapter=self.chapter2
            )