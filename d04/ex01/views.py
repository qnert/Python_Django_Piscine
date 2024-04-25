from django.shortcuts import render

# Create your views here.
def index(request):
  return(render(request, 'nav.html'))

def django(request):
  return (render(request, 'django.html'))

def display(request):
  return (render(request, 'display.html'))

def templates(request):
  return (render(request, 'templates.html'))
