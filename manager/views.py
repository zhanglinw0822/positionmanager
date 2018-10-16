from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    print(request)
    return render(request, 'manager/home.html', context)
