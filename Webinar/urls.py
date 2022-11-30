from unicodedata import name
from django.urls import path, re_path

from django.contrib import admin
from matplotlib.pyplot import show
from.import views
urlpatterns = [
    path('', views.RegisterPage, name="register"),
    path("register/", views.UserRegister, name="register"),
    path("logout/", views.logout, name="logout"),
    path("login/", views.LoginPage, name="loginpage"),
    path("loginuser/", views.LoginUser, name="login"),
    # path("index/", views.Index, name="index"),
    path("admin1/", views.Admin, name="admin1"),
    path("app-profile/", views.Profile, name="profile"),
    path("Calculator/cha2ds2_vasc/", views.Clinical, name="cha"),
    path("hcpconnect/", views.Hcpconnect, name="hcpconnect"),
    path("hcpconnect/addblog/", views.Home, name="Hcpconnectt"),
    path("test/", views.Testing, name="testing"),
    path("Calculator/has_bled/", views.Mob, name="hassbled"),
    path("user/Webinar/", views.Upload, name="uploadapi"),
    path("archive/webinarlist/", views.Uploadvideo, name="webinarlist"),
    path("uploadvideo/", views.Help, name="testing"),
    path("user/Dashboard/", views.Indexx, name="index"),
    path("uploadwebinar/", views.Uploadwebinar, name="uploadwebinar"),
    path("index/livewebinarlist/", views.Happy, name="uploadwebinar1"),
    #  '''logic'''   
    path("clinical/", views.UploadClinical, name="clinical"),               

    path("logic/", views.Uploadcalcu, name="logic"),



]
