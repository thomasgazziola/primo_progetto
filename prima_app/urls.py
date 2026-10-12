from django.urls import path
from django.contrib import admin
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili,index

app_name="prima_app"
urlpatterns=[
    path('homepage', homepage, name='homepage'),
    path('welcome/', welcome, name='welcome' ),
    path('lista/', lista, name='lista'),
    path('chi_siamo/', chi_siamo,name='chi_siamo'),
    path('variabili/', variabili, name='variabili'),
    path('admin/', admin.site.urls),
    path('index/', index, name='index')
]

