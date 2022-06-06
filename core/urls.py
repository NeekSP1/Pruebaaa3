from django.urls import path
from .views import home,home2,home3,contacto,login,Registro,BandanaB,BandanaF,ArnesN,ArnesF,CollarP,CollarH,HuesoP,HuesoPJ

urlpatterns = [
    path('',home,name="home"),
    path('home.html',home,name="home"),
    path('home2.html',home2,name="home2"),
    path('home3.html',home3,name="home3"),
    path('core/home3.html',home3,name="home3"),
    path('contacto.html',contacto,name="contacto"),
    path('login.html',login,name="login"),
    path('Registro.html',Registro,name="Registro"),
    path('BandanaB.html',BandanaB,name="BandanaB"),
    path('BandanaF.html',BandanaF,name="BandanaF"),
    path('ArnesN.html',ArnesN,name="ArnesN"),
    path('ArnesF.html',ArnesF,name="ArnesF"),
    path('CollarP.html',CollarP,name="CollarP"),
    path('CollarH.html',CollarH,name="CollarH"),
    path('HuesoP.html',HuesoP,name="HuesoP"),
    path('HuesoPJ.html',HuesoPJ,name="HuesoPJ"),
    
    
    
    
]