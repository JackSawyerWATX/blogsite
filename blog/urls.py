# blog/urls.py

from django.urls import path
from . import views
from django.contrib import admin
from blog.views import visitor_count, home

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Use the new home view for the empty path
    path('blog/index.html', visitor_count, name='blog/index.html'),
]