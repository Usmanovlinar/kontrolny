from _ast import operator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Calc_History
from histtory.forms import HistoryForm


def get_truth(symbol, a, b):
    oops = {'*': lambda a, b: a * b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: a // b
            }
    return oops[symbol](a, b)
def calculate(request):
    form = HistoryForm()
    if request.method == 'POST':
        symbol = str(request.POST.get('operator'))
        val1 = int(request.POST.get('val1'))
        val2 = int(request.POST.get('val2'))
        result = get_truth(symbol, val1, val2)
        form = HistoryForm(request.POST,  initial={'result':result})
        if form.is_valid():
            form.save()
            return redirect('calc')

    return render(request, template_name='histtory/form.html', context={'form': form})
def history_objects(request):
    storage = Calc_History.objects.all()
    return render(request, "histtory/obj.html", context={'storage':storage})


# Create your views here.
