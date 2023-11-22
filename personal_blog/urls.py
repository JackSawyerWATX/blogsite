# personal_blog/urls.py

from django.contrib import admin
from django.urls import path, include
from blog.views import visitor_count, home, reset_count

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path('', home, name='home'),
    path('visitor_count/', visitor_count, name='visitor_count'),
    path('reset_count/', reset_count, name='reset_count'),
]