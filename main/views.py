from django.shortcuts import render, redirect
import random
from .models import *
from django.contrib import messages


def shorturl(request):
	def gen_short(url):
		choice = "abcdefghijklmnopqrstuvwxyz0123456789"
		short = "".join(random.choices(choice, k=6))
		return short
		
	
	if request.method == "POST":
		
		url= request.POST.get("url")
		short_url = gen_short(url)
		if not Url.objects.filter(url=url).exists():
			Url.objects.create(
			      url=url, 
			      short_url=short_url
		        )
		else:
			pass         
		messages.info(request, f"{request.META['HTTP_HOST']}/{short_url}")	
		
	return render(request, "url.html")