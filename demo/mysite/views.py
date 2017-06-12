from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.template import RequestContext

from models import Article, Reply



# index page
def index(request):
    latest_article_list = Article.objects.all().order_by('-pub_date')[:10]
    return render_to_response('mysite/index.html', {'latest_article_list': latest_article_list})

# login page
def login(request):
    return render_to_response('mysite/login.html', {}, context_instance=RequestContext(request))

# check username and password from db
def login_check(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=uname, password=pw)
        if user is not None:
            return redirect(reverse('mysite.views.index'))
        else:
            return redirect(reverse('mysite.views.login'))
    return redirect(reverse('mysite.views.login'))