from django.test import TestCase, SimpleTestCase
from .models import Notee
from django.urls import reverse

class HomePageViewTest(TestCase):

    def setUp(self):
        Notee.objects.create(text='another text')

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

    def setUp(self):
        Notee.objects.create(text='just a test')

    def test_post_content(self):
        note = Notee.objects.get(id=1)
        excepted_object_name = f'{note.text}'
        self.assertEqual(excepted_object_name, 'just a test')