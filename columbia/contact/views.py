from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    title = "contact"
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' % (comment, name)
        from_email = form.cleaned_data['email']
        to_email = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_email, fail_silently=False, auth_user=None, auth_password=None,
                  connection=None, html_message=None)
        title = "Thanks for reaching out!"
        confirm_message = "Thanks for the message.  We will get back to you as soon as we can."
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)
