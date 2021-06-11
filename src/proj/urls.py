"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

#import for media files
from django.conf import settings
from django.conf.urls.static import static

from airports import views as airports_views
from refshelf import views as refshelf_views
from books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refshelf/', include('refshelf.urls', namespace='refshelf')),
    path('books/', include('books.urls', namespace='books')),
    path('<code>', airports_views.airports),
    path('', airports_views.airports_home)
]

if settings.DEV_MODE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

