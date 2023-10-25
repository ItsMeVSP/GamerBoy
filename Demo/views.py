from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # msg="<h1>Annan Naan Erangi Varava</h1>"
    if request.method=="POST":
        personname=request.POST.get('firstname','')
        songname=request.POST.get('songname','')
        html=f'''
        <p>Hi {personname}</p>
        <p>Your request for the song-{songname} is accepted. It will be played in the concert.</p>
        <p>Thank you</p>
        '''
        return render(request,'index.html',{'mycontent':html})
    else:
        return render(request,'index.html')
