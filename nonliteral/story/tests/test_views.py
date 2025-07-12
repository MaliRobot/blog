# story/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from story.models import Chapter, Choice, ReaderUser, UserProgress


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.chapter1 = Chapter.objects.create(
            title="The Beginning",
            text="You wake up in a mysterious forest...",
            is_terminal=False
        )
        self.chapter2 = Chapter.objects.create(
            title="The Middle",
            text="You continue your journey...",
            is_terminal=False
        )
        self.terminal_chapter = Chapter.objects.create(
            title="The End",
            text="Your adventure concludes here.",
            is_terminal=True
        )

        self.reader = ReaderUser.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            current_chapter=self.chapter1
        )
        self.reader.set_password("testpassword")
        self.reader.save()

        self.choice = Choice.objects.create(
            name="Go forward",
            description="Continue deeper into the forest",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=10,
            energy_cost=5
        )


class HomeViewTest(ViewTestCase):
    def test_home_view(self):
        response = self.client.get(reverse('story:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Story Adventure")

    def test_home_view_with_logged_in_reader(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome back")


class ReaderAuthViewTest(ViewTestCase):
    def test_reader_login_get(self):
        response = self.client.get(reverse('story:reader_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reader Login")

    def test_reader_login_post_success(self):
        response = self.client.post(reverse('story:reader_login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

        # Check session
        self.assertIn('reader_user_id', self.client.session)
        self.assertEqual(self.client.session['reader_user_id'], self.reader.id)

    def test_reader_login_post_failure(self):
        response = self.client.post(reverse('story:reader_login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Stay on login page
        self.assertContains(response, "Invalid username or password")

    def test_reader_signup_get(self):
        response = self.client.get(reverse('story:reader_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Reader Account")

    def test_reader_signup_post_success(self):
        response = self.client.post(reverse('story:reader_signup'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after signup

        # Check user was created
        new_reader = ReaderUser.objects.get(username='newuser')
        self.assertEqual(new_reader.email, 'new@example.com')

        # Check logged in
        self.assertIn('reader_user_id', self.client.session)

    def test_reader_logout(self):
        # Login first
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:reader_logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertNotIn('reader_user_id', self.client.session)


class DashboardViewTest(ViewTestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('story:dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_dashboard_with_login(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, Test User")
        self.assertContains(response, "Money: 100")
        self.assertContains(response, "Energy: 100")


class ChapterDetailViewTest(ViewTestCase):
    def test_chapter_detail_requires_login(self):
        response = self.client.get(reverse('story:chapter_detail'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_chapter_detail_with_login(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:chapter_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.chapter1.title)
        self.assertContains(response, self.chapter1.text)
        self.assertContains(response, self.choice.name)

    def test_chapter_detail_specific_chapter(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(
            reverse('story:chapter_detail', kwargs={'chapter_id': self.chapter2.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.chapter2.title)


class MakeChoiceViewTest(ViewTestCase):
    def test_make_choice_requires_login(self):
        response = self.client.post(reverse('story:make_choice'), {
            'choice_id': self.choice.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_make_choice_success(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        # Check initial stats
        self.assertEqual(self.reader.money, 100)
        self.assertEqual(self.reader.energy, 100)
        self.assertEqual(self.reader.current_chapter, self.chapter1)

        response = self.client.post(reverse('story:make_choice'), {
            'choice_id': self.choice.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after choice

        # Refresh reader from database
        self.reader.refresh_from_db()

        # Check stats changed
        self.assertEqual(self.reader.money, 90)  # 100 - 10
        self.assertEqual(self.reader.energy, 95)  # 100 - 5
        self.assertEqual(self.reader.current_chapter, self.chapter2)

        # Check progress was recorded
        progress = UserProgress.objects.filter(reader=self.reader).first()
        self.assertIsNotNone(progress)
        self.assertEqual(progress.choice_made, self.choice)

    def test_make_choice_insufficient_resources(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        # Create expensive choice
        expensive_choice = Choice.objects.create(
            name="Expensive choice",
            from_chapter=self.chapter1,
            to_chapter=self.chapter2,
            money_cost=200,  # More than reader has
            energy_cost=5
        )

        response = self.client.post(reverse('story:make_choice'), {
            'choice_id': expensive_choice.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect

        # Stats should not change
        self.reader.refresh_from_db()
        self.assertEqual(self.reader.money, 100)
        self.assertEqual(self.reader.current_chapter, self.chapter1)


class RestartStoryViewTest(ViewTestCase):
    def test_restart_get(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:restart'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure")

    def test_restart_post(self):
        # Login reader and modify stats
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        self.reader.money = 50
        self.reader.energy = 30
        self.reader.current_chapter = self.chapter2
        self.reader.save()

        response = self.client.post(reverse('story:restart'))
        self.assertEqual(response.status_code, 302)  # Redirect

        # Check stats reset
        self.reader.refresh_from_db()
        self.assertEqual(self.reader.money, 100)
        self.assertEqual(self.reader.energy, 100)
        self.assertEqual(self.reader.current_chapter, self.chapter1)


class ProgressHistoryViewTest(ViewTestCase):
    def test_progress_history_requires_login(self):
        response = self.client.get(reverse('story:progress_history'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_progress_history_with_progress(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        # Create some progress
        UserProgress.objects.create(
            reader=self.reader,
            chapter=self.chapter1,
            choice_made=self.choice
        )

        response = self.client.get(reverse('story:progress_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Adventure History")
        self.assertContains(response, self.choice.name)


class APIViewTest(ViewTestCase):
    def test_api_reader_stats(self):
        # Login reader
        session = self.client.session
        session['reader_user_id'] = self.reader.id
        session.save()

        response = self.client.get(reverse('story:api_reader_stats'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['money'], 100)
        self.assertEqual(data['energy'], 100)
        self.assertEqual(data['current_chapter'], self.chapter1.title)
