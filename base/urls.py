from django.urls import path

from base.views import LocationAPIVIew

urlpatterns = [
    path('save/', LocationAPIVIew.as_view(), name='location'),
]