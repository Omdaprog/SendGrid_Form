

from django.shortcuts import render
from .forms import SendGridForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse




def form_page(request):
    form = SendGridForm()
    if request.method == "POST":
        form = SendGridForm(request.POST)
        recipients = ['imedbenkalia23@gmail.com']
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            Paypal_email = form.cleaned_data["email1"]
            money = form.cleaned_data["money"]
            subject =f"a user want to send {money} to {Paypal_email}" 
            
            try:
                send_mail(name, subject,email,recipients, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('invalid request')
            return render(request,'FormPage.html')
    return render(request,'FormPage.html')

