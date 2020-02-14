from braces.views import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView
from django_filters.views import FilterView

from accounts.models import Profile

from .filters import AllUsersFilter, UsersFilter
from .forms import UsersManageForm


# TODO sort
class ProfileListView(LoginRequiredMixin, FilterView):
    model = Profile
    template_name = 'catalogOfUsers/list.html'
    filterset_class = AllUsersFilter
    paginate_by = 3

    def get_queryset(self): 
        new_context = Profile.objects.exclude(user=self.request.user)
        return new_context


class ProfileTenantListView(LoginRequiredMixin, FilterView):
    model = Profile
    template_name = 'catalogOfUsers/list.html'
    filterset_class = UsersFilter
    paginate_by = 3

    def get_queryset(self):
        new_context = Profile.objects.filter(
            user__groups__name__in=['tenant']
        ).exclude(user=self.request.user)
        return new_context


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'catalogOfUsers/user_detail.html'


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'catalogOfUsers/user_detail.html'


class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    #form_class = UsersManageForm
    template_name = 'catalogOfUsers/manage/user_update.html'
    success_url = reverse_lazy('User-list-manage')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied()
        return super(MyProfileUpdateView, self).dispatch(request, *args, **kwargs)
