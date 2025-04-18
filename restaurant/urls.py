from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

# Create a separate router for booking
booking_router = DefaultRouter()
booking_router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/', include(router.urls)),
    path('booking/', include(booking_router.urls)),
]