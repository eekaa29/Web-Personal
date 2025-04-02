from django.shortcuts import render, HttpResponse
html_base = """
<h1>Mi web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/"</a>Contact</a></li>
<ul>
"""
# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    """)

def about_me(request):
    return HttpResponse(html_base + """
        <h2>About me</h2>
        <p>Me llamo Ekaitz, tengo 21 años y soy desarrollador de software</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portfolio</h2>
        <p>Aquí mostraré todos mis proyectos</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contact</h2>
        <p>Aquí tenéis mi email para poneros en contacto conmigo: <a href="mailto:ekamartinc2003@gmail.com">ekamartinc2003@gmail.com</a></p>
    """)