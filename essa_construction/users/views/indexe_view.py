from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch

def home_redirect(request):
	"""Redirect the site root to the public homepage.

	Tries to reverse the named route 'public_home'. If that name is not defined,
	falls back to '/' to avoid server errors.
	"""
	try:
		url = reverse('public_home')
	except NoReverseMatch:
		url = '/'
	return redirect(url)
