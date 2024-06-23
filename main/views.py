from django.shortcuts import render, redirect
import random
from .models import *
from django.contrib import messages


# view function to shorten an inputed long url
def shorturl(request):

    # function that generate a short url
    def gen_short():
        choice = "abcdefghijklmnopqrstuvwxyz0123456789"
        short = "".join(random.choices(choice, k=6))
        return short

    # call the gen_short function to store the returned value
    short_url = gen_short()

    if request.method == "POST":
        url = request.POST.get("url")

        # check if the url already exist if not it will create the url together with the generated short url
        if not Url.objects.filter(url=url).exists():
            Url.objects.get_or_create(url=url, short_url=short_url)

            messages.info(request, f"{request.META['HTTP_HOST']}/{short_url}")

        # if the url already exist it will display the existed short url for that url
        else:
            u = Url.objects.get(url=url)
            messages.info(request, f"{request.META['HTTP_HOST']}/{u.short_url}")

    return render(request, "url.html")


# a function to redirect the user to the original url if the shortened url is inputed in the web search
def main_url(request, short_str):
    u = Url.objects.get(short_url=short_str)
    return redirect(u.url)
