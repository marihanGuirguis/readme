from django.http import JsonResponse
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 ,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
from .models import Book,Author,User,rates,Category
from django.db.models import Count,Sum,Avg,Q
from django.core.serializers.json import json
from django.core import serializers
from library.SignUpForm import SignUpForm
from library.EditUser import *
from django.contrib.auth.forms import PasswordChangeForm

def bookPage(request):

    data = get_object_or_404(Book, pk=2)
    str=data.picture.url.replace("library/", "../" ,1);

    context={'bookData':data ,'pic':str}
    return render(request, 'BookPg.html', context)

def home(request):

    return render(request, 'home.html')


def favourite(request ,which ):
    book=get_object_or_404(Book, name=which)
    if request.GET.get('data', None) == "off":
        book.Userfavourite.add(request.user)
        data = {
            'add_fav': "add"
        }
    elif request.GET.get('data', None) == "on":
         book.Userfavourite.remove(request.user)
    data = {
        'add_fav': "add"
    }
    book.save()

    return JsonResponse(data)

def rate(request , which):
    no= request.GET.get('data', None);
    book=get_object_or_404(Book, name=which)
    if(no == -1):
        rate=rates.objects.create(rate=no,user=request.user)
    else :
        re=rates.objects.filter(Q(book=book)| Q(user=request.user)).update(rate=no)
        rate=rates.objects.get(pk=re)

    book.usersRate.add(rate)
    book.save()

    data = {
        'add_fav': "done"
    }
    return JsonResponse(data)


def read(request ,which):
    wish=""
    book = get_object_or_404(Book, name=which)
    if request.GET.get('data', None) == "off":
        book.Userread.add(request.user)
        if request.user in book.UserwishList.all():
            book.UserwishList.remove(request.user)
            wish="and removed from wish list"
        data = {
            'add_fav': "add "+wish
        }
    elif request.GET.get('data', None) == "on":
        book.Userread.remove(request.user)
        data = {
            'add_fav': "remove"
        }
    book.save()

    return JsonResponse(data)

def wishlist(request ,which):
    book = get_object_or_404(Book, name=which)
    if request.GET.get('data', None) == "off":
        book.UserwishList.add(request.user)
        data = {
            'add_fav': "add"
        }
    elif request.GET.get('data', None) == "on":
        book.UserwishList.remove(request.user)
        data = {
            'add_fav': "remove"
        }
    book.save()

    return JsonResponse(data)


def follow(request ,who):
    author = get_object_or_404(Author, name=who)
    if (request.GET.get('data', None) == "off"):
        author.followers.add(request.user)
        data = {
            'add_fav': "add"
        }
    elif (request.GET.get('data', None) == "on"):
        author.followers.remove(request.user)
        data = {
            'add_fav': "remove"
        }
    author.save()

    return JsonResponse(data)

def categoryFollow(request ,type):
    category = get_object_or_404(Category, type=type)

    if (request.GET.get('data', None) == "off"):
        category.follow.add(request.user)
        data = {
            'add_fav': "add"
        }
    elif (request.GET.get('data', None) == "on"):
        category.follow.remove(request.user)
        data = {
            'add_fav': "remove"
        }
        category.save()

    return JsonResponse(data)





def getcategory(request):
    category = Category.objects.all()
    data_as_json=serializers.serialize('json',category)
    return HttpResponse(data_as_json,content_type="application/json")


def get_author(request):
    author = Author.objects.filter(followers=request.user.id)
    data_as_json=serializers.serialize('json',author)
    return HttpResponse(data_as_json,content_type="application/json")


def get_book(request):
    book = Book.objects.filter(Userfavourite=request.user.id)
    data_as_json=serializers.serialize('json',book)
    return HttpResponse(data_as_json,content_type="application/json")


def get_data(request):

    me = User.objects.get(pk=request.user.id)
    latest_category_list = Category.objects.all()
    authors_list = Author.objects.filter(followers=request.user.id)
    books_list = Book.objects.filter(Userfavourite=request.user.id)
    wish_list = Book.objects.filter(UserwishList=request.user.id)
    top_author = Author.objects.all().annotate(count=Count('followers')).order_by('-count')[:5]  # Done
    top_rated = Book.objects.values('name','picture').annotate(rateAVG=Avg('usersRate__rate'),countRaters=Count('usersRate__rate'))[:5]  # Done
    context = {'latest_category_list': latest_category_list, 'authors_list': authors_list, 'books_list': books_list, 'top_author': top_author, 'me':me, 'top_rated':top_rated,'wish_list':wish_list}
    return context


def index(request):
    context = get_data(request)
    for auth in context["top_author"]:
        auth.pic = auth.picture.url.replace("library/", "../", 1)

    for t in context["top_rated"]:
        t["pic"]=t["picture"].replace("library/", "../", 1)






    for wlist in context["wish_list"]:
        wlist.pic = wlist.picture.url.replace("library/", "../", 1)
    return render(request, 'home.html', context)


def categoryPage(request,type):
    category = Category.objects.get(type=type);
    books = Book.objects.filter(categories=category)
    context = get_data(request)
    context['category'] = category
    context['CatetegoryBooks'] = books
    str = category.pic.url.replace("library/", "../", 1);
    context['pic'] = str
    if request.user in category.follow.all():
        context['followValue'] = "on"
    else:
        context['followValue'] = "off"
    return render(request, 'category.html', context)


def who_author(request,who):
    author = Author.objects.get(name=who);
    books = Book.objects.filter(author=author)
    context = get_data(request)
    context['author'] = author
    context['authorBooks'] = books
    str = author.picture.url.replace("library/", "../", 1)
    context['pic'] = str
    if request.user in author.followers.all():
        context['followValue'] = "on"
    else:
        context['followValue'] = "off"

    related_author = Author.objects.filter(name__icontains=who)
    context["related_author"]=related_author
    return render(request, 'Author.html', context)


def get_all_author(request):
    authors = Author.objects.all()
    count=Author.objects.all().count()
    context = {}
    all_pic ={}
    for auth in authors:
        auth.pic=auth.picture.url.replace("library/", "../", 1)


    list = zip(authors, all_pic)
    context['lists'] = list
    context['authors'] = authors
    return render(request, 'all_author.html', context,all_pic)


def which_book(request, which):
    book = Book.objects.get(name=which)
    context = get_data(request)
    str = book.picture.url.replace("library/", "../", 1);
    context['bookData'] = book
    context['pic']=str
    if request.user in book.Userfavourite.all():
        context['favvalue']="on"
        context['favvalueText'] = "favorite"
    else:
        context['favvalue'] = "off"
        context['favvalueText'] = "unfavorite"
    if request.user in book.Userread.all():
        context['readvalue']="on"
        context['readvalueText'] = "read"
    else:
        context['readvalue'] = "off"
        context['readvalueText'] = "unread"
    if request.user in book.UserwishList.all():
        context['wishListvalue'] = "on"
        context['wishListvalueText'] = "wish"
    else:
        context['wishListvalue'] = "off"
        context['wishListvalueText'] = "unwish"
    rate=rates.objects.filter(Q(book=book) | Q(user=request.user))

    if rate:
        context['Ratevalue'] = rate[0].rate
    else:
        context['Ratevalue'] = -1

    related_books=Book.objects.filter(name__icontains=book.name)

    context["related_books"]=related_books
    return render(request, 'BookPg.html', context)


def searchPg(request,token):
    context=get_data(request)
    author = Author.objects.filter(name__icontains=token)
    book = Book.objects.filter(name__icontains=token)
    category = Category.objects.filter(type__icontains=token)

    for cat in category:
        cat.pic = cat.picture.url.replace("library/", "../", 1)
    for bo in book:
        bo.pic = bo.picture.url.replace("library/", "../", 1)
    for auth in author:
        auth.pic = auth.picture.url.replace("library/", "../", 1)
    context['by'] = token
    context['book'] = book
    context['author'] = author
    context['category'] = category
    return render(request, 'search.html', context)


def updateUser(request):
    # User.objects.filter(pk=request.user.id).update(username = username,email = email)
    # context = get_data(request)
    # context['me'] = request
    # user = authenticate(username=username, password=password)
    # login(request, user)
    # return render(request, 'profile.html', context)
    if request.method == "POST":
        form = Edit(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/library/profile')
        else:
            return HttpResponse(form.error_messages)
    else:
        form=Edit(instance=request.user)
        context=get_data(request)
        context['form']= form
        return render(request,'update.html',context)


def changePasswordUser(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save();
            update_session_auth_hash(request,form.user)
            return redirect('/library/profile')
        else:
            return HttpResponse(form.error_messages)
    else:
        form=PasswordChangeForm(user=request.user)
        context = get_data(request)
        context['form'] = form
        return render(request,'changePassword.html',context)


def profile(request):
    context = get_data(request)
    context['me'] = request.user
    for auth in context["authors_list"]:
        auth.pic = auth.picture.url.replace("library/", "../", 1)

    for book in context["books_list"]:
        book.pic = book.picture.url.replace("library/", "../", 1)

    for wlist in context["wish_list"]:
        wlist.pic = wlist.picture.url.replace("library/", "../", 1)

    return render(request, 'profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('templates/home.html')
    else:
        form=SignUpForm()

    return render(request,'registration/signup.html',{'form' : form})


