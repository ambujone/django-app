from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Menu
from .serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu model
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=120, Inventory=50)
        Menu.objects.create(Title="Burger", Price=90, Inventory=75)

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Create token for authentication
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        # Set up authentication credentials
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_getall(self):
        # Get API response
        # The URL for MenuItemsView is 'restaurant/menu/' based on urls.py
        response = self.client.get('/restaurant/menu/')

        # Get data from database
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
