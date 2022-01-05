from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Topic, Concept

class AddConcept(forms.Form):
    concept = forms.CharField(max_length=100, label="Concept")
    image = forms.ImageField(label="Image")
    class Meta:
        model = Concept
        fields = ["concept", "image"]
    
    @transaction.atomic
    def save(self):
        c = Concept()
        c.concept = self.cleaned_data["concept"]
        c.image = self.cleaned_data["image"]
        c.save()
        return c

class EditConcept(forms.ModelForm):
    concept = forms.CharField(max_length=100, label="Concept")
    image = forms.ImageField(label="Image")
    
    class Meta:
        model = Concept
        fields = ["concept", "image"]

# class AddTopic(forms.Form):
#     #concept = forms.CharField(Concept, label="Concept", max_length=100)
#     topic = forms.CharField(label="Topic", max_length=100)
#     title1 = forms.CharField(label="Title1", max_length=500)
#     description1 = forms.CharField(label="Description1", max_length=3000)
#     title2 = forms.CharField(label="Title2", max_length=500)
#     description2 = forms.CharField(label="Description2", max_length=3000)
#     title3 = forms.CharField(label="Title3", max_length=500)
#     description3 = forms.CharField(label="Description3", max_length=3000)
    
#     class Meta:
#         model = Topic
    
#     @transaction.atomic
#     def save(self):
#         t = Topic()
#         concept = self.cleaned_data["concept"]
#         topic = self.cleaned_data["topic"]
#         title1 = self.cleaned_data["title1"]
#         description1 = self.cleaned_data["description1"]
#         title2 = self.cleaned_data["title2"]
#         description2 = self.cleaned_data["description2"]
#         title3 = self.cleaned_data["title3"]
#         description3 = self.cleaned_data["description3"]
        
#         t.concept = concept
#         t.topic = topic
#         t.title1 = title1
#         t.title2 = title2
#         t.title3 = title3
#         t.description1 = description1
#         t.description2 = description2
#         t.description3 = description3
    
#         t.save()

#         return t

class AddTopic(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.concept = kwargs.pop("concept", None)
        super(AddTopic, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Topic
        fields = ["topic", "title1", "description1", "title2", "description2", "title3", "description3"]
    
    def save(self):
        instance = super(AddTopic, self).save(commit=False)
        instance.concept = self.concept
        instance.save()
        return instance

class EditTopic(forms.ModelForm):
    #concept = forms.CharField(Concept, label="Concept", max_length=100)
    topic = forms.CharField(label="Topic", max_length=100)
    title1 = forms.CharField(label="Title1", max_length=500)
    description1 = forms.CharField(label="Description1", max_length=3000)
    title2 = forms.CharField(label="Title2", max_length=500)
    description2 = forms.CharField(label="Description2", max_length=3000)
    title3 = forms.CharField(label="Title3", max_length=500)
    description3 = forms.CharField(label="Description3", max_length=3000)
    
    class Meta:
        model = Topic
        fields = ["topic", "title1", "description1", "title2", "description2", "title3", "description3"]
