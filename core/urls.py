"""
URL configuration for core project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL
from account import views
from account.views import CustomLoginView, CustomLogoutView, CustomRegisterView, CustomTermsView, index_view, contact_view, shop_view, testimonial_view, why_view
from account.views import profile_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/', include('account.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('terms/', CustomTermsView.as_view(), name='terms'),
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('templates/shop.html', shop_view, name='shop'),
    path('templates/testimonial.html', testimonial_view, name='testimonial'),
    path('templates/why.html', why_view, name='why'),
    path('search/', views.search_results_view, name='search_results'),
    path('add/', views.add_product, name='add_product'),
    path('my_products/', views.my_products, name='my_products'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('basket/', views.basket_views, name='basket'),
    path('remove/<int:product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('summ_views/<int:product_id>/', views.summ_views, name='summ_views'),
    path('', include('new_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
