from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path('profile/list', views.ProfileTenantListView.as_view(), name='profiles'),
    path('profile/all', views.ProfileListView.as_view(), name='profiles-all'),
    path('profile/<int:pk>/detail', views.ProfileDetailView.as_view(), name='profile-detail'),

    path('myprofile/detail', views.MyProfileDetailView.as_view(), name='my-profile-detail'),
    path('myprofile/update', views.MyProfileUpdateView.as_view(), name='my-profile-update')

] 