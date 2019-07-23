from django.shortcuts import render
from datetime import datetime

# Create your views here.
def welcome(request):
    return render(request, 'memo/welcome.html', {'current_date_time':datetime.now})