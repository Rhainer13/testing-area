from django.shortcuts import render

# Create your views here.
def form1(request):
    return render(request, 'app1/form1.html')