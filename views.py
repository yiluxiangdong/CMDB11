#coding:utf-8
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
import hashlib
# uuuuuuuu

def user_vaild(username):
    if User.objects.filter(users=username):
        return True
    else:
        return False

def hash_passwd(password):
    hash_md5 = hashlib.md5()
    if isinstance(password,unicode):
        hash_md5.update(password.encode('utf-8'))
    passwd = hash_md5.hexdigest()
    return passwd

def  vaild_login(func):
    def inner(request,*args,**kwargs):
        username = request.session.get('username')
        if username:
            userData = User.objects.get(users=username)
            all_dict = {
                'users': userData.users,
                'passwd':userData.passwd,
                'name':userData.name,
                'city':userData.city,
                'email':userData.email,
                'phone':userData.phone,
            }
            request.session['userData'] = all_dict
            return func(request)
        else:
            return HttpResponseRedirect('/user/login')
    return inner

@vaild_login
def index(request):
    # username = request.COOKIES.get('user',None)
    # if request.session.get('userdata',''):
    #     return render_to_response('index.html',locals())
    # else:
    #     return HttpResponseRedirect('/user/login')
    username = request.session['userData']['users']
    return render_to_response('index.html',locals())
def login(request):
    if request.method=='POST' and request.POST:
        user = request.POST['name']
        passwd = request.POST['passwd']
        if user_vaild(user):
            pwd = User.objects.get(users = user).passwd
            if pwd == hash_passwd(passwd):
                response =  HttpResponseRedirect('/user/index/')
                response.set_cookie('user',user)
                request.session['username'] = user
                return response
            else:
                return HttpResponseRedirect('/user/login/')
        else:
            return HttpResponseRedirect('/user/login/')
    else:
        return render_to_response('signin.html', locals())






def register(request):
    username = request.POST.get('user')
    if  request.method == 'POST' and request.POST:
        if User.objects.filter(users=username):
            return render(request, '404.html')
        else:
            u = User()
            u.users = request.POST['user']
            u.passwd = hash_passwd(request.POST['passwd'])
            u.name = request.POST['name']
            u.city = request.POST['city']
            u.email = request.POST['email']
            u.phone = request.POST['phone']
            u.save()
            return redirect('/user/login')
    else:
        return render_to_response('signup.html',locals())