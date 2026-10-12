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


