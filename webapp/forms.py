from django.forms import ModelForm

from webapp.models import CaseSF


class CaseSFForm(ModelForm):
    class Meta:
        model = CaseSF
        fields = ['caseNumber', 'caseSubject', 'caseDescription', 'caseModule', 'aicorrect', 'datecompleted', 'completedBy']
