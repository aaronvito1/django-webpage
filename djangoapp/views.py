import requests
from django.shortcuts import render


def index(request):
	content_html = open("djangoapp/templates/index.html").read()
	print('Index page being visited')
	context = {
		"content": content_html, 
	}
	return render(request, "index.html", context)

def about(request):
	content_html = open("djangoapp/templates/about.html").read()
	print('About page being visited')
	context = {
		"content": content_html, 
	}
	return render(request, "about.html", context)

def portfolio(request):
	content_html = open("djangoapp/templates/portfolio.html").read()
	print('Portfolio page being visited')
	response = requests.get('https://api.github.com/users/aaronvito1/repos')
	repos = response.json()
	context = {
		"content": content_html,
		'github_repos': repos, 
	}
	return render(request, "portfolio.html", context)

def extra(request):
	content_html = open("djangoapp/templates/extra.html").read()
	print('Extra page being visited')
	context = {
		"content": content_html, 
	}
	return render(request, "extra.html", context)

def blog(request):
	content_html = open("djangoapp/templates/blog.html").read()
	print('Blog page being visited')
	context = {
		"content": content_html, 
	}
	return render(request, "blog.html", context)

def contact(request):
	content_html = open("djangoapp/templates/contact.html").read()
	print('Contact page being visited')
	context = {
		"content": content_html, 
	}
	return render(request, "contact.html", context)

# def github_api(request):

#     return render(request, 'github.html', context)