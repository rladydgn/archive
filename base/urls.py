from django.urls import path

from base.views import LocationAPIVIew, RoadInfoAPIView

urlpatterns = [
    path('save/', LocationAPIVIew.as_view(), name='location'),
    path('road/', RoadInfoAPIView.as_view(), name='road'),
]