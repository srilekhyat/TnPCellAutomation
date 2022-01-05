from django.db.transaction import commit
from django.shortcuts import redirect, render

from learningmaterial.forms import AddConcept, EditConcept, AddTopic, EditTopic
from learningmaterial.models import Concept, Topic

# Create your views here.
def learning_material_home(request):
    concepts = Concept.objects.all()
    if concepts:
        valid = True
    else:
        valid = False
    if not request.user.is_authenticated:
        return redirect("login")
        
    return render(request, "lm-home.html", context={"lm": "active", "concepts": concepts, "valid": valid})

def add_concept(request):
    if request.method == "POST":
        form = AddConcept(data=(request.POST or None), files=(request.FILES or None))
        if form.is_valid():
            form.save()
            return redirect('lrng_mtrl')
    else:
        form = AddConcept(files=(request.FILES or None))
    return render(request, "add-concept.html", {"form": form, "lm": "active"})

def edit_concept(request, id):
    found = True
    obj = None

    try:
        obj = Concept.objects.get(id=id)
    except Exception as e:
        found = False

    if request.method == "POST":
        form = EditConcept(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("lrng_mtrl")

    form = EditConcept(instance=obj)
    return render(request, "edit-concept.html", {"form": form, "lm": "active"})

def delete_concept(request, id):
    try:
        obj = Concept.objects.get(id=id)
        obj.delete()
    except Exception as e:
        found = False

    return render(request, "delete-concept-page.html", context={"lm": "active"})

def topics_view(request, id):
    if not request.user.is_authenticated:
        return redirect("login")

    concept = Concept.objects.get(id=id)
    topics = Topic.objects.filter(concept=concept)

    if topics:
        valid = True
    else:
        valid = False
    print("Concept = ", concept)
    print("Topics: ", topics)

    return render(request, "lmtopics-base.html", context={"lm": "active", "topics": topics, "id": id, "valid": valid})

def topic_info(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    topic = Topic.objects.get(id=id)
    return render(request, "lm-info.html", context={"lm": "active", "topic": topic})

def add_topic(request, id):
    concept = Concept.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = AddTopic(data=(request.POST or None), files=(request.FILES or None), concept=concept)
        if form.is_valid():
            form.save()
            return redirect('lrng_mtrl')
    else:
        form = AddTopic(files=(request.FILES or None), concept=concept)
    return render(request, "add-topic.html", context={"lm": "active", "form": form})

def edit_topic(request, id):
    found = True
    obj = None

    try:
        obj = Topic.objects.get(id=id)
    except Exception as e:
        found = False

    if request.method == "POST":
        form = EditTopic(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("lrng_mtrl")

    form = EditTopic(instance=obj)
    return render(request, "edit-concept.html", {"form": form, "lm": "active"})

def delete_topic(request, id):
    try:
        obj = Topic.objects.get(id=id)
        obj.delete()
    except Exception as e:
        found = False

    return render(request, "delete-topic-page.html", context={"lm": "active"})