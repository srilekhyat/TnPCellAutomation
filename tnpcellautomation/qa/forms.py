from django import forms
from django.db import transaction
from .models import Question, Answer


"""
class AddQuestion(forms.Form):
    ques = forms.CharField(label="Question", max_length=1000)
    
    class Meta:
        model = Question

    
    @transaction.atomic
    def save(self):
        q = Question()
        ques = self.cleaned_data["ques"]
        
        q.ques = ques
        
        q.save()

        return q
"""

class AddQuestion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddQuestion, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Question
        fields = ["ques"]
    
    def save(self):
        instance = super(AddQuestion, self).save(commit=False)
        instance.user = self.user
        instance.save()
        return instance

class AnswerQuestion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.ques = kwargs.pop("ques", None)
        self.user = kwargs.pop("user", None)
        super(AnswerQuestion, self).__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ["ans"]

    def save(self):
        instance = super(AnswerQuestion, self).save(commit=False)
        instance.ques = self.ques
        instance.user = self.user
        instance.save()
        return instance