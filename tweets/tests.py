from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import tweet

User=get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user=User.objects.create(username="Sahil Saini")

    def test_tweet_item(self):
        obj=tweet.objects.create(
            user=User.objects.first(),
            content="hey there"
        )


        self.assertTrue(obj.content=="hey there")
        self.assertTrue(obj.id==1)
        absolute_url=reverse("tweet:detail",kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)