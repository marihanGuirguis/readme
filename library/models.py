from django.db import models
from django.contrib.auth.models import User

class rates(models.Model):
    rate = models.IntegerField()
    user =models.ForeignKey(User ,on_delete=models.CASCADE ,default=1)


class Author(models.Model):
    name = models.CharField(max_length=100)
    Bio = models.TextField(max_length=200)
    country = models.CharField(max_length=100)
    picture = models.ImageField(default='au.jpg', upload_to="library/static/library")
    Born_at = models.DateField()
    Diad_at = models.DateField()
    followers = models.ManyToManyField(User)

    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture=models.ImageField(upload_to="library/static/library")
    published_at= models.DateField()
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    categories=models.ManyToManyField('Category')
    UserwishList=models.ManyToManyField(User ,related_name="wishList")
    Userread=models.ManyToManyField(User,related_name="read")
    Userfavourite=models.ManyToManyField(User,related_name="favourite")
    usersRate=models.ManyToManyField(rates)

    def __str__(self):
        return self.name



class Category(models.Model):
    category_choice = (("Action","Action"), ("mystry",'Mystory'), ("horor",'Horor'), ("novel",'Novel'), ("funny",'Funny'), ("comedy",'Comedy'));
    #category_choice=("Action","Mystry","horror","novel","comedy");
    Description = models.TextField(max_length=100 ,default="film Category")
    pic = models.ImageField(upload_to="library/static/library")
    type = models.CharField(max_length=10, choices=category_choice)
    follow=models.ManyToManyField(User)

    def __str__(self):
        return self.type

class UserPhoto(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    userPic=models.ImageField(default='au.jpg',upload_to="library/static/library")