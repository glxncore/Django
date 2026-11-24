from django.shortcuts import render
from .forms import LoginModelForm
def greeting(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = LoginModelForm()
    return render(request,'index.html',{'form':form})

def aboutUs(request):
    return render(request,'about-us.html')
def pages(request, title):
    return render(request,'pages.html',{'title':title})
def count(request, num):
    return render(request,'count.html',{'num':num})




from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
 
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render

def pagevisit(request):
    # Get the current count from the session, or set it to 0 if it doesn't exist
    count = request.session.get('page_count', 0)
    # Increment the count
    count += 1
    # Store the updated count in the session
    request.session['page_count'] = count
    # Render the template with the count variable
    return render(request,'page_view.html', {'count': count})










