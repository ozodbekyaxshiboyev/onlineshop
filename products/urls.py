from django.urls import path
from .views import (
CategoryListCreateAPIView,
CategoryDetailAPIView,
)

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name="categories"),
    path('', CategoryDetailAPIView.as_view(), name="category-detail"),
]
