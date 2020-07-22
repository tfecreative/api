from django.urls import path
from tfecreative.api.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('me/',
         views.AccountView.as_view(),
         name='account'),
]
