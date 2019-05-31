from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hi This is bakwas.</h1>")