from django.shortcuts import redirect, render
from opportunities.models import Interested, Opportunity
from opportunities.forms import AddOpportunity, EditOpportunity
from user.models import User

# Create your views here.

def display(request):
    if not request.user.is_authenticated:
        return redirect("login")

    all_opps = Opportunity.objects.all()
    interested = []
    not_interested = []

    for j in all_opps:
        print("J = ", j.title)
        isPresent = Interested.objects.filter(user=request.user, job=j)
        if isPresent:
            interested.append(j)
        else:
            not_interested.append(j)

    context = {"opportunities": all_opps, "interested": interested, "not_interested": not_interested, "opp_page": "active"}
    print("Context = ", context)
    return render(request, "display.html", context=context)

def add_opportunity(request):
    if request.method == "POST":
        form = AddOpportunity(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = AddOpportunity()
    return render(request, "add-opp.html", {"form": form, "opp_page": "active"})

def add_to_interests(request, id):
    opp = Opportunity.objects.get(id=id)
    user = request.user

    if not Interested.objects.filter(user=user, job=opp).exists():
        i = Interested(user=user, job=opp)
        i.save()
    return display(request)

def remove_from_interests(request, id):
    curr_user = request.user
    opp = Opportunity.objects.get(id=id)
    i = Interested.objects.filter(user=curr_user, job=opp)
    i.delete()
    return display(request)


def edit_opportunity(request, id):
    found = True
    obj = None

    try:
        obj = Opportunity.objects.get(id=id)
    except Exception as e:
        found = False

    if request.method == "POST":
        form = EditOpportunity(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("display")

    form = EditOpportunity(instance=obj)
    return render(request, "edit-op.html", {"form": form, "opp_page": "active"})

def delete_opportunity(request, id):
    try:
        obj = Opportunity.objects.get(id=id)
        obj.delete()
    except Exception as e:
        found = False

    return render(request, "opp-delete-page.html", context={"opp_page": "active"})