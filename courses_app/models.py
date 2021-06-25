from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def course_validator(self, data):
        errors={}

        if len(data["course_name"]) < 5:
            errors["courseName"]="Course name should be at least 5 characters"
        
        if len(data["description"]) < 15:
            errors["desc"]="Description should be at least 15 characters"
    
        return errors


class Description(models.Model):
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #course

    def __repr__(self):
        return f"Comment from {self.description}"
    

class Course(models.Model):
    course_name=models.CharField(max_length=255)
    description=models.ForeignKey(Description, related_name="course", on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #comments
    objects=CourseManager() #vinculando el validador a la clase

    def __repr__(self):
        return f"Curso: {self.course.name}"


class Comment(models.Model):
    user=models.CharField(max_length=255)
    comment=models.TextField()
    course=models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Comment from {self.user}"