from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        # Allow GET requests without authentication
        if self.request.method == 'GET':
            return []
        # Require authentication for other methods (POST, etc.)
        return [IsAuthenticated()]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        # Allow GET requests without authentication
        if self.request.method == 'GET':
            return []
        # Require authentication for other methods (PUT, PATCH, DELETE, etc.)
        return [IsAuthenticated()]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
