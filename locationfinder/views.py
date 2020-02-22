from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from locationfinder.forms import regform
from locationfinder.models import reg, add, fed, fedre, locre


def open(request):
    return render(request, 'open.html')


def hom(request):
    d = add.objects.filter(status=1)
    return render(request, 'hom.html', {'s': d})


def home(request):
    h = add.objects.filter(status=1)
    return render(request, 'home.html', {'s': h})


def log(request):
    userlist = reg.objects.all()
    return render(request, 'signin.html', {'user': userlist})


def login(request):
    un = request.POST['user']
    ps = request.POST['passw']
    try:
        request.session['name'] = un
        if un=="admin" and ps=="admin":
            return admins(request)
        else:
            m = reg.objects.get(username=request.POST['user'])
            if m.password == (request.POST['passw']):
                return home(request)
            else:
                return HttpResponse("Your username and password didn't match.")

    except:
        return render(request,'signin.html',{'error':"Username is not valid"})


def profile(request):
    try:
        ch = request.session['name']

        us = reg.objects.filter(username=ch)

        return render(request, 'profile.html', {'ww': us})
    except:
        return render(request, 'signin.html')



def logout(request):
    try:
        del request.session['name']
    except KeyError:
        pass
    return hom(request)


def registered(request):
    return render(request, 'registered.html')


def regt(request):
    form = regform()
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            form.save()
            return registered(request)
        else:
            HttpResponse("invalid data")
    return render(request, 'signup.html', {'form': form})


def locadd(request):
    try:
        nm = request.session['name']
        if nm == 'admin':
            if request.method == 'POST':
                f = add(userid=nm, locname=request.POST['lname'], map=request.POST['map'], cover_img=request.FILES['cimg'],
                    img_1=request.FILES['img1'], img_2=request.FILES['img2'], img_3=request.FILES['img3'],
                    indro=request.POST['ind'], desc=request.POST['des'],status=1 )
                f.save()
                return render(request,'adminadd.html',{'msg':"Successfully Uploaded"})
            return render(request, 'adminadd.html')
        else:
            if request.method == 'POST':
                f = add(userid=nm, locname=request.POST['lname'], map=request.POST['map'], cover_img=request.FILES['cimg'],
                        img_1=request.FILES['img1'], img_2=request.FILES['img2'], img_3=request.FILES['img3'],
                        indro=request.POST['ind'], desc=request.POST['des'], status=0)
                f.save()
                return render(request,'add.html',{'msg':"Successfully Uploaded"})
            return render(request, 'add.html')

    except:
        return render(request, 'signin.html')


def feed(request):
    try:
        n = fed(date=date.today(), userid=request.session['name'], feed=request.POST['feedback'])
        n.save()
        return HttpResponse('Thank You...!')
    except:
        return HttpResponse('Please sign in your account')


def success(request):
    return HttpResponse('successfully uploaded')


def locview(request):
    try:
        s = request.session['name']
        if s=='admin':
            d = add.objects.filter(userid=s)
            return render(request, 'adminlocview.html', {'s': d})
        else:
            d = add.objects.filter(userid=s)
            return render(request, 'locview.html', {'s': d})
    except:
        return render(request, 'signin.html')


def about(request):
    return render(request, 'about.html')


def liked(request):
    return render(request, 'liked.html')


def notification(request):
    try:
        c = request.session['name']
        print(c)
        d= fedre.objects.filter(userid=c)
        e= locre.objects.filter(userid=c)
        return render(request, 'notification.html',{'s':d,'t':e})
    except:
        return render(request,'notification.html')


def view(request):
    a = request.POST['btnview']
    b = add.objects.filter(locname=a)
    return render(request, 'view.html', {'a': b})

def admins(request):
    g = add.objects.filter(status=0)
    return render(request,'admins.html', {'s': g})

def more(request):
    a = request.POST['btnmore']
    b = add.objects.filter(locname=a)
    return render(request,'more.html', {'s': b})

def approve(request):
    a = request.POST['btnapp']
    b = request.POST['btnid']
    data=add.objects.get(id=a)
    data.status=1
    data.save()
    st = locre(date=date.today(), userid=b, locstatus="Your location has approved")
    st.save()
    return admins(request)

def reject(request):
    a = request.POST['btnrej']
    b = request.POST['btnid2']
    data = add.objects.get(id=a)
    data.delete()
    st = locre(date=date.today(), userid=b, locstatus="Your location has rejected")
    st.save()
    return admins(request)

def fedview(request):
    fd = fed.objects.all()
    return render(request,'fedview.html',{'s':fd})


def fedreplay(request):
    r = fedre(date=date.today(),userid=request.POST['btn-fed'], feedreplay=request.POST['feddd'])
    r.save()
    return HttpResponse('successfully')

def trash(request):
    try:
        b = request.POST['btn-rmv']
        data = fedre.objects.get(id=b)
        data.delete()
        return notification(request)
    except:
        a =request.POST['btn-rmv']
        data2 = locre.objects.get(id=a)
        data2.delete()
        return notification(request)

def change(request):
    s = request.session['name']
    x = reg.objects.get(username=s)
    if x.password == (request.POST['old']):
        if request.POST['new'] == request.POST['new1']:
            x.password = request.POST['new']
            x.save()
        else:
            return HttpResponse('password does not match ')
    else:
        return HttpResponse('Incorrect password')
    return log(request)



# Create your views here.
