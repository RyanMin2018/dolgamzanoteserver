# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from .models import AlarmMessageKey

class AlarmMessageKeyForm(forms.ModelForm):
    class Meta:
        model = AlarmMessageKey
        fields = ('userid', 'fcmkey',)

