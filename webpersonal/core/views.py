from django.shortcuts import render, HttpResponse

html_base = """

<h1>mi web 1</h1>
<ul>
    <li><a href="/">portada </a> </li>
    <li><a href="/about">about-me</a> </li>
    <li><a href="/portafolio">Portafolio</a> </li>
    <li><a href="/contacto">Contacto</a> </li>
</ul>

"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def portafolio(request):
    return render(request,"core/portafolio.html")

def contacto(request):
    return HttpResponse(html_base + "<h1>mi web 1</h1><h2>Contacto</h2><p>Contacto</p>")