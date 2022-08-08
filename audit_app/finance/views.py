from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import csv
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate as auth
from django.contrib.auth import logout as lo
from datetime import timedelta, date, datetime
from .models import Category, Costs, Profits
from .send_email import send_email
from .generic_statistic_file import file_create


def index(request):

    unique_category = Category.objects.all()

    if request.method == 'GET':

        get_costs = Costs.objects.filter(date_costs=date.today())
        profit_query = Profits.objects.filter(date_profit=date.today())
        profit = sum([p.count for p in profit_query])
        all_costs = sum([costs.count for costs in get_costs])
        period = 'today'
        category_id = 'all_category'
        file_send, file_download = file_create(period, category_id, get_costs)
        return render(request, 'finance/index.html', {'costs': get_costs, 'unique_category': unique_category,
                                                      'sum_costs': all_costs, 'profit': profit, 'period': period,
                                                      'file': file_download})

    if request.method == 'POST':
        email_method = request.POST['send_email']
        category_id = request.POST['category']
        period = request.POST['period']
        period_dct = {
            'today': date.today(),
            '7-days': date.today() - timedelta(days=7),
            '30-days': date.today() - timedelta(days=30),
            '180-days': date.today() - timedelta(days=180)
        }
        profit_query = Profits.objects.filter(date_profit__range=[period_dct.get(period), date.today()])
        profit = sum([p.count for p in profit_query])

        if category_id != 'all_category':
            get_costs = Costs.objects\
                .filter(category_id=category_id, date_costs__range=[period_dct.get(period), date.today()])
            all_costs = sum([costs.count for costs in get_costs])
            file_send, file_download = file_create(period, category_id, get_costs)
            if email_method:

                send = send_email(file_send, email_method)
                if send:
                    print('send')
            return render(request, 'finance/index.html', {'costs': get_costs, 'unique_category': unique_category,
                                                          'sum_costs': all_costs, 'profit': profit, 'period': period,
                                                          'file': file_download})
        else:
            get_costs = Costs.objects.filter(date_costs__range=[period_dct.get(period), date.today()])
            all_costs = sum([costs.count for costs in get_costs])
            file_send, file_download = file_create(period, category_id, get_costs)
            if email_method:
                send = send_email(file_send, email_method)
                if send:
                    print('send')
            return render(request, 'finance/index.html', {'costs': get_costs, 'unique_category': unique_category,
                                                          'sum_costs': all_costs, 'profit': profit, 'period': period,
                                                          'file': file_download})


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
        profit = Profits.objects.create(count=money, date_profit=date)
        return render(request, 'finance/add-profit.html', {})

    return render(request, 'finance/add-profit.html', {})


def about(request):
    return render(request, 'finance/about.html')
