from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def contact(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last Name']
        Email = request.POST['Email']
        Message = request.POST['Message']

        # send  an email
        send_mail(
            First_Name,#name
            Message,#message
            Email,# from email
            ['Neolawrencemasilo@gmail.com'], #to email
        )



        return render(request, 'contact.html', (''))
    else:
        return render(request, 'contact.html', {})