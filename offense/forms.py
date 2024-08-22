from django import forms
from .models import Offense


class OffenseForm(forms.ModelForm):
  class Meta:
    model = Offense
    fields = ['student', 'statement', 'conclusion', 'status']  # Update fields as needed
  
  def __init__(self, *args, **kwargs):
    super(OffenseForm, self).__init__(*args, **kwargs)
    # You can customize the form fields here
    self.fields['student'].disabled = True  # Disable student field for editing