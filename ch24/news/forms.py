from django import forms

class report(forms.Form):
    Name_anchor=forms.CharField()
    year_experience=forms.IntegerField()
    Domain=forms.CharField()
    age=forms.IntegerField()