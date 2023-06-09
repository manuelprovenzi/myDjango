from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Telefono
from .models import Libro
from .models import Cd
from django.core import serializers

from django.template.response import TemplateResponse
from .xmlFile import XMLSerializer as Serializer

def telefono(request):
  myphone = Telefono.objects.all().values()
  template = 'all_telefoni.html'
  context = {
    'myphone': myphone,
  }
  return TemplateResponse(request,template,context)

def libri(request):
  
  libros = Libro.objects.all().values()
  if len(libros)<1:
    #load data
    listLibri = loadLibri("C:/Users/Utente/OneDrive/Desktop/python/testServer/appManu/libri_cd.xml")   
    
    libros = Libro.objects.all().values()
  
  libriJson = serializers.serialize("json",Libro.objects.all())
  template = 'all_libri.html'
  context = {
    'libros': libros,
    'libriJson':libriJson
  }
  return TemplateResponse(request,template,context)


def loadLibri(path):
  sl = Serializer(path)
  listLibri = sl.listLibri
  for l in listLibri:
    libroModel = Libro()
    libroModel.parse(attributes= l.attributes) 
    libroModel.save()
    
  return listLibri 
  
  
def cd(request):
  
  cds = Cd.objects.all().values()
  if len(cds)<1:
    #load data
    listCd = loadCd("C:/Users/Utente/OneDrive/Desktop/python/testServer/appManu/libri_cd.xml")   
    
    cds = Cd.objects.all().values()
  
  template = 'all_cd.html'
  context = {
    'cds': cds,
    
  }
  return TemplateResponse(request,template,context)


def loadCd(path):
  sc = Serializer(path)
  listCd = sc.listCD
  for c in listCd:
    cdModel = Cd()
    cdModel.parse(attributes= c.attributes) 
    cdModel.save()
    
  return listCd 
    
    
    
def displayId(request,id):
  objSelected = Libro.objects.filter(id = id)
  template = 'all_libri.html'
  context = {
    'libros': objSelected.all().values(), 
  }
  
  return TemplateResponse(request,template,context)


def displayTitolo(request,titolo):
  objSelected = Libro.objects.filter(titolo = titolo)
  template = 'all_libri.html'
  context = {
    'libros': objSelected.all().values(), 
  }
  
  return TemplateResponse(request,template,context)



def displayAnno(request,anno):
  objSelected = Cd.objects.all().filter(anno=anno)
  template = "all_cd.html"
  context = {
    'cds':objSelected
  }
  return TemplateResponse(request,template,context)


def displayIdCd(request,id):
  objSelected = Cd.objects.all().filter(id=id)
  template = "all_cd.html"
  context = {
    'cds':objSelected
  }
  return TemplateResponse(request,template,context)