from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse

def home(request):
    html = " <h1>Welcome to my Home Page</h1><ol><li><a href='/music/'>To go to Music page</a></li><li><a href='/admin/'>To go to admin page</a></li></ol>"
    #return render(request, 'mysite/home.html',context=None)
    return HttpResponse(html)
    #return render_to_response('mysite/home.html')