from django.shortcuts import render
from datetime import datetime

# Create your views here.

def homepage(request):
    if request.is_ajax():
        context = {}
        reserveData = {}
        reserveData['firstName'] = request.POST['firstName']
        reserveData['lastName'] = request.POST['lastName']
        reserveData['phoneNo'] = request.POST['phoneNo']
        reserveData['email'] = request.POST['email']
        reserveData['clientMsg'] = request.POST['clientMsg']
        reserveData['checkinDate'] = request.POST['checkinDate']
        reserveData['checkoutDate'] = request.POST['checkoutDate']
        reserveData['numOfAdults'] = request.POST['numOfAdults']
        reserveData['numOfChildren'] = request.POST['numOfChildren']

        context['reserveTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['reserveData'] = reserveData
        
        return render(request, "reserveresponse.html", context)

    else:
        context = {}
        return render(request, "reserveresponse.html", context)

