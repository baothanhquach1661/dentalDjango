from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if (request.method) == "POST":
        # do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message': message
            })
        
        #send email

        send_mail(
            'Appoinment ' + message_name, # subject
            message, # message
            'Send from ' + message_email, # from email
            ['baothanhquach1661@gmail.com'], # to my email
            fail_silently=False,
        )

    else:
        # return the page
        return render(request, 'contact.html', {})