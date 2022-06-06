from django.shortcuts import render



# Create your views here.

def home(request):

    return render(request, 'core/home.html')
    

def home2(request):

    return render(request, 'core/home2.html')

def home3(request):

    return render(request, 'core/home3.html')

def contacto(request):

    return render(request, 'core/contacto.html')

def login(request):

    return render(request, 'core/login.html')

def Registro(request):

    return render(request, 'core/Registro.html')

def BandanaB(request):

    return render(request, 'core/BandanaB.html')

def BandanaF(request):

    return render(request, 'core/BandanaF.html')

def ArnesN(request):

    return render(request, 'core/ArnesN.html')

def ArnesF(request):

    return render(request, 'core/ArnesF.html')

def CollarP(request):

    return render(request, 'core/CollarP.html')

def CollarH(request):

    return render(request, 'core/CollarH.html')


def HuesoP(request):

    return render(request, 'core/HuesoP.html')

def HuesoPJ(request):

    return render(request, 'core/HuesoPJ.html')



    