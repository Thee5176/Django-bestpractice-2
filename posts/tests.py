from django.test import TestCase

from .models import Post
class PostTests(TestCase):
    """Model test"""
    @classmethod
    def setUpTestData(cls):
        """Store in class instance"""
        cls.post = Post.objects.create(text="This is a test.")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test.")