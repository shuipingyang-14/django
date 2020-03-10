from django.shortcuts import render
from django.http import HttpResponse, Http404

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

def home(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))

def home1(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home1时间标签：%s年/%s月" %(year, month))