from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'deuFome/post_list.html',{})
