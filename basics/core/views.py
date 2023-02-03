from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from .models import Product
# Create your views here.

# main function describe a view.
# a view is a user return
# something as function below
def main(request):
    return render(request, 'main.html')
    # this function describe what todo when request some route with this function
    # if this route access render main.html

# django has a 3 base class views
# 1) the class 'view' is the base class
# All other class-based views inherit from this base class. 
# It isn’t strictly a generic view and thus can also be imported from django.views.
# as class view example:
class Main(View):
    # here we define a get method
    # when this class is called as view with get method from HTTP
    # this fuction is called
    def get(self, request, *args, **kwargs):
        return HttpResponse('Main')

# 2) the class TemplateView
# Renders a given template, with the context containing parameters captured in the URL.
# that class renders a HTML template, with information requested
class HomePageView(TemplateView):
    # and our template is passed as
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # here, context will be all data requested from some model
        # context['latest_articles'] = Article.objects.all()[:5]
        return context

# 3) the class RedirectView
# this class redirect to a especific given url
# when called is redirect to a url passed in path (route describe)
class ArticleCounterRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class Products(View):
    def get(self, request):
        print(request)
        products = Product.objects.all()
        return HttpResponse(products)