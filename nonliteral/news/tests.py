from django.test import TestCase
from news.models import News

import datetime


# Create your tests here.
class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(
            title="test1",
            text="lorem ipsum",
            public=0,
            language='eng',
            image="/test",
            date_published=datetime.date.today()
        )

    def test_news_read(self):
        news = News.objects.get(title="test1")
        self.assertEqual(news.text, "lorem ipsum")
