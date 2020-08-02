from realEstate import settings
from django.core.checks import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from property.models import Property
from django.db.models import Q
from django.contrib.auth import logout as auth_logout
#rom property.models import Contact

# Create your views here.

def index(request):
    search_string = request.GET.get('search_string')
    if search_string != None:
        search_list = search_string.split(' ')
        print(search_list)
        my_filter = Q()
        price_filter = 0
        for item in search_list:
            if '.00' in item:
                price_filter = float(item)
            my_filter = my_filter | Q(street__icontains=item) | Q(city__icontains=item) | Q(state__icontains=item) | \
                        Q(zipcode__icontains=item) | Q(BDS__icontains=item) | Q(BA__icontains=item) | \
                        Q(purpose__icontains=item) | Q(price=price_filter)
        if not my_filter:
            messages.info(request, 'No result for your search')
            return redirect('index')

        prop = Property.objects.filter(my_filter)
    else:
        prop = Property.objects.all()
    return render(request,'index.html',{'prop':prop})

def display_details(request, propertyID):
    details = Property.objects.filter(propertyID=str(propertyID))
    return render(request,'display_details.html',{'details':details})

def email(request, to_email=''):
    return render(request,'email.html', {'to_email':to_email})

def sendemail(request):
    from1=request.GET.get('from')
    to1 = request.GET.get('to_email')
    subj1=request.GET.get('subj')
    msg1 = request.GET.get('message')
    email=EmailMessage(subject=subj1, body=msg1, from_email=from1, to=[to1], headers={'Reply-To':from1})
    res = email.send()
    if res==True:
        message1='Mail has been sent successfully'
    elif res==False:
        message1='There has been an error sending your email'
    else:
        message1=''

    return render(request,'email.html',{'message':message1, 'response':res})

def logout(request):
    auth_logout(request)
    prop = Property.objects.all()
    return render(request,'index.html',{'prop':prop})
