from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Interested, Opportunity

class AddOpportunity(forms.Form):
    choices = [("Job", "Job"), ("Hackathon", "Hackathon"), ("Internship", "Internship")]
    title = forms.CharField(label="Title", max_length=100)
    company_name = forms.CharField(max_length=50, label="Company Name")
    description = forms.CharField(max_length=700, label="Description")
    eligibility = forms.CharField(max_length=50, label="Eligibility")
    link_to_apply = forms.CharField(max_length=1000, label="Link")
    type = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, label="Type")
    
    class Meta:
        model = Opportunity
    
    @transaction.atomic
    def save(self):
        opp = Opportunity()
        title = self.cleaned_data["title"]
        comp_name = self.cleaned_data["company_name"]
        descp = self.cleaned_data["description"]
        elig = self.cleaned_data["eligibility"]
        link = self.cleaned_data["link_to_apply"]
        job_type = self.cleaned_data["type"]
        
        opp.title = title
        opp.company_name = comp_name
        opp.description = descp
        opp.eligibility = elig
        opp.link_to_apply = link
        
        if job_type == "Job":
            opp.is_job = True
        
        if job_type == "Hackathon":
            opp.is_hackathon = True

        if job_type == "Internship":
            opp.is_internship = True

        opp.save()

        return opp

class EditOpportunity(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=100)
    company_name = forms.CharField(max_length=50, label="Company Name")
    description = forms.CharField(max_length=700, label="Description")
    eligibility = forms.CharField(max_length=50, label="Eligibility")
    link_to_apply = forms.CharField(max_length=200, label="Link")
    
    class Meta:
        model = Opportunity
        fields = ["title", "company_name", "description", "eligibility", "link_to_apply"]

class AddToInterested(forms.ModelForm):
    class Meta:
        model = Interested
        fields = ["user", "job", "date"]