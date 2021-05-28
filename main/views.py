from django.shortcuts import render, HttpResponse

def landing(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
    return render(request, "landing.html")
