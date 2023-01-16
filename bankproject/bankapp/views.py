
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout as deauth
from django.contrib.auth.models import User
from .models import *




# Create your views here.
from.models import District,Branch
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        print(username  , password , cpassword)
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                print("else working")
                user=User.objects.create_user(username=username,password=password)
                print(user)
                user.save()
                return redirect('user-login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")







def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'invalid credentials')
            return redirect('user-login')


    return render(request,"login.html")

def newpage(request):
    return render(request,"newpage.html")

#
# def form(request):
#     district=District.objects.all()
#     branch=Branch.objects.all()
#     return render(request,"form.html",{'district':district,'branch':branch})



def form(request):
    if not request.user.is_authenticated:
        return redirect('user-login')

    if request.method == 'POST':
        name = request.POST.get('name')
        month = request.POST.get('month')
        day = request.POST.get('day')
        year = request.POST.get('year')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        account_type = request.POST.get('account_type')
        materials_provide = request.POST.get('materials')
        Branch_id = request.POST.get('Branch_id')
        District_id = request.POST.get('district')

        print("name" , name)
        print("month" , month)
        print("day", day)
        print("year", year)
        print("gender", gender)
        print("age", age)
        print("phone", phone)
        print("email", email)
        print("address",address)
        print("account_type",account_type)
        print("materials_provide",materials_provide)
        print("Branch_id",Branch_id)
        print("District_id",District_id)

        user = request.user
        District_id = District.objects.get(id=District_id)
        Branch_id = Branch.objects.get(id=Branch_id)

        Applicationform.objects.create(
            user  =   user,
            name =   name,
            month =  month ,
            day =  day ,
            year =  year ,
            gender = gender  ,
            age =   age,
            phone =  phone ,
            email =  email ,
            address =  address ,
            account_type =  account_type ,
            materials_provide =  materials_provide ,
            Branch_id =   Branch_id,
            District_id =District_id
        )
        return redirect('msg')

    district = District.objects.all()
    context = {
         'district': district
    }
    return render(request,'form.html',context)
def get_branches(request):
    print("get_branch")
    get_district = request.GET.get('district')
    print(get_district)
    get_object = District.objects.filter(id=get_district).first()
    print(get_district)

    all_branches=Branch.objects.filter(district=get_object)
    print(all_branches)
    context={

        'all_branches': all_branches
    }
    return render(request , 'partials/branches.html' , context)

def msg(request):
    return render(request,"msg.html")

def logout(request):
    deauth(request)
    messages.success(request , "You are Logout Successfully")
    return redirect('demo')


# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
#
# # Create your views here.
# from .models import District,Branch
#
#
#
# def home(request):
#     return render(request,'home.html')
# def logout(request):
#
#     return redirect('/')
#
# def form(request):
#     district=District.objects.all()
#     branch=Branch.objects.all()
#     return render(request,'form.html',{'district':district,'branch':branch})
#
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#
#         if user is not None:
#             auth.login(request,user)
#             return render(request,'newpage.html')
#         else:
#             messages.info(request,'Invalid credentials')
#             return redirect('login')
#
#
#
#     return render(request,"login.html")
#
#
#
#
#
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#
#         password=request.POST['password']
#         cpassword=request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"Username taken")
#                 return redirect('register')
#
#             else:
#                  user=User.objects.create_user(username=username,password=password)
#                  user.save()
#                  return redirect('login')
#
#         else:
#             messages.info(request,"password not matching")
#             return redirect('register')
#         return redirect('/')
#
#     return render(request,"register.html")
#
#
# def newpage(request):
#     return render(request, "newpage.html")
#
# def message(request):
#     return render(request,"message.html")