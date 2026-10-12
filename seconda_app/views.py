from django.shortcuts import render 


def es_if(request):
    dic = { 'var1': 200,
            'var2': 200,
            'var3': 300 }
#Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render (request, "es_if.html", dic)

def if_else_elif(request):
    dic = { 'var1': 200,
            'var2': 200,
            'var3': 300 }
#Calling the render() method to render the request from es_if_else_elif.html page by using the dictionary, dic
    return render (request, "if_else_elif.html", dic)

from django.shortcuts import render
import datetime

def es_for(request):

    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'], 'list2': [1, datetime.date (2019,7,16), 'Do not give up!'], 'my_dict' : {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'} }
    return render(request, "es_for.html", dic)


