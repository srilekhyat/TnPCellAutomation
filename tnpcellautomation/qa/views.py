from django.db.models import query
from django.shortcuts import redirect, render
from .models import Answer, Question
from .forms import AddQuestion, AnswerQuestion

# Create your views here.
def qa_home(request):
    all_Qs = Question.objects.all()
    all_As = Answer.objects.all()
    print("Answers: ", all_As)
    answers = {}

    for q in all_Qs:
        ans = Answer.objects.filter(ques=q)
        answers[q] = ans

    if all_Qs:
        valid = 1
    else:
        valid = 0
    return render(request, "qa-home.html", context={"qa":"active", "questions": all_Qs, "answers": answers, "valid": valid})

def add_question(request):
    if request.method == "POST":
        form = AddQuestion(data=request.POST, user=request.user)
        print("Form = ", form)
        if form.is_valid():
            form.save()
            return redirect('qa')
    else:
        form = AddQuestion()
    return render(request, "add-ques.html", {"form": form, "qa": "active"})

def add_answer(request, id):
    q = Question.objects.get(id=id)
    if request.method == "POST":
        form = AnswerQuestion(request.POST, ques=q, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('qa')
    else:
        form = AnswerQuestion(ques=q, user=request.user)
    return render(request, "ans-ques.html", {"form": form, "qa": "active"})

def display_answers(request, id):
    q = Question.objects.get(id=id)
    answers = Answer.objects.filter(ques=q)
    if answers:
        valid = True
    else:
        valid = False

    context = {"question": q, "answers": answers, "qa": "active", "valid": valid}

    return render(request, "show-ans.html", context)