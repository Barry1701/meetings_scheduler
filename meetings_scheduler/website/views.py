from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html',
                 {'num_meetings': Meeting.objects.count()})

def date(request):
    return HttpResponse('Ta Strona zostala zaladowana ' + str(datetime.now()))

def about(request):
    return HttpResponse('Experienced security professional with over a decade of industry expertise, currently completing a full stack developer course. Skilled in access control management, surveillance oversight, and incident response. Proven track record of delivering exceptional customer service and driving continuous improvement. Eager to leverage technical proficiency and adaptability in dynamic environments.')