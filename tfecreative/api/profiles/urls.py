from django.urls import path
from tfecreative.api.profiles import views

app_name = 'profiles'

urlpatterns = [
    path('me/',
         views.MyProfileView.as_view(),
         name='my-profile'),
]
