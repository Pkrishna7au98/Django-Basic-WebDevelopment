from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', views.index ,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    path('news/', views.news, name='news')
]


urlpatterns = urlpatterns + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)