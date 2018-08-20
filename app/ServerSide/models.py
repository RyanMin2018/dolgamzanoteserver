from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class AlarmMessageKey(models.Model):
    objects = models.Manager()
    dt     = models.DateTimeField(default=timezone.now, verbose_name='생성일시')
    userid = models.CharField(max_length=50, verbose_name='단말기고유번호')
    fcmkey = models.CharField(max_length=200, verbose_name='FCM키')

    def __str__(self):
        return self.userid
