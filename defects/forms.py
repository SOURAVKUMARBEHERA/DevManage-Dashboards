from django import forms
from defects.models import defectsData


class DefectEditForm(forms.ModelForm):
    defect_ID=forms.CharField(max_length=100,disabled=True)
    defectName=forms.CharField(max_length=100,disabled=True)
    class Meta:
        model=defectsData
        fields =['defect_ID','defectName','assigned_by','assigned_to', 'description','defect_status','priority',]


class AddDefectForm(forms.ModelForm):
    class Meta:
        model=defectsData
        fields="__all__"
