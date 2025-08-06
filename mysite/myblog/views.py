from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, template_name="register.html", context={'form': form})
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, template_name="register.html", context={'form': form})