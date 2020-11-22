from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    result = "Hello Django"
    return HttpResponse(result, content_type="text/plain")

from pymongo import MongoClient
def boardlist(request):
    data = request.GET.copy()
    with MongoClient('mongodb://192.168.219.138:27017/') as client:
        worknetDB = client.worknet
        result = list(worknetDB.samplecollection.find({}))

        result_page = []
        for info in result:
            temp = {'jobs':info['jobs'], 'companies':info['companies'], 'date':info['date']}
            result_page.append(temp)
        data['page_obj'] = result
    

    return render(request, 'board/listwithmongo.html', context=data)