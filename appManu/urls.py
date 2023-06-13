"""
URL configuration for graphql_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from appManu import views as viewManu
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView #View for the user interface
from graphql_tutorial.schema import schema #Schema we want to query

urlpatterns = [
    path('admin/', admin.site.urls),
    # This URL will provide a user interface that is used to query the database
    # and interact with the GraphQL API.
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path("manu/telefoni",viewManu.telefono),
    path("manu/libri",viewManu.libri),
    path("manu/city",viewManu.city),
    path("manu/cd",viewManu.cd),
    path("manu/cd/anno=<anno>",viewManu.displayAnno, name = "displayAnno"),
    path("manu/cd/id=<id>",viewManu.displayIdCd, name = "displayIdCd"),


    path("manu/libri/titolo=<titolo>",viewManu.displayTitolo, name = "displayTitolo"),
    path("manu/libri/id=<id>",viewManu.displayId, name = "displayId")
    

]