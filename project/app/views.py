from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def my_render(req):
    # there are 2 ways of sending data to html 
    # first one :
    # return render(req,'my_render.html', {'n':'Smrituu'})
    # second one :
    data = {'n':'Rohit'}
    return render(req,'my_render.html', data)

def my_redirect(req):
    return redirect('redirect1',x=10)

def redirect1(req,x):
    return render(req,'index.html',{'data':x})