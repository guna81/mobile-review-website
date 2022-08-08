from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import * 
from django.db.models import Count, Avg


# Create your views here.
def home(request):
    user = request.user
    brands = Brand.objects.all()
    latest = Latest.objects.all()
    p_mobiles = PopularMobiles.objects.all()
    p_compare = PopularComparisions.objects.all()
    r_mobiles = RecentMobiles.objects.filter(user__username=user.username).order_by('-id')[0:4]
    r_compare = RecentComparisions.objects.filter(user__username=user.username).order_by('-id')[0:2]
    
    context = {
        'user':user,
        'brands':brands,
        'latest':latest,
        'r_mobiles':r_mobiles,
        'p_mobiles':p_mobiles,
        'r_compare':r_compare,
        'p_compare':p_compare
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == "POST":
        first_name=request.POST["firstname"]
        last_name=request.POST["lastname"]
        username=request.POST["username"]
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({"success":False, "msg":"Username Already Taken"})
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        if not password==password2:
            return JsonResponse({"success":False, "msg":"Password Doesn't Match"})
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return JsonResponse({"success":True, "msg":"Registered. You Can Now Login"})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return JsonResponse({"success":True})
        return JsonResponse({"success":False, "msg":"Invalid Credentials"})

def logout_view(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not logged in")
    logout(request)
    print('logged out')
    return JsonResponse({'msg':'Logged Out'})

def mobile_list(request,brand_name):
    user = request.user
    brands = Brand.objects.all()
    if request.method == "POST":
        model = request.POST["mobile"]
        models = Spec.objects.filter(model__name__contains=model)
    else:
        models = Spec.objects.filter(model__brand__name=brand_name)
    latest = Latest.objects.all()
    context = {
        'user':user,
        'models':models,
        'latest':latest,
        'brands':brands,
        
    }
    return render(request, 'mobile_list.html', context)

def mobile_details(request,model_name):
    user = request.user
    models = None
    if request.method == "POST":
        model = request.POST["mobile2"]
        models = Model.objects.filter(name__contains=model)
    
    specs = Spec.objects.get(model__name=model_name)
    if request.user.is_authenticated:
        old = RecentMobiles.objects.filter(model__name=model_name)
        if old:
            old.delete()
        r_mobiles = RecentMobiles(model=Model.objects.get(name=model_name), user=user)
        r_mobiles.save()
    varients = Varient.objects.filter(model__name=model_name)
    reviews = Review.objects.filter(mobile__name=model_name)
    try :
        Review.objects.get(user=request.user, mobile__name=model_name)
        reviewed = True
    except:
        reviewed = False
    brands = Brand.objects.all()
    latest = Latest.objects.all()
    context = {
        'user':user,
        'specs':specs,
        'varients':varients,
        'brands':brands,
        'latest':latest,
        'models':models,
        'reviews':reviews,
        'reviewed':reviewed
    }
    return render(request, 'mobile_details.html', context)

def compare_mobile(request,mobile1,mobile2):
    user = request.user
    specs1 = Spec.objects.get(model__name=mobile1)
    specs2 = Spec.objects.get(model__name=mobile2)
    if request.user.is_authenticated:
        old = RecentComparisions.objects.filter(mobile1__name=mobile1, mobile2__name=mobile2)
        if old:
            old.delete()
        r_compare = RecentComparisions(mobile1=Model.objects.get(name=mobile1), mobile2=Model.objects.get(name=mobile2), user=request.user)
        r_compare.save()
    varients1 = Varient.objects.filter(model__name=mobile1)
    varients2 = Varient.objects.filter(model__name=mobile2)
    brands = Brand.objects.all()
    latest = Latest.objects.all()
    context = {
        'user':user,
        'latest':latest,
        'specs1':specs1,
        'specs2':specs2,
        'varients1':varients1,
        'varients2':varients2
    }
    return render(request, 'compare_mobile.html',context)

def write_review(request, mobile):
    if request.method == "POST":
        rating = request.POST['rating']
        review = request.POST['review']
        reviews = Review(rating=rating, review=review, user=request.user, mobile=Model.objects.get(name=mobile))
        reviews.save()
        avg_rating = Review.objects.filter(mobile__name=mobile).aggregate(Avg('rating'))
        model = Model.objects.get(name=mobile)
        model.avg_rating = round(avg_rating['rating__avg'], 1)
        model.save()
        data = {
            'success':True
        }
        return JsonResponse(data)