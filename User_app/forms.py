from django import forms
from User_app.models import User_Role, User_Register, User_Login

class UserRoleForm(forms.ModelForm):
    class Meta():
        model = User_Role
        exclude = ["role_name", "role_id"]


class UserRegisterForm(forms.ModelForm):
    class Meta():
        model = User_Register
        exclude = ["first_name", "last_name", "user_mobile", "user_dob", "user_gender", "user_email", "password", "conf_password", "login_time", "login_date", "logout_time"]


class UserLoginForm(forms.ModelForm):
    class Meta():
        model = User_Login
        exclude = ["email", "password"]
