from django.shortcuts import render
from main.models import *
from django.conf import settings
import os

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
    exist = {} #id:bool
    files = Attatchments.objects.all()
    for file in files:
        if not os.path.isfile(str(settings.BASE_DIR) + file.file.url):
            try:
                parent = file.message.all()[0]
                parent.message += f"<br><del>{file.file.name}</del>"
                parent.save()
            except Exception as e:
                print(e)
            file.delete()
    return render(request, "landing.html",{'msgs':msgs})
