from django.urls import path, include
from django.conf.urls import url


app_name = 'api'

urlpatterns = [
    path('status/', include('tfecreative.api.status.urls'), name='status'),
    path('accounts/', include('tfecreative.api.accounts.urls'), name='accounts'),
    path('auth/', include('tfecreative.api.auth.urls'), name='auth'),
    path('profiles/', include('tfecreative.api.profiles.urls'), name='profiles'),
]
