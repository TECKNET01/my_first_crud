from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
