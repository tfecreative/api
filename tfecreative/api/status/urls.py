from django.urls import path
from tfecreative.api.status import views

app_name = 'status'

urlpatterns = [
    path('', views.StatusView.as_view(), name='status'),
]
