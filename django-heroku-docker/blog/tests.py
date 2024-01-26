from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class RegisterCreateViewTest(TestCase):
    def test_create_user(self):
        url = reverse('sign-up')  # Use the reverse function with the name from your urlpatterns
        data = {
   "username": "testuser",
  "password": "string",
  "confirm_password": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class PostListViewTest(TestCase):
    def test_list_posts(self):
        url = reverse('post_list_view')  # Use the reverse function with the name from your urlpatterns

        # Assuming you have some posts in the database
        Post.objects.create(title='Post 1', content='Content 1')
        Post.objects.create(title='Post 2', content='Content 2')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
