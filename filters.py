from accounts.models import Profile, User
import django_filters


class UsersFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = {'city'}
        #exclude = ['',]

class AllUsersFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = {'city':['iexact'], 'user__first_name':['iexact'], 'user__last_name':['iexact']}
        #exclude = ['',]
