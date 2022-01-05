import io
from django.contrib.admin.sites import all_sites
from django.shortcuts import redirect, render
from stats.methods import Stats
from stats.models import Graph
from user.models import Student, Professor, User
from django.utils import timezone
from matplotlib import pyplot as plt
from PIL import Image

# Create your views here.
def get_all_logged_in_users():
    count = 0
    users = User.objects.all()

    for u in users:
        if u.is_authenticated:
            count += 1
    
    return count

def show_stats(request):
    if not request.user.is_authenticated:
        return redirect("login")
    #bwc, bw = get_stats()
    #print("BWC = ", bwc)
    #context = {"bwc": bwc, "bw": bw}
    active_users = get_all_logged_in_users()
    qp = Professor.objects.all()
    qs = Student.objects.all()
    CIVIL_studs = qs.filter(rollno__icontains="732")
    CSE_studs = qs.filter(rollno__icontains="733")
    EEE_studs = qs.filter(rollno__icontains="734")
    ECE_studs = qs.filter(rollno__icontains="735")
    MECH_studs = qs.filter(rollno__icontains="736")
    IT_studs = qs.filter(rollno__icontains="737")
    
    context = {
        "active_users": active_users,
        "stud_total": qs.count(),
        "prof_total": qp.count(),
        "IT": IT_studs.count(),
        "CSE": CSE_studs.count(),
        "stat": "active"
    }

    return render(request, "stats-page.html", context=context)
    #return render(request, "stats-page.html")

def show_total(request):
    s = Stats()
    interested_count, not_interested_count = s.get_interested()
    print("IC: ", interested_count)
    print("NIC: ", not_interested_count)
    context = {"Interested": interested_count, "Not_Interested": not_interested_count, "stat": "active"}
    return render(request, "stats-page.html", context=context)

def get_data(request):

    x = [1, 2, 3]
    y = [2, 4, 1]

    plt.plot(x, y)

    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.title("My First Graph!")

    plt.savefig("media/pic.png")

    return render(request, "display_graphs.html", context={"graph":"/media/pic.png", "title": "First Graph"})
