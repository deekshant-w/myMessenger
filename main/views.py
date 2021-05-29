from django.shortcuts import render, HttpResponse
from main.models import *

def landing(request):
    if request.method == "POST":
        msg = Message(
            heading = request.POST.get("heading"),
            tags    = request.POST.get("tags"),
            message = request.POST.get("msgBody"),
            user = request.META['HTTP_USER_AGENT']
        )
        msg.save()
        for f in request.FILES.getlist("file",[]):
            temp = Attatchments(file=f)
            temp.save()
            msg.files.add(temp)
    
    msgs = Message.objects.all().order_by('-edited')
    return render(request, "landing.html",{'msgs':msgs})
