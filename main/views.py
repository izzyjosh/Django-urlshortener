from django.shortcuts import render, redirect
import random
from .models import *
from django.contrib import messages


def shorturl(request):
	def gen_short():
		choice = "abcdefghijklmnopqrstuvwxyz0123456789"
		short = "".join(random.choices(choice, k=6))
		return short
	
	short_url = gen_short()
	if request.method == "POST":
		url = request.POST.get("url")
		
		if not Url.objects.filter(url=url).exists():
			Url.objects.create(url=url, short_url=short_url)
		
			messages.info(request, f"{request.META['HTTP_HOST']}/{short_url}")
			
		else:
			u = Url.objects.get(url=url)
			messages.info(request, f"{request.META['HTTP_HOST']}/{u.short_url}")
			
	return render(request, "url.html")
	
	
def main_url(request, str):
	u = Url.objects.get(short_url=str)
	return redirect(u.url)