from django.urls import path

from base.views import DriverAPIVIew, RoadInfoAPIView, PedestrianAPIView

urlpatterns = [
    path('driver/', DriverAPIVIew.as_view(), name='driver'),
    path('road/', RoadInfoAPIView.as_view(), name='road'),
    path('pedestrian/', PedestrianAPIView.as_view(), name='pedestrian')
]
