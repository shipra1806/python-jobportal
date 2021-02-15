from django.contrib import admin
from django.urls import path
from  jobportal import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
    path('signin',views.signin),
    path('saveSignUp',views.saveSignUp),
    path('checkLogin',views.checkLogin),
    path('logout',views.logout),
    path('dashboard',views.dashboard),
    path('jobopening',views.jobopening),
    path('search/<slug:type>/<slug:id>',views.search),
    path('viewcandidate/<slug:id>',views.viewcandidate),
    path('apply/<slug:id>',views.apply),
    path('addtofav/<slug:id>',views.addtofav),
    path('postjob',views.postjob),
    path('appliedjobs',views.appliedjobs),
    path('removefav/<slug:id>',views.removefav),
    path('sendmail',views.sendmail),
    path('chgpwd',views.chgpwd),
    path('savejob',views.savejob),
    path('changepassword',views.changepassword)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)