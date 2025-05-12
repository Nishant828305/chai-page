from django import forms
from .models import chaivariety

class ChaiVarietyForm(forms.Form):
  chai_variety = forms.ModelChoiceField(queryset=chaivariety.objects.all(),label="select chai variety")