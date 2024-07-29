from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,UserLoginForm,TodoForm,TodoUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Todos
# Create your views here.
class Home(View):
    def get(self,request):
        return render (request,'index.html')
class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'user_reg.html',{'form':form})
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            fname=form.cleaned_data.get("first_name")
            lname=form.cleaned_data.get("last_name")
            email=form.cleaned_data.get("email")
            uname=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
            messages.success(request,'Registered Successfully!')
            return redirect('home')
        else:
            messages.error(request,"invalid data")
            return redirect('home')
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render (request,'user_login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,"WELCOME")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials!")
            return redirect('log_view')
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect ('log_view')
class TodoAddView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,'add_todo.html',{'form':form})
    def post(self,request):
        if request.user.is_authenticated:
            form=TodoForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get("title")
                content=form.cleaned_data.get("content")
                user=request.user
                Todos.objects.create(title=title,content=content,user=user)
                messages.success(request,"Added")
                return redirect("home")
            else:
                messages.error(request,'invalid data')
                return redirect('add_view')
        else:
            messages.warning(request,"you must login fisrt!")
            return redirect ('log_view')
class TodoListView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            todo=Todos.objects.filter(user=request.user,status=False)
            return render(request,'todo_list.html',{'todo':todo})
        else:
            messages.warning(request,"you must login fisrt!")
            return redirect ('log_view')
class TodoDetailView(View):
    def get (self,request,*args,**kwargs):
        id=kwargs.get('id')
        todo=Todos.objects.get(id=id)
        return render(request,'todo_detail.html',{'todo':todo})
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect('list_view')
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        todo=Todos.objects.get(id=id)
        form=TodoUpdateForm(instance=todo)
        return render(request,'update_list.html',{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        todo=Todos.objects.get(id=id)
        form=TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list_view")


    