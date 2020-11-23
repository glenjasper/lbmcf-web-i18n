from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from .forms import ContactForm

def send_email(to_name, to_email, to_phone, to_content):
    context = {'to_name': to_name,
               'to_email': to_email,
               'to_phone': to_phone,
               'to_content': to_content}

    template = get_template('contact/email.html')
    html_content = template.render(context)

    subject = '[LBMCF] New message of {} ({})'.format(to_name, to_email)
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER]
    reply_to_list = [to_email]

    email = EmailMultiAlternatives(subject = subject,
                                   # body = to_content,
                                   from_email = from_email,
                                   to = to_list,
                                   reply_to = reply_to_list)
    email.attach_alternative(html_content, 'text/html')
    # email.send()

    return email

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')

            # Send email
            email = send_email(name, email, phone, content)

            try:
                email.send()
                # Ok
                return redirect(reverse('contact_app:url_contact') + '?ok')
            except:
                # Error/Fail
                return redirect(reverse('contact_app:url_contact') + '?fail')

    return render(request,
                  "contact/contact.html",
                  {"context_form": contact_form})
