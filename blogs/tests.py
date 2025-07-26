from django.test import TestCase
from .models import Blog


# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        blog = Blog.objects.create(
            id=1, title="Test Title", author="Madu", content="This just a test."
        )

    def test_viewa_index(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.title, "Test Title")
        self.assertEqual(blog.author, "Madu")
