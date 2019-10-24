from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data = {
    'eno': 100,
    'ename':'Karthik',
    'esal':1000,
    'eadd':'Banalore'
    }
    resp = '<h1>Emp No:{}<br>Emp Name:{}<br>Emp Salary:{}<br>Emp Add:{}<h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eadd'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data = {
    'eno': 100,
    'ename':'Karthik',
    'esal':1000,
    'eadd':'Banalore'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type = 'application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
    'eno': 100,
    'ename':'Karthik',
    'esal':1000,
    'eadd':'Banalore'
    }
    return JsonResponse(emp_data)

#write class based view class should be the child class of view
from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from GET method"})
        return HttpResponse(json_data,content_type = 'application/json')
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from POST method"})
        return HttpResponse(json_data,content_type = 'application/json')
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from PUT method"})
        return HttpResponse(json_data,content_type = 'application/json')
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from DELETE method"})
        return HttpResponse(json_data,content_type = 'application/json')

from testapp.mixin import HttpResponseMixin
class JsonCBVMixin(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from GET method"})
        return self.render_to_http_responce(json_data)
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from POST method"})
        return self.render_to_http_responce(json_data)
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from PUT method"})
        return self.render_to_http_responce(json_data)
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"This is from DELETE method"})
        return self.render_to_http_responce(json_data)
