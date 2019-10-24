#It is parent class and give support to the child class
#It won't support for itself
#code reusability can be achived by mixin
#It is the direct child class of Object
#Abstract base class

#mixin is an independent class which contains several instance methods

#it does not contain any instance variable
#differance b/w multile inhefitance and Mixin
#    MIXIN                                              Muiltiple
#1.parent class instatiation is not possible    1.parent class instatiation is possible
#2.parent class contains only instance methods  2.parent class contains both instance methods
#  not instance variable                          and instance variable
#3.The methods are usefull only for child       3.The methods are usefull both child and parent classes
#  classess
#4.parent class should be direct child class    4.parent class can be extend any other class also need not
# of object class                                 be object class



from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_responce(self,json_data):
        return HttpResponse(json_data,content_type='application/json')
