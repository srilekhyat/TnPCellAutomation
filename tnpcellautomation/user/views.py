import os
from django.shortcuts import render, redirect

from qa.models import Question
from learningmaterial.models import Concept
from .forms import StudentSignUpForm, ProfessorSignUpForm, StudentUpdateForm
from .models import Student, User
from opportunities.models import Interested, Opportunity

# Create your views here.
def home_view(request):
    return render(request, "home.html", context={"home": "active"})

def register_view(request):
    return render(request, "register.html", context={"register": "active"})

def student_register_view(request):
    if request.method == "POST":
        formUser =  StudentSignUpForm(request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('login')
    else:
        formUser = StudentSignUpForm()
    return render(request, "studentregister.html", {"register_form": formUser, "register": "active"})

def prof_register_view(request):
    if request.method == "POST":
        formUser =  ProfessorSignUpForm(request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('login')
    else:
        formUser = ProfessorSignUpForm()
    return render(request, "profregister.html", {"register_form": formUser, "register": "active"})

def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect("login")

    is_myprofile = False

    user_liked_opps = None
    user_asked_ques = None

    if request.user.username == username:
        is_myprofile = True
        curr_user = request.user
        all_opps = Interested.objects.all()
        all_ques = Question.objects.all()
        user_liked_opps = all_opps.filter(user=curr_user)
        user_asked_ques = all_ques.filter(user=curr_user)
        print("ULO:", user_liked_opps)
    else:
        user = User.objects.get(username=username)
        curr_user = Student.objects.get(user=user)    
        is_myprofile = False

    print("CU: ", curr_user)
    s = Student.objects.get(user=curr_user)
    print("S = ", s)
    if request.method == "POST":
        formUser =  StudentUpdateForm(data=(request.POST or None), files=(request.FILES or None), instance=s)
        if formUser.is_valid():
            formUser.save()
            return redirect('home')
    else:
        formUser = StudentUpdateForm(files=(request.FILES or None), instance=s)
    
    return render(request, "profile.html", context={"form": formUser, "isMyProfile": is_myprofile, "profile": "active", "liked_opps": user_liked_opps, "asked_ques": user_asked_ques})

def search_users(request):
    if not request.user.is_authenticated:
        return redirect("login")
    try:
        search_query = request.POST.get("q")
    except Exception as e:
        return render(request, "errorpage.html")
    all_users = User.objects.get_queryset()
    search_results = []
    for u in all_users:
        if search_query in str(u):
            search_results.append(u)
            #s = Student.objects.get(user=u)
            #search_results.append(s)
    print(search_results)
    context = {"search_results": search_results}
    return render(request, "search.html", context=context)

    
