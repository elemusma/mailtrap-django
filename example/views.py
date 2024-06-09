from django.http import HttpResponse
from django.core.mail import send_mail


def simple_mail(request):
    send_mail(
        subject="That's the subject line",
        message="hello from the body of the email",
        recipient_list="tadeoycuba@gmail.com",
    )

    return HttpResponse("Message sent")
