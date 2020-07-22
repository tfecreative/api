from django.conf.urls import url
from django.urls import path
from tfecreative.api.auth import views


urlpatterns = [
    path('',
         views.Auth.as_view(),
         name='auth'),
    path('sign-in/',
         views.SignIn.as_view(),
         name='sign-in'),
    path('sign-out/',
         views.SignOut.as_view(),
         name='sign-out'),
    path('sign-up/',
         views.SignUp.as_view(),
         name='sign-up'),
]
