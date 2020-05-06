from django.urls import path
from .views import form_page
app_name = 'core'

urlpatterns = [
    path('',form_page, name='form')
]