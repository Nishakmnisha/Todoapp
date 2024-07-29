from django import forms
from django.contrib.auth.models import User
from Todoapp.models import Todos

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"Email"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"})
        }
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"})
        }
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","content"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"Content"})
        }
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","content","status"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"Content"}),
            "status":forms.CheckboxInput(attrs={"class":"form-checkbox","placeholder":"status"})
        }