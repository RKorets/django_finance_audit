from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate as auth
from django.contrib.auth import logout as lo
from .models import Category, Costs, Profits


def index(request):

    get_costs = Costs.objects.all()
    # get_costs.category_id = ', '.join([str(name) for name in get_costs.category.all()])
    print(get_costs)

    return render(request, 'finance/index.html', {'costs': get_costs})


def add_costs(request):

    get_category = Category.objects.all()
    if request.method == 'POST':
        category_id = request.POST['category']
        date = request.POST['date']
        description = request.POST.get('description')
        spent = request.POST['spent']
        cost = Costs.objects.create(count=spent, description=description, date_costs=date, category_id=category_id)
        return render(request, 'finance/add-costs.html', {'category': get_category})

    return render(request, 'finance/add-costs.html', {'category': get_category})


def add_profit(request):
    if request.method == 'POST':

        money = request.POST['money']
        date = request.POST['date']
        profit = Profits(count=money, date_profit=date)
        return render(request, 'finance/add-profit.html', {})

    return render(request, 'finance/add-profit.html', {})


def about(request):

    return render(request, 'finance/about.html')