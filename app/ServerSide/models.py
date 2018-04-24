from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class AlarmMessageKey(models.Model):
    objects = models.Manager()
    dt     = models.DateTimeField(default=timezone.now, verbose_name='Date')
    userid = models.CharField(max_length=50, verbose_name='Device Secure Key')
    fcmkey = models.CharField(max_length=200, verbose_name='FCM Key')

    def __str__(self):
        return self.userid
