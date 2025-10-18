from django.test import TestCase
# from django.contrib.auth.models import User
from .models import User,OrderItem,Order 
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class UserOrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1',password='testuser1')
        user2 = User.objects.create_user(username='user2',password='testuser2')
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)
    def test_user_order(self):
        user = User.objects.get(username='user2')
        self.client.force_login(user)    
        response = self.client.get(reverse('user-orders'))
        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(order['user']== user.id for order in orders))
        # print(f"ID: ::{data} \n" )
        # return super().setUp()
    def test_anonymous_user_order(self):
        response = self.client.get(reverse('user-orders'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # return super().setUp()
