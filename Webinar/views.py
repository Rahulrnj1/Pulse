import email
import json
from email import message
from operator import index

import django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from matplotlib.pyplot import text
from requests import request
from rest_framework.response import Response

from Webinar.serializers import *

from .models import *
from rest_framework.decorators import api_view


@csrf_exempt
# Create your views here.
def RegisterPage(request):       # register.html view
    return render(request, 'app/register.html')


def UserRegister(request):   # view for registations
    if request.method == "POST":
        usertype = request.POST['usertype']
        fname = request.POST['fname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        state = request.POST['state']
        city = request.POST['city']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

      # First we will validate that user already exist

        user = User.objects.filter(email=email)
        if user:
            message = "User already exist"
            return render(request, "app/register.html", {'msg': message})
        else:
            if password == cpassword:
                newuser = User.objects.create(name=fname, email=email, mobile=mobile, state=state, city=city,
                                              password=password, user_type=usertype)
                message = "user register successfully"
                return render(request, "app/login.html")
            else:
                message = "password and confirm password Doesnot mantch"
                return render(request, "app/register.html", {'msg': message})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LoginPage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # checking emailid with database
        user = User.objects.get(email=email)

        if user:
            if user.password == password:
                # we are getting user data in session
                request.session['fname'] = user.name
                request.session['email'] = user.email

                return render(request, "app/index.html")
            else:
                message = "password Does not match"
                return render(request, "app/login.html", {'msg': message})
        else:
            message = "User does not exist"
            return render(request, "app/register.html", {'msg': message})

    else:
        return render(request, "app/login.html")


# login User
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LoginUser(request):
    print(request.POST)
    # if request.method == "POST":
    #      email = request.POST['email']
    #      password = request.POST['password']

    #       # checking emailid with database
    #      user = User.objects.get(email=email)

    #      if user:
    #           if user.password == password:
    #                # we are getting user data in session
    #                request.session['fname'] = user.name
    #                request.session['email'] = user.email
    #                return render(request,"app/index.html")
    #           else:
    #                message = "password Does not match"
    #                return render(request,"app/login.html",{'msg':message})
    #      else:
    #           message = "User does not exist"
    #           return render(request,"app/register.html",{'msg':message})


# def logout(request):
#     if request.session['email']:
#         request.session.flush()
#         return render(request, "app/login.html")
    # del request.session['email']
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url=None)


def logout(request):
    request.session.flush()
    return render(request, "app/login.html")
    try:
        del request.session['email']

    except:
        return redirect('login')
    return redirect('login')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='/login/')


def Index(request):

    return render(request, "app/index.html")
    # else:
    #      return render(request,"app/login.html")


def headerr(request):
    return render(request, "app/header.html")


# def Archave(request):
#      return render(request,"app/archive.html")


def Profile(request):
    return render(request, "app/app-profile.html")


def Admin(request):
    return render(request, "app/Admin/index.html")


@csrf_exempt
def Cha(request):
    return render(request, "app/cha.html")


# @csrf_exempt
# def Has(request):
#     return render(request, "app/hasbled.html")


# def Video(request):
#     return render(request, "app/uploadwebinar.html")


def Hcpconnect(request):
    mydata = HCPConnect.objects.all()
    serialzer = HCPConnectSerializer(mydata, many=True)
    # print(serialzer.data)
    template = loader.get_template('app/hcpconnect.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    # return Response({
    # 'mymembers': serialzer.data
    # })
    return HttpResponse(template.render(context, request))
    # return render(request,"app/hcpconnect.html")
# def result(request):
#      pass


def Home(request):
    if request.method == "POST":
        hcp_connect_title = request.POST.get('hcp_connect_title')
        hcp_connect_author = request.POST.get('hcp_connect_author')
        hcp_connect_date = request.POST.get('hcp_connect_date ')
        hcp_connect_description = request.POST.get('hcp_connect_description')
        hcp_connect_image = request.POST.get('hcp_connect_image')
        data = HCPConnect(Blog_title=hcp_connect_title, Blog_author=hcp_connect_author,
                          Blog_date=hcp_connect_date, Blog_description=hcp_connect_description, Blog_image=hcp_connect_image)
        data.save()
    return render(request, "app/addblog.html")


@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def Testing(request):
    mydata = HCPConnect.objects.all()
    serialzer = HCPConnectSerializer(mydata, many=True)
    # print(serialzer.data)
    template = loader.get_template('app/new.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))


@csrf_exempt
def Upload(request):
    mydata = WebinarList.objects.all()
    serialzer = WebinarListSerializer(mydata, many=True)
    # print(serialzer.data)
    template = loader.get_template('app/archive.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))


def Uploadvideo(request):
    if request.method == "POST":
        webinar_archive_title = request.POST.get('webinar_archive_title')
        webinar_archive_link = request.POST.get('webinar_archive_link')
        webinar_archive_date = request.POST.get('webinar_archive_date')
        webinar_archive_thumbnail = request.POST.get(
            'webinar_archive_thumbnail')
        data = WebinarList(webinar_title=webinar_archive_title, webinar_link=webinar_archive_link,
                           webinar_date=webinar_archive_date, webniar_image=webinar_archive_thumbnail)
        data.save()
    return render(request, "app/archive.html")


@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def Help(request):
    data = WebinarList.objects.all()
    serialzer = WebinarListSerializer(data, many=True)
    # print(serialzer.data)
    template = loader.get_template('app/old.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))


def Indexx(request):
    mydata = Livewebinar.objects.all()
    serialzer = LivewebinarSerializer(mydata, many=True)
    # print(serialzer.data)
    template = loader.get_template('app/index.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")

    return HttpResponse(template.render(context, request))


def Uploadwebinar(request):
    if request.method == "POST":
        webinar_archive_title = request.POST.get('webinar_archive_title')
        webinar_archive_link = request.POST.get('webinar_archive_link')
        webinar_archive_date = request.POST.get('webinar_archive_date')
        webinar_archive_thumbnail = request.POST.get(
            'webinar_archive_thumbnail')
        data = Livewebinar(webinar_title=webinar_archive_title, webinar_link=webinar_archive_link,
                           webinar_date=webinar_archive_date, webniar_image=webinar_archive_thumbnail)
        data.save()
    return render(request, "app/index.html")


@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def Happy(request):
    data = Livewebinar.objects.all()
    serialzer = LivewebinarSerializer(data, many=True)
    print(serialzer.data)
    template = loader.get_template('app/old.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))


def Clinical(request):
    mydata = ClinicalTool.objects.all()
    serialzer = ClinicalToolSerializer(mydata, many=True)
    print(serialzer.data)
    template = loader.get_template('app/cha.html')
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))


@api_view(('POST',))
def UploadClinical(request):
    if request.method == "POST":
        # patient_name = request.data.get('patient_name')
        # result_date = request.data.get('result_date')
        # age = request.data.get('age')

        patient_name = request.data.get('patient_name')
        user_id = request.data.get('user_id')
        result_date = request.data.get('result_date')
        age = int(request.data.get('age'))
        print("requesty", request.data)

        if (request.data.get('sex') == None):
            sex = 0
        else:
            sex = 1

        if (request.data.get('chf_history') == None):
            chf_history = 0
        else:
            chf_history = 1

        if (request.data.get('hypertension_history') == None):
            hypertension_history = 0
        else:
            hypertension_history = 1

        if (request.data.get('thromboembolism_history') == None):

            thromboembolism_history = 0

        else:

            thromboembolism_history = 1

        if (request.data.get('vascular_disease') == None):

            vascular_disease = 0

        else:

            vascular_disease = 1

        if (request.data.get('diabetes_history') == None):

            diabetes_history = 0

        else:

            diabetes_history = 1

        print("beforTor", age, sex, chf_history, hypertension_history,
              thromboembolism_history, vascular_disease, diabetes_history)
        total_points = age + sex + chf_history + hypertension_history + \
            thromboembolism_history + vascular_disease + diabetes_history
        print("afterTor", total_points)
        # total_points =6
        if (total_points == 0):

            risk_level = 'Low'
            thromboembolic_event_rate = '0%'
            treatment_recommendations = 'No antithrombotic treatment'
            stroke_risk_percentage = '0'

        elif (total_points == 1):

            risk_level = 'Intermediate'
            thromboembolic_event_rate = '0.46 -2.8%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class II, level \
                                            B) Non-vitamin K \
                                            antagonist oral  \
                                            anticoagulants  \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '1.3'

        elif (total_points == 2):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '2.2'

        elif (total_points == 3):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '3.2'

        elif (total_points == 4):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '4.0'

        elif (total_points == 5):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '6.7'

        elif (total_points == 6):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '9.8'

        elif (total_points == 7):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '9.6'

        elif (total_points == 8):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended chf_historyin  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '6.7'

        elif (total_points == 9):

            risk_level = 'High'
            thromboembolic_event_rate = '3.0-5.0%'
            treatment_recommendations = 'Oral anticoagulant is  \
                                            recommended for \
                                            stroke prevention in \
                                            AF (Class I, level A) \
                                            Non-vitamin K \
                                            antagonist oral \
                                            anticoagulants \
                                            (NOACs) are \
                                            recommended in  \
                                            preference to VKAs  \
                                            (Class I, level A). \
                                            VKA with INR goal  \
                                            2.0–3.0 in patients  \
                                            with mechanical \
                                            heart valves or  \
                                            moderate-to-severe  \
                                            mitral stenosis \
                                            (Class I, level B).'
            stroke_risk_percentage = '15.2'

        else:

            risk_level = ''
            thromboembolic_event_rate = ''
            treatment_recommendations = ''
            stroke_risk_percentage = ''

        data1 = {
            'patient_name': patient_name,
            'user_id': user_id,
            'result_date': result_date,
            'age': age,
            'sex': sex,
            'chf_history': chf_history,
            'hypertension_history': hypertension_history,
            'thromboembolism_history': thromboembolism_history,
            'vascular_disease': vascular_disease,
            'diabetes_history': diabetes_history,
            'total_score': total_points,
            'risk_level': risk_level,
            'thromboembolic_event_rate': thromboembolic_event_rate,
            'treatment_recommendations': treatment_recommendations,
            'stroke_risk_percentage': stroke_risk_percentage
        }
        print("datarrrrrrrrrrrr", data1)
        # data = ClinicalTool(data1)
        # data.save()
        template = loader.get_template('app/cha.html')
        context = {
            'mymembers': data1,
        }
        # print("success")
    return HttpResponse(template.render(context, request))

    return "data1"  # render(request, "app/cha.html")

@csrf_exempt
def Mob (request):
    mydata = Clinic.objects.all()
    serialzer = ClinicSerializer(mydata, many=True)
    print(serialzer.data)
    template = loader.get_template("app/hasbled.html")
    context = {
        'mymembers': serialzer.data,
    }
    print("success")
    return HttpResponse(template.render(context, request))

@api_view(('POST',))
def Uploadcalcu(request):
    if request.method == "POST":

        patient_name = request.data.get('patient_name')
        user_id = request.data.get('user_id')
        result_date = request.data.get('result_date')


        # def x_input():
        #     user = []
        #     for i in range(9):
        #         x = int(input("Enter Value:- "))
        #         user.append(x)
        #     return user

        print("request1: ", request.data.get('Hypertension'))

        if (request.data.get('Hypertension') == None):
            Hypertension = 0
        else:
            Hypertension = 1
        
        print("Hypertension: ", Hypertension)

        if (request.data.get('Renal disease') == None):
            Renal_disease = 0
        else:
            Renal_disease = 1
        
        if (request.data.get('Liver disease') == None):
            Liver_disease= 0 
        else:
            Liver_disease = 1
        
        if (request.data.get('Stroke history') == None):
            Stroke_history = 0
        else:
            Stroke_history = 1
        
        if (request.data.get('Prior major bleeding or predisposition to bleeding') == None):
            Prior_major_bleeding_or_predisposition_to_bleeding = 0
        else:
            Prior_major_bleeding_or_predisposition_to_bleeding = 1
        
        if (request.data.get('Labile INR') == None):
            Labile_INR= 0
        else:
            Labile_INR = 1
        
        if (request.data.get('Age >65') == None):
            Age_65 = 0
        else:
            Age_65 = 1
        
        if (request.data.get('Medication usage predisposing to bleeding') == None):
            Medication_usage_predisposing_to_bleeding = 0
        else:
            Medication_usage_predisposing_to_bleeding = 1
        
        if (request.data.get('Alcohol_use') == None):
            Alcohol_use = 0
        else:
            Alcohol_use = 1
        
        user = [Hypertension, Renal_disease, Liver_disease, Stroke_history, 
        Prior_major_bleeding_or_predisposition_to_bleeding, Labile_INR, Age_65, Medication_usage_predisposing_to_bleeding, 
        Alcohol_use
        ]
        

        result = {0: 'Risk was 0.9% in one validation study (Lip 2011) and 1.13 bleeds per 100 patient-years in another validation study (Pister 2010).\n\
Anticoagulation should be considered: Patient has a relatively low risk for major bleeding (~1/100 patient-years).',

          1: 'Risk was 3.4% in one validation study (Lip 2011) and 1.02 bleeds per 100 patient-years in another validation study (Pister 2010).\n\
Anticoagulation should be considered: Patient has a relatively low risk for major bleeding (~1/100 patient-years).',

          2: 'Risk was 4.1% in one validation study (Lip 2011) and 1.88 bleeds per 100 patient-years in another validation study (Pister 2010).\n\
Anticoagulation should be considered, however patient does have moderate risk for major bleeding (~2/100 patient-years).',

          3: 'Risk was 5.8% in one validation study (Lip 2011) and 3.72 bleeds per 100 patient-years in another validation study (Pisters 2010).\n\
Alternatives to anticoagulation should be considered: Patient is at high risk for major bleeding.',

          4: 'Risk was 8.9% in one validation study (Lip 2011) and 8.70 bleeds per 100 patient-years in another validation study (Pisters 2010).\n\
Alternatives to anticoagulation should be considered: Patient is at high risk for major bleeding.',

          5: 'Risk was 9.1% in one validation study (Lip 2011) and 12.50 bleeds per 100 patient-years in another validation study (Pisters 2010).\n\
Alternatives to anticoagulation should be considered: Patient is at high risk for major bleeding.',

          6: 'Scores greater than 5 were too rare to determine risk, but are likely over 10%.\n\
Alternatives to anticoagulation should be considered: Patient is at very high risk for major bleeding.'

          }


        def get_score(x):

            field = {'Hypertension': x[0], 'Renal_disease': x[1], 'Liver_disease': x[2],
             'Stroke_history': x[3], 'Prior_major_bleeding_or_predisposition_to_bleeding': x[4],
             'Labile_INR': x[5], 'Age_65': x[6], 'Medication_usage_predisposing_to_bleeding': x[7],
             'Alcohol_use': x[8]}

            y = sum(field.values())

            return "{} points".format(y), result[y], field


        x = get_score(user)
        # print(x[0])
        # print(x[1])
        print("data",x)
      
    template = loader.get_template('app/hasbled.html')
    context = {
            'mymembers': x[2],
        }
        # print("success")
    return HttpResponse(template.render(context, request))

