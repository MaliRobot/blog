from django.test import TestCase
from django.urls import resolve
from rest_framework.test import APIClient
from datetime import datetime
import pytz

from news.models import News


# Create your tests here.
class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(
            title="test1",
            text="lorem ipsum",
            public=0,
            language='eng',
            image="/test",
            date_published=datetime.now(pytz.timezone("Europe/Zurich"))
        )

    def test_news_read(self):
        news = News.objects.get(title="test1")
        self.assertEqual(news.text, "lorem ipsum")

        resolver = resolve(f'/news/{news.id}/')
        self.assertEqual(resolver.kwargs['pk'], news.id)
        self.assertEqual(resolver.route, 'news/<int:pk>/')
        self.assertEqual(resolver.url_name, 'single_news')

    def test_api_news_get(self):
        client = APIClient()
        response = client.get('http://testserver/api/news/')
        assert response.status_code == 200
