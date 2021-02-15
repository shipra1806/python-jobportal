from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from .Forms import *
from  jobportal import settings
from django.conf import settings
from django.core.mail import send_mail
import smtplib
import ssl
# Create your views here.
def sendmail(request):
    port = settings.EMAIL_PORT
    smtp_server = settings.EMAIL_HOST
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    receiver_email = 'shree.industries7@gmail.com'
    subject = 'Website registration'
    body = 'Activate your account.'
    message = 'Subject: {}\n\n{}'.format(subject, body)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return redirect('/')
def index(request):
    context={};
    context['homeactive']="active"
    context['testimonials']=Testimonials.objects.filter(status='approved');
    return render(request,"index.html",context)
def signup(request):
    context = {};
    context['signupactive'] = "active"
    context['header']="Sign Up "
    context['msg'] = ""
    context['form'] = SignupForm()
    context['target']="saveSignUp"
    return render(request, "signup.html", context)
def signin(request):
    context = {};
    context['signinactive'] = "active"
    context['header']="Sign In "
    context['msg'] = ""
    context['form'] = SigninForm()
    context['target']="checkLogin"
    return render(request, "signup.html", context)
def saveSignUp(request):
    context={}
    form =  SignupForm(request.POST or None)
    if(form.is_valid()):
        form.save();
        context['signinactive'] = "active"
        context['msg']="Registration Successfull! Please Login"
        context['form'] = SigninForm()
        context['target'] = "checkLogin"
        return render(request,"signup.html",context)
    else:
      context['msg'] = "Registration Failed! Please Try Again"
      context['signupactive'] = "active"
      context['signupform'] = SignupForm()
      context['target'] = "saveSignUp"
      return render(request, "signup.html", context)
def checkLogin(request):
    context={}
    form=SigninForm(request.POST or None)
    if(form.is_valid()):
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        check = Seeker.objects.raw('SELECT * from seeker where email=\''+email +'\' and password =\''+password+'\'')
        if(len(list(check))>0):
            context['dashboardactive'] = "active"
            request.session['seeker']=email
            return  redirect('/dashboard');
        else:
            context['signinactive'] = "active"
            context['header'] = "Sign In "
            context['msg'] = "Login failed"
            context['form'] = SigninForm()
            context['target'] = "checkLogin"
            return  render(request,"signup.html",context);
    else:
        return HttpResponse('error')
def dashboard(request):
    context={}
    context['dashboardactive'] = "active"
    context['jobopenings'] = JobOpenings.objects.all();
    context['locations']=Location.objects.all();
    context['job_type']=JobTypes.objects.all()
    context['skills']=KeySkills.objects.all()
    context['experience']=Experience.objects.all();
    context['designation']=Designation.objects.all();
    context['a_o_s'] = AreaOfSectors.objects.all();
    if request.session.has_key('seeker'):
        context['seeker'] = request.session['seeker']
        return render(request, "dashboard.html", context);
    else:
        return redirect('/');

def logout(request):
    del request.session['seeker']
    response=redirect('/')
    return response
def jobopening(request):
    context={}
    return render(request,"jobopening.html",context)
def search(request,type,id):
    context = {}
    context['dashboardactive'] = "active"
    context['jobopenings'] = JobOpenings.objects.raw('SELECT * from job_openings where '+type+'_id='+id+'')
    context['locations'] = Location.objects.all();
    context['job_type'] = JobTypes.objects.all()
    context['skills'] = KeySkills.objects.all()
    context['experience'] = Experience.objects.all();
    context['designation'] = Designation.objects.all();
    context['a_o_s']=AreaOfSectors.objects.all();
    if request.session.has_key('seeker'):
        context['seeker'] = request.session['seeker']
        return render(request, "dashboard.html", context);
    else:
        return redirect('/');
def viewjob(request,id):
    context = {}
    context['jobopenings'] = JobOpenings.objects.raw('SELECT * from job_openings where id=' + id + '')
    context['locations'] = Location.objects.all();
    context['job_type'] = JobTypes.objects.all()
    context['skills'] = KeySkills.objects.all()
    context['experience'] = Experience.objects.all();
    context['designation'] = Designation.objects.all();
    context['a_o_s'] = AreaOfSectors.objects.all();
    context['dashboardactive'] = "active"
    if request.session.has_key('seeker'):
        context['seeker'] = request.session['seeker']
        isapplied = JpApplayJob.objects.raw('SELECT * from jp_applay_job where s_email=\'' + request.session['seeker'] + '\' and job_id='+id)
        isfav = JpFavJob.objects.raw('SELECT * from jp_fav_job where s_email=\'' + request.session['seeker'] + '\' and job_id='+id)
        context['isapplied']=len(list(isapplied));
        context['isfav'] = len(list(isfav));
        return render(request, "singlejob.html", context);
    else:
        return redirect('/');
def apply(request,id):
    #context['dashboardactive'] = "active"
    seeker=request.session['seeker']
    app=JpApplayJob()
    app.job_id=id;
    app.s_email=seeker
    app.save();
    return redirect('/viewjob/'+id);
def addtofav(request,id):
    #context['dashboardactive'] = "active"
    seeker = request.session['seeker']
    app = JpFavJob()
    app.job_id = id;
    app.s_email = seeker
    app.save();
    return redirect('/viewjob/' + id);
def removefav(request,id):
    
    seeker = request.session['seeker']
    app = get_object_or_404(JpFavJob, job_id=id,s_email=seeker)
    app.delete();
    return redirect('/viewjob/' + id);
def appliedjobs(request):
    context = {}
    context['appliedjobactive'] = "active"
    context['locations'] = Location.objects.all();
    context['job_type'] = JobTypes.objects.all()
    context['skills'] = KeySkills.objects.all()
    context['experience'] = Experience.objects.all();
    context['designation'] = Designation.objects.all();
    context['a_o_s'] = AreaOfSectors.objects.all();
    if request.session.has_key('seeker'):
        context['seeker'] = request.session['seeker']
        seeker=request.session['seeker']
        context['jobopenings'] = JobOpenings.objects.raw(
            'SELECT * from job_openings where id in (select job_id from jp_applay_job where s_email=\'' + seeker + '\')')
        return render(request, "dashboard.html", context);
    else:
        return redirect('/');


def favjobs(request):
    context = {}
    context['favjobactive'] = "active"
    context['locations'] = Location.objects.all();
    context['job_type'] = JobTypes.objects.all()
    context['skills'] = KeySkills.objects.all()
    context['experience'] = Experience.objects.all();
    context['designation'] = Designation.objects.all();
    context['a_o_s'] = AreaOfSectors.objects.all();
    if request.session.has_key('seeker'):
        context['seeker'] = request.session['seeker']
        seeker = request.session['seeker']
        context['jobopenings'] = JobOpenings.objects.raw(
            'SELECT * from job_openings where id in (select job_id from jp_fav_job where s_email=\'' + seeker + '\')')
        return render(request, "dashboard.html", context);
    else:
        return redirect('/');
def chgpwd(request):
    context={}
    context['chgpwdactive']="active"
    if request.session.has_key('seeker'):
        seeker = request.session['seeker'];
        context['seeker'] = seeker
        form = SigninForm(initial={"email":seeker})
        context['form'] = form

        return render(request, "chgpwd.html", context);
    else:
        return redirect('/')
def changepassword(request):
    context={}
    obj=SigninForm(request.POST or None)
    context['chgpwdactive'] = "active"
    seeker = request.session['seeker'];
    context['seeker'] = seeker
    form = SigninForm(initial={"email": seeker})
    context['form'] = form

    if(obj.is_valid()):
        email=obj.cleaned_data.get("email")
        pwd=obj.cleaned_data.get("password")
        data=Seeker.objects.raw("select * from seeker where email='"+email+"' and password='"+pwd+"'")
        if(data):
            npwd=request.POST['npwd']
            rpwd=request.POST['rpwd']
            if(npwd==rpwd):
                emp = Seeker.objects.get(email=email)
                emp.password = npwd
                emp.save();
                context['msg']="Password update successfully"
                return render(request, "chgpwd.html", context)
            else:
                context['msg']="Password and retype password doesn't match"
                return render(request, "chgpwd.html", context)
        else:
            context['msg']="Password incorrect"
            return render(request, "chgpwd.html", context)
    else:
        return render(request, "chgpwd.html", context)
