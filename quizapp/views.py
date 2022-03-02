from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import registration_form, login_form, addquesform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return render(request=request, template_name="quizapp/home.html")
from .models import quesmodel


def reg(request):
    if request.method == "POST":
        print("Reached to post data")
        filled_form = registration_form(request.POST)
        if filled_form.is_valid():

            registered_user = filled_form.cleaned_data["username"]
            registered_email = filled_form.cleaned_data["email"]
            registered_pass = filled_form.cleaned_data["password1"]
            try:
                User.objects.get(Q(email=registered_email))
                status = "Email already registered"
                form = registration_form()
                return render(request, "quizapp/register.html", {"form": form, "status": status})

            except User.DoesNotExist:
                print("Reached except")
                # register_user=User.objects.create_user(username=registered_user,email=registered_email,password=registered_pass)
                register_user_obj = User.objects.create_user(username=registered_user, email=registered_email,
                                                             password=registered_pass)
                register_user_obj.save()
                print("data saved in  database")
                return redirect('log')  # it goes into login view

    # get request
    form = registration_form()
    my_form = {"form": form}
    return render(request=request, template_name="quizapp/register.html", context=my_form)


def log(request):
    if request.method == "POST":
        print("Reached login post")
        filled_form = login_form(request.POST)
        if filled_form.is_valid():
            reg_email = filled_form.cleaned_data["login_email"]
            reg_pass = filled_form.cleaned_data["login_password"]
            try:
                print("reached try")
                user_data = User.objects.get(email=reg_email)
                print("reached try-1")
                user = authenticate(request, username=user_data.username, password=reg_pass)
                print("reached authenication", user)
                if user is not None:
                    login(request, user)
                    print("reached log if")
                    return redirect('quiz')
                else:
                    print("Reached else")
                    status = "Login Details mismatch"
                    form = login_form()
                    my_form = {"form": form, "status": status}
                    return render(request=request, template_name="quizapp/home.html", context=my_form)
            except User.DoesNotExist:
                print("Reached except")
                status = "User not registered"
                form = login_form()
                my_form = {"form": form, "status": status}
                return render(request=request, template_name="quizapp/home.html", context=my_form)
        else:
            form = login_form()
            my_form = {"form": form}
            return render(request=request, template_name="quizapp/home.html", context=my_form)

    form = login_form()
    my_form = {"form": form}
    return render(request=request, template_name="quizapp/home.html", context=my_form)


def log_out(request):
    logout(request)
    return redirect('log')


def quiz(request):
    return render(request=request, template_name="quizapp/quiz.html")


def play(request):
    if request.method == "POST":
        print("Reached post")
        filled_form = addquesform(request.POST)
        if filled_form.is_valid():
            print("Reached if")
            questions = quesmodel.objects.all()
            score = 0
            wrong = 0
            correct = 0
            total = 0
            for q in questions:
                total += 1
                if q.answer == request.POST.get(q.question):
                    score += 10
                    correct += 1
                    print("Reached another if")
                else:
                    wrong += 1
            percentage = score / (total * 10) * 100
            my_form = {
                'score': score,
                'wrong': wrong,
                'correct': correct,
                'total': total,
                'percentage': percentage
            }
            print("Reached database")
            reg_ans = filled_form.save()
            return redirect('result')

    else:
        questions = quesmodel.objects.all()
        my_form = {"questions": questions}
        return render(request=request, template_name="quizapp/play.html", context=my_form)

    form = addquesform()
    my_form = {"form": form}
    return render(request=request, template_name="quizapp/result.html", context=my_form)


def result(request):
    return render(request=request, template_name="quizapp/result.html")
