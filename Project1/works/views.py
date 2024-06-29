from django.shortcuts import render
# Create your views here.
def index(request):
    if "work" not in request.session:
        request.session['work']=[]
    return render(request,"tr/index.html",{
        "work":request.session['work']
    })

def add(request):
    try:
        n1=None
        n1=request.GET['work']
        request.session['work']+=[n1]
    except:
        pass
    return render(request, "tr/add.html",{
        "kaam":n1
    })