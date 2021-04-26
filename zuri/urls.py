from django.contrib import admin
from django.urls import path, include

from blog.views import frontpage, post_detail

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', post_detail, name='post_detail'),
]
