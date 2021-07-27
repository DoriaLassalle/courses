from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):   
     
    context={
        "allcourses":Course.objects.all()
    }  
    
    return render(request, 'index.html', context)


def addCourse(request): 
    errorsFromModel=Course.objects.course_validator(request.POST)    
   
    if len(errorsFromModel)>0:
        for key, value in errorsFromModel.items():
            messages.error(request,value)

        return redirect("/")
    else:
        description=request.POST["description"] 
        Description.objects.create(description=description) #primero creo la instacia de description
        descr=Description.objects.last()#obtengo la que se acaba de crear
        
        courseName=request.POST["courseName"]
        Course.objects.create(course_name=courseName, description=descr)#le paso la instancia de description recien creada
        messages.success(request, f"Thanks! {courseName} has been added.")

        return redirect("/")


def destroyCourse(request, id):
    courseToConfirm=Course.objects.get(id=id)
    course=courseToConfirm.course_name
    descr=courseToConfirm.description.description

    context={
        "course": course,
        "descr": descr,
        "id": id
    }

    return render(request, "remove.html", context)


def deleteCourse(request, id):
    courseToDelete=Course.objects.get(id=id)
    courseToDelete.delete()
    messages.success(request, f"{courseToDelete.course_name} has been deleted :(")
   
    return redirect("/")
    


def deleteAjax(request, id):
    courseToDelete=Course.objects.get(id=id)
    courseToDelete.delete()     
    
    return JsonResponse({"accion":"borrado"})


def commentForm(request, id):
    courseToComment=Course.objects.get(id=id)
    allComments=courseToComment.comments.all()
   
    context={
        "courseName": courseToComment.course_name,
        "desc":courseToComment.description.description,
        "id":id,
        "allComments": allComments           
    }
 
    return render(request, "comment.html", context)
    

def makeComment(request,id):
    currentCourse=Course.objects.get(id=id)
    user=request.POST["user"]
    comment=request.POST["comment"]
    Comment.objects.create(user=user, comment=comment, course=currentCourse)#le pasola instancia de curso
    messages.success(request, "Your comment has been created")

    return redirect(f"/courses/comment/{id}")



