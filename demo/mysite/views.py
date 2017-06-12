from django.shortcuts import render_to_response, get_object_or_404
from models import Article, Reply

# Create your views here.

def index(request):
    latest_article_list = Article.objects.all().order_by('-pub_date')[:10]
    return render_to_response('mysite/index.html', {'latest_article_list': latest_article_list})