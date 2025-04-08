from django.shortcuts import render
from .models import Project
# Create your views here.


def portfolio(request):
    projects = Project.objects.all()#Para listar todos los obejtos dentro del modelo Project
    return render(request, "portfolio/portfolio.html",{"projects":projects})