from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World ! django ~~")

def demo(request):
    return render(request, 'demo.html')

def page(request, num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404