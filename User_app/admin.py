from django.contrib import admin
from User_app.models import User_Role, User_Login, User_Register
# Register your models here.
admin.site.register(User_Role)
admin.site.register(User_Register)
admin.site.register(User_Login)

