from django.shortcuts import render
from .models import Bars

title = "Бары Челябинска"

def index(request):

    bar = Bars.objects.all()
    return render(request, 'bars/index.html', {'bar':bar})
# Create your views here.
