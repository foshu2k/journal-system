from django import forms
from . import DiaryLog

class DiaryLogForm(forms.ModelForm):
    class Meta:
        model = DiaryLog
        fields = ['title', 'content']