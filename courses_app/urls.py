from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add", views.addCourse),    
    path("courses/destroy/<id>", views.destroyCourse),
    path("courses/delete/<id>", views.deleteCourse),
    path("back", views.index),
    path("courses/comment/<id>", views.commentForm),
    path("courses/make_comment/<id>", views.makeComment),
    path('deleteAjax/<id>', views.deleteAjax)
   
]