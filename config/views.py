from django.shortcuts import render

def main(request):
    return render( request, 'config/home.html' )