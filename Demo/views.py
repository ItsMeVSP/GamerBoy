from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # msg="<h1>Annan Naan Erangi Varava</h1>"
    return render(request,'index.html')
