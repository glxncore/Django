
# Create your views here.
from django.shortcuts import render
from .forms import LoginForm
def display(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'form-data.html',{
                 'email': form['email'].value,
                 'message':"thankyou"
                

             })
    else:
        form = LoginForm()
    return render(request,'index.html',{'form':form})