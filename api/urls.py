# urls.py
from django.urls import path
from .views import ShortURLDetailView

urlpatterns = [
    path('shorturl/<str:short_code>/', ShortURLDetailView.as_view(), name='shorturl-detail'),
    path('shorturl/pk/<int:pk>/', ShortURLDetailView.as_view(), name='shorturl-by-pk'),
    path('shorturl/', ShortURLDetailView.as_view(), name='shorturl-create'),
]
