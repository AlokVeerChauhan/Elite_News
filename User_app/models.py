from django.db import models

# Create your models here.
class User_Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", unique=True)


class User_Register(models.Model):
    user_role_id = models.ForeignKey(User_Role, on_delete=models.CASCADE, default="")
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    user_mobile = models.CharField(max_length=255, default="")
    user_dob = models.CharField(max_length=255, default="")
    user_gender = models.CharField(max_length=10, default="")
    user_email = models.CharField(primary_key=True, max_length=255, default="")
    user_password = models.CharField(max_length=300, default="")
    conf_password = models.CharField(max_length=300, default="")
    login_time = models.CharField(max_length=255, default="")
    login_date = models.CharField(max_length=255, default="")
    logout_time = models.CharField(max_length=255, default="")


class User_Login(models.Model):
    user_role_id = models.ForeignKey(User_Role, on_delete=models.CASCADE, default="")
    user_email = models.ForeignKey(User_Register, primary_key=True, on_delete=models.CASCADE, default="")
    password = models.CharField(max_length=255, default="")


# python manage.py makemigrations User_app(App name)
# python manage.py migrate