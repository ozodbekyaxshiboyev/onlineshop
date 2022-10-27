from django.contrib import admin
from .models import Comment, Rating, Wishlist

admin.site.register([Comment, Rating, Wishlist])
