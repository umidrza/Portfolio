from django.urls import path
from portfolio.views import *

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_list, name='list'),
    path('<int:id>/', portfolio_detail, name='detail'),
    path('create/', portfolio_create, name='create'),
    path('pdf/<int:id>/', portfolio_pdf, name='pdf'),
]