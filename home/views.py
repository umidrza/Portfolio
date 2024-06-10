from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.conf import settings

# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def contact_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        contact = form.save()

        html_message = render_to_string("email.html", {"name": contact.name})

        email_message = EmailMessage(
            subject = "Yeni Müraciət",
            body = html_message,
            from_email = settings.EMAIL_HOST_USER,
            to = [contact.email],
        )

        email_message.content_subtype = "html"
        email_message.send()

        messages.success(request, "Müraciətiniz uğurla göndərildi...")

    return render(request, "contact.html", {'form': form})


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response