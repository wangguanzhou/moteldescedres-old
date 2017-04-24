from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import send_mail
import urllib
from urllib.request import urlopen

# Create your views here.
def sendSMSviaNexmo(smsContent):
    params = {
        'api_key': '8f27294a',
        'api_secret': 'f44647eee9a437f0',
        'to': '15147757799',
        'from': '15147757799',
        'text': 'reserve notification received.'
    }

    url = 'https://rest.nexmo.com/sms/json?' + urllib.parse.urlencode(params)
    print(url)
    request = urllib.request.Request(url)
    request.add_header('Accept', 'application/json')
    response = urllib.request.urlopen(request)
    if response.code == 200 :
        print('success')
    else:
        print('failure')

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
        emailTo1 = 'moteldescedres@videotron.ca'
        emailTo2 = 'alexwang74@gmail.com'
        
        send_mail(emailSubject, emailBody, emailFrom, [emailTo1, emailTo2], fail_silently=False)
        sendSMSviaNexmo('...')
        return render(request, 'reserve_notification.txt', context)

    else:
        context = {}
        return render(request, "homepage.html", context)
        

