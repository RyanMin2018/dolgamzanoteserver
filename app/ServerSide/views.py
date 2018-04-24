from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import AlarmMessageKey

def Splash(request):
    height = request.GET.get("h")
    return render(request, 'app/ServerSide/Splash.htm', {'height':height,})

def Version(request):
    lang = request.GET.get("lang")
    currentApplicationVersion = 2
    currentMessageVersion = 7
    message = "Brilliant VR Asia Information Memorandum..."
    url = "dolgamza://dolgamzanote.pythonanywhere.com/"

    if lang == 'ko':
        holidayversion = 2
    else :
        holidayversion = 1

    return render(request, 'app/ServerSide/Version.htm', {
            'lang':lang,
            'version':currentApplicationVersion,
            'messageid':currentMessageVersion,
            'message':message,
            'url':url,
            'holidayversion':holidayversion,
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
    lang = request.GET.get("lang").capitalize();
    strFileName = 'app/ServerSide/Holiday' + lang + '.txt'
    return render(request, strFileName,)

