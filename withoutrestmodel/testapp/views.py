from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
# Create your views here.
#if we want to fetch all the data from the database like - Employee.objects.all()
#Serializers --> django inbuild module
#serialize() is the method
class EmployeeDetailCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp = Employee.objects.get(id = id)
        #Converting python dictionary to json object is called Serialization
        # emp_data = {
        # 'eno' : emp.eno,
        # 'ename': emp.ename,
        # 'esal' : emp.esal,
        # 'eaddr' :emp.eaddr
        # }
        # json_data = json.dumps(emp_data)
        json_data = serialize('json',[emp])
        return HttpResponse(json_data,content_type = 'application/json')

class EmployeeListCBV(View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = serialize('json',qs)
        return HttpResponse(json_data,content_type = 'application/json')
