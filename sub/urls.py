from django.conf.urls import url,include
from sub import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^register/$',views.register,name="register"),
    url(r'^volun/$',views.volun,name="volun"),
    url(r'^donate/$',views.donate,name="donate"),
    url(r'^pay/$',views.pay,name="pay"),
    url(r'^adform/$',views.adform,name="adform"),
    url(r'^adopt/$',views.adopt,name="adopt"),
    url(r'^action/$',views.action,name="action"),
    url(r'^laws/$',views.laws,name="laws"),
    url(r'^login/$', views.login, name="login"),
    url(r'^camp/$', views.campaign, name="camp"),
    url(r'^profile/$', views.profiles, name="profile"),
    path('rem/<str:title>/',views.rem,name='rem'),
    path('rem1', views.rem1, name='rem1'),
    url(r'^logout/$', views.logout, name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)