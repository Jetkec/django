from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def request_views(request):
    scheme = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES
    return render(request,'01-request.html',locals())

def get_views(request):
    if 'name' in request.GET:
        print('name'+request.GET['name'])
    if 'age' in request.GET:
        print('age'+request.GET['age'])
    return HttpResponse('Get OK')

def post_views(request):
    if request.method == 'GET':
        return render(request,'03-post.html')
    else:
        return HttpResponse('POST OK')

def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'04-form.html',locals())
    else:
        # 手动解析
        # subject = request.POST['subject']
        # email = request.POST['email']
        # message = request.POST['message']
        # topic = request.POST['topic']
        # isSaved = request.POST['isSaved']
        # print(subject,email,message,topic,isSaved)
        # return HttpResponse('POST OK')
        # 自动解析
        form = RemarkForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            subject = cd['subject']
            email = cd['email']
            message = cd['message']
            topic = cd['topic']
            isSaved = cd['isSaved']
            print(subject,email,message,topic,isSaved)
        return HttpResponse('POST OK')