from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import Banner, AboutImages, Prospecs
from .models import MainInfo, Apartments


def index_view(request):
    return render(request, 'app/index.html',
                  context={"banners": Banner.objects.all(), "main_info": MainInfo.objects.first(),
                           "about_images": AboutImages.objects.all(), "prospecs": Prospecs.objects.all(),
                           "apartments": Apartments.objects.all()})


def contact_view(request):
    return render(request, 'app/contact.html',
                  context={"main_info": MainInfo.objects.first(), })


def about_view(request):
    return render(request, 'app/about.html',
                  context={"main_info": MainInfo.objects.first(),
                           "prospecs": Prospecs.objects.all(), })


def apartments_view(request):
    apartments_list = Apartments.objects.all()
    paginator = Paginator(apartments_list, 6)  # Show 6 apartments per page
    page_number = request.GET.get('page')
    apartments = paginator.get_page(page_number)

    return render(request, 'app/apartments.html', {
        "main_info": MainInfo.objects.first(),
        "apartments": apartments,
    })


def apartment_details(request):
    return render(
        request,
        "app/apartment-details.html",
        {
            "main_info": MainInfo.objects.first()}
    )



def pricing_view(request):
    return render(request, 'app/pricing.html',
                  context={"main_info": MainInfo.objects.first(), })


from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


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