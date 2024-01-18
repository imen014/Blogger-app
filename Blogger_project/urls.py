"""
URL configuration for Blogger_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.views import create_account, login_user, home, logout_user
from django.conf.urls.static import static
from Blogger_project import settings

from Blogger.views import create_blog_and_image, get_blogs_images, get_my_blogs_and_images, modify_blog_image, delete_blog_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_account/', create_account, name='create_account'),
    path('', login_user, name='login_user'),
    path('home/', home, name='home'),
    path('logout_user/', logout_user, name='logout_user'),
    path('create_blog_and_image/', create_blog_and_image, name='image-blog-create'),
    path('get_blogs_images/', get_blogs_images, name='get_blogs_images'),
    path('get_my_blogs_and_images/', get_my_blogs_and_images, name='get_my_blogs_and_images'),
    path('modify_blog_image/<int:id>/modify', modify_blog_image, name='modify_blog_image'),
    path('delete_blog_image/<int:id>/delete', delete_blog_image, name='delete_blog_image'),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
