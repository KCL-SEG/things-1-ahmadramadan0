from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Things</title>
    </head>
    <body>
        <h1>Things</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
