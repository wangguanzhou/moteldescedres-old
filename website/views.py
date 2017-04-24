from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import send_mail

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

        emailSubject = 'New reservation by ' + reserveData['firstName'] + ' ' + reserveData['lastName'] + ' via moteldescedres.ca'
        emailBody = render_to_string('reserve_notification.txt', context)
        emailFrom = 'admin@moteldescedres.ca'
        emailTo = 'alexwang74@gmail.com'
        
        send_mail(emailSubject, emailBody, emailFrom, [emailTo], fail_silently=False)
        
        return render(request, emailBody, context)

    else:
        context = {}
        return render(request, "homepage.html", context)
        

