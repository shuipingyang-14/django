from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world !  django ~~")

def xy(request):
    return HttpResponse("xy!  django ~~ ")