from django.shortcuts import render, redirect
from .models import Products
from .forms import ApplicationForm


def home(request):
    products = Products.objects.all()[:9]
    return render(request, 'index.html', {'products': products})


def contact(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Good')
            return redirect('/')

    return render(request, 'contact.html', {'form': form})


def shop(request, id):
    item = Products.objects.get(id=id)
    return render(request, 'shop.html', {'item': item})


