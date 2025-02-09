from django.db import models


class Driver(models.Model):
    user_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    limit_speed = models.IntegerField()
    road_name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    do_limit = models.IntegerField()


class Pedestrian(models.Model):
    user_id = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)