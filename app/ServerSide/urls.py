from django.conf.urls import url
from . import views

app_name = 'app.ServerSide'
urlpatterns = [
    url(r'^Splash/$', views.Splash, name='Splash'),
    url(r'^Version/$', views.Version, name='Version'),
    url(r'^SaveFCMKey/$', views.SaveFCMKey, name='SaveFCMKey'),
    url(r'^Holiday/$', views.Holiday, name='Holiday'),
    url(r'^WriteFCMMessage/$', views.WriteFCMMessage, name='WriteFCMMessage'),
    url(r'^SendFCMMessage/$', views.SendFCMMessage, name='SendFCMMessage'),
]
