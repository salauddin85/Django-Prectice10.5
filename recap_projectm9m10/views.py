from django.shortcuts import render
from django.http import HttpResponse
import datetime


# def home(request):
#     return render(request,"index.html")



# for context in django
def home(request):
    dict= {'Author':'Salauddin','age':30,'Division':'Chottogram','details':
        [
        {
        'id':1,
        'roll':333,
        'department':'computer',
        },
        {
        'id':2,
        'roll':353,
        'department':'computer',
        }
        ],
        'val':5,
        'name':'salauddin',
        'name1':'al a ud din',
        'birth':datetime.datetime.now(),
        'lst':['a','b','c'],
        'num':123,
        'slice':[2,'a',4,5,'b'],
        
    }
    return render(request,"context.html",dict)
# kunu object baniye patale "" double cotetion ar bitore dite hoy jemon 25 number line disi

















 