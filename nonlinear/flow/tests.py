from django.test import TestCase

from .models import Image, Post, News, Comment, Album, Order
# Create your tests here.


class NewsTest(TestCase):
    def test_comments_to_posts(self):
        post_1 = Post(title="news article 1")
        post_2 = Post(title="news article 2")
        comment_1 = Comment(title="Test comment 1")
        comment_2 = Comment(title="Test comment 2")
        comment_1.post = post_1
        comment_2.post = post_2
        self.assertIs(comment_1.post == post_1, True)
        self.assertIs(comment_2.post == post_2, True)

