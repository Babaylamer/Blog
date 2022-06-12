from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"
urlpatterns = [
    path("dashbord/",views.dashBord,name="dashbord"),
    path("addarticle/",views.AddArticle,name="addArticle"),
    path("article/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.updateArticle,name="update"),
    path("delete/<int:id>",views.deleteArticle,name="delete"),
    path("",views.articles,name="articles"),
    path("comment/<int:artid>",views.addComment,name="comment"),
]