from django.test import TestCase
from django.urls import resolve
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import datetime
import pytz

from poems.models import Poem


# Create your tests here.
class PoemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        Poem.objects.create(
            title="test1",
            text="lorem ipsum",
            public=0,
            date_created=datetime.now(pytz.timezone('Europe/Zurich')),
            author_id=user.id,
        )

    def test_poem_read(self):
        poem = Poem.objects.get(title="test1")
        self.assertEqual(poem.text, "lorem ipsum")

        resolver = resolve("/poetry/")
        self.assertEqual(resolver.route, 'poetry/')
        self.assertEqual(resolver.url_name, 'poems')

    def test_api_get(self):
        client = APIClient()
        response = client.get('http://testserver/api/poems/')
        assert response.status_code == 200
