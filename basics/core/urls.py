from django.urls import path
from .views import Main, Products

# this is a example how routes 
# are build in big projects
# for this create a url file on app
# and add that app urls to it 
urlpatterns = [
    path('', Main.as_view()),
    path('products', Products.as_view())
]