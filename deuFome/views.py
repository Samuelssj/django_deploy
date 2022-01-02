from django.shortcuts import render
from django.utils import timezone
from .models import MakeOrder

# Create your views here.


def post_list(request):
    posts = MakeOrder.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request,'deuFome/post_list.html',{'posts': posts})
