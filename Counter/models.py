from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmr = models.FloatField()
    res = models.FloatField()
    bmi = models.FloatField(default=22.05)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.user.username
