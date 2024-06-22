from django import forms
from .models import VisionTest

class VisionTestForm(forms.ModelForm):
    class Meta:
        model = VisionTest
        fields = ['left_eye', 'right_eye']
