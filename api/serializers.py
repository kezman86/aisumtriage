from rest_framework import serializers
from webapp.models import CaseSF


class CaseSFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseSF
        fields = ['caseIDSf', 'caseNumber', 'caseSubject','caseDescription','caseModule']
