from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(name='John Doe', header='Test Header', text='Test Text')

    def test_post_content(self):
        # Retrieve the Post object created in setUpTestData
        post = Post.objects.get(id=1)
        # Verify the content of the post
        self.assertEqual(post.name, 'John Doe')
        self.assertEqual(post.header, 'Test Header')
        self.assertEqual(post.text, 'Test Text')
