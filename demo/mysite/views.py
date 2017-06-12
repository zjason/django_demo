from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.template import RequestContext

from models import Article


# index page
def index(request):
    latest_article_list = Article.objects.all().order_by('-pub_date')[:10]
    # check user status, if user is logged in then provide logout link
    # if user is anonymousUser then provide login and registration links
    if request.user.is_authenticated():
        return render_to_response('mysite/index.html', {'latest_article_list': latest_article_list,
                                                        'user_status': '<a href="/logout" class="navbar-text navbar-right">'+str(request.user)+', logout'+'</a>'})
    else:
        return render_to_response('mysite/index.html', {'latest_article_list': latest_article_list,
                                                        'user_status': '<a href="/login" class="navbar-text navbar-right">Login</a> \
                                                                               <a href="/registration" class="navbar-text navbar-right">Registration</a>'})


# login page
def user_login(request):
    return render_to_response('mysite/login.html', {'user_status': '<a href="/registration" class="navbar-text navbar-right">Registration</a>'}, context_instance=RequestContext(request))


# check username and password from db
def login_check(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(username=user_name, password=user_password)
        # if username and password correct then login user and redirect to index page
        # if username and password incorrect then redirect to login page
        if user is not None:
            login(request, user)
            return redirect(reverse('mysite.views.index'))
        else:
            return redirect(reverse('mysite.views.user_login'))
    return redirect(reverse('mysite.views.user_login'))

# registration page
def registration(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        # if username already exist, provide error message,
        # if username did not exist, create new user and add to 'client' group
        try:
            u = User.objects.get(username=user_name)
            if u:
                return render_to_response('mysite/registration.html', {'status': 'Username already exist!'},
                                          context_instance=RequestContext(request))
        except User.DoesNotExist:
            # create user
            user = User.objects.create_user(user_name, '', user_password)
            user.save()
            # add user to group 'client'
            g = Group.objects.get(name='client')
            g.user_set.add(user)
            # check user from database
            test_user = authenticate(username=user_name, password=user_password)
            if test_user is not None:
                login(request, test_user)
            else:
                return render_to_response('mysite/registration.html', {'status': 'Something went wrong, please try again!'},
                                          context_instance=RequestContext(request))
            return redirect(reverse('mysite.views.index'))

    return render_to_response('mysite/registration.html', {}, context_instance=RequestContext(request))

# logout page, log user out
def user_logout(request):
    logout(request)
    return redirect(reverse('mysite.views.index'))
