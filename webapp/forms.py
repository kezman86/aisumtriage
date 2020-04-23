from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm , forms

from webapp.models import CaseSF


class CaseSFForm(ModelForm):
    class Meta:
        model = CaseSF
        fields = ['caseNumber', 'caseSubject', 'caseDescription', 'caseModule', 'aicorrect', 'datecompleted', 'completedBy']

