from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    project_started = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    project =  models.ForeignKey(Project , on_delete=models.CASCADE)

    def __str__(self):
        return self.name