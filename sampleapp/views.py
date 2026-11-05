

# Create your views here.
from django.shortcuts import render
def greeting(request):
    return render(request,'index.html')
def variable(request):
    count = 23
    return render(request,'index.html',{'count':count})
def safevariable(request):
    count = '<b>23</b>'
    return render(request,'index.html',{'count':count})
from django.shortcuts import render
def condition(request):
    count = 23
    return render(request,'index.html',{'count':count})
def loop(request):
    students = ['Ajay', 'Vineeth','Sudheesh']
    return render(request,'index.html',{'students':students})