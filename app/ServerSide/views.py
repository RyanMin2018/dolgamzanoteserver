from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import AlarmMessageKey
'''
from google.oauth2 import id_token
from google.auth.transport import requests
'''

def Splash(request):
    height = request.GET.get("h")
    return render(request, 'app/ServerSide/Splash.htm', {'height':height,})

def Version(request):
    lang = request.GET.get("lang")[:5]
    currentApplicationVersion = 2
    holidayversion = 1

    return render(request, 'app/ServerSide/Version.htm', {
            'lang':lang,
            'applicationVersion':currentApplicationVersion,
            'holidayVersion':holidayversion,
        }
    )

@csrf_exempt
def SaveFCMKey(request):
    if request.method == "POST":

        '''
        m = AlarmMessageKey()
        m.userid = request.POST.get("id")
        m.fcmkey = request.POST.get("key")
        m.save()
        '''

        uid = request.POST.get("id")
        key = request.POST.get("key")

        if AlarmMessageKey.objects.filter(userid=uid).exists():
            AlarmMessageKey.objects.filter(userid=uid).update(
                fcmkey = key,
            )
        else :
            AlarmMessageKey.objects.create(
                userid = uid,
                fcmkey = key,
            )
        return HttpResponse(uid)
    else:
        return HttpResponse("Fail...")

def Holiday(request):
    lang = request.GET.get("lang").capitalize()[:5];
    strFileName = 'app/ServerSide/Holiday' + lang + '.txt'
    return render(request, strFileName,)


def WriteFCMMessage(request):
    list = AlarmMessageKey.objects.order_by('-dt')
    return render(request, 'app/ServerSide/WriteFCMMessage.htm', {'list':list})

def SendFCMMessage(request):
    url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Authorization':'key=AAAA_65J53k:APA91bE3av6Z6L36uawZ6xhAcmpmMs75aryUXaUar14SSHhWwvmrlHmfWmrwHPvT7XkcNFVEhEM5rwhHFKZnOSQvVIkDolmjKTlHLISueW5Kd5q8K6o0yMzdCaQkkk4nioiHBXZDelTrUguN7aUf1assiffAaXWc2w',
        'Content-Type':'application/json; UTF-8',
    }
    to    = request.POST.get('to')
    title = request.POST.get('title')
    msg   = request.POST.get('msg')
    link  = request.POST.get('link')
    img   = request.POST.get('img')

    content = {
        'to':to,
        'data':{
            'title':title,
            'message':msg,
            'linkurl':link,
            'imgurl':img
        }
    }
    res = requests.post(url, data=json.dumps(content), headers=headers)
    return HttpResponse(res.text)

