from django.forms import ModelForm
from .models import Employer, File, Examination


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = [
            'lastname',
            'name',
            'surname',
            'position',
            'punishment'
        ]


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['data']


class ExaminationForm(ModelForm):
    class Meta:
        model = Examination
        fields = [
            'title',
            'mark',
            'limitations',
            'plan_file',
        ]

