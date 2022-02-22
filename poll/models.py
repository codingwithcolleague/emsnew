from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.TextField(null=True,blank=True)
    status =models.CharField(default='inactive' ,null=True,blank=True,max_length=200)
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.title} { self.created_by } "

    @property
    def choices(self):
        return self.choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.text} "

    @property
    def votes(self):
        return self.answer_set.count()
    

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.user.first_name + "-" + self.choice.text