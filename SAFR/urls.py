
from django.urls import path
from.import views
from django.contrib.auth import views as authviews 

urlpatterns = [
path('',views.home,name="home"),
path('login/',views.userlogin,name="login"),
path('signUp/',views.signUp,name="signUp"),
path('visa/',views.visa,name="visa"),
path('creatorder/',views.Creatorder,name="creatorder"),
#path('logout/',views.userLogout,name="logout"),


path('reset_password/',authviews.PasswordResetView.as_view(),name="reset_password"),
path('password_reset/done/',authviews.PasswordResetDoneView.as_view(),name="password_reset_done"),
path('reset/<uidb64>/<token>/',authviews.PasswordResetConfirmView.as_view(),name="reset_password_confirm" ),
path('reset_password_complete/',authviews.PasswordResetCompleteView.as_view() ,name="reset_password_complete")
]