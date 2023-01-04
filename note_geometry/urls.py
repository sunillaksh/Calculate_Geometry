from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    
    path('notes', views.notes, name='notes'),
    path('notedetail/<id>', views.notedetail, name='notedetail'),
    path('notedelet/<id>', views.notedelet, name="notedelet"),
    path('notecreate/', views.notecreate, name="notecreate"),
    path('noteedit/<id>', views.noteedit, name="noteedit"),
    path('noteedit/savenoteedit/<id>', views.savenoteedit, name="savenoteedit"),

]