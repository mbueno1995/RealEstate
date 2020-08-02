import requests
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import Property
from django.db.models import Q
from django.contrib.auth import logout as auth_logout
from .models import Customer
from .serializrs import PropertySerializer
from rest_framework import viewsets
from django.shortcuts import render
from newsapi import NewsApiClient

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

def register(request):
    if request.method=='POST':
        custEmail1 = request.POST['custEmail']
        custPassword1a = request.POST['custPassword1']
        custPassword1b = request.POST['custPassword2']
        custFname1 = request.POST['custFname']
        custLname1 = request.POST['custLname']
        occupation1 = request.POST['occupation']
        custZipcode1 = request.POST['custZipcode']
        custPhone1 = request.POST['custPhone']

        if custPassword1a==custPassword1b:
            cust = Customer(custEmail=custEmail1, custPassword=custPassword1a, custFname=custFname1, custLname=custLname1, occupation=occupation1, custZipcode=custZipcode1, custPhone=custPhone1)
            cust.save()
            #return HttpResponse('Welcome '+ custFname1)
            return redirect('index')
        else:
            error1="Password entered didn't match"
            return render(request, 'register.html',{'error':error1})
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    prop = Property.objects.all()
    return render(request,'index.html',{'prop':prop})

class PropertyViewSet(viewsets.ModelViewSet):
    queryset=Property.objects.all().order_by('propertyID')
    serializer_class=PropertySerializer

def googlenews(request):
    newsapi = NewsApiClient(api_key='5b0bd5bf6a82451ba8f5435a59a6e2bd')
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mynews = zip(news, desc, img)
    return render(request, 'news.html', context={"mynews": mynews})

def weathernews(request):
    city = request.GET.get('city')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5fbf20b59ad6242900d3c98d05d84871&units=metric'.format(city)
    myweather = requests.get(url)
    weatherdata=myweather.json()
    temp=weatherdata['main']['temp']
    wind_speed=weatherdata['wind']['speed']
    latitude=weatherdata['coord']['lat']
    longitude=weatherdata['coord']['lon']
    description=weatherdata['weather'][0]['description']

    return render(request, 'weather.html',{'temp':temp, 'wind_speed':wind_speed, 'latitude':latitude, 'longitude':longitude, 'description':description})