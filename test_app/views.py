from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
from .forms import EmployerForm, FileForm, ExaminationForm
from .models import Employer, File, Examination


def index(request, employer_extra=1, file_extra=1):
    EmployerFormSet = modelformset_factory(Employer, form=EmployerForm, extra=employer_extra)
    FileFormSet = modelformset_factory(File, form=FileForm, extra=file_extra)
    ExaminationFormSet = modelformset_factory(Examination, form=ExaminationForm, extra=1)

    if request.method == "POST":
        employer_formset = EmployerFormSet(request.POST or None)
        file_formset = FileFormSet(request.POST or None)
        examination_formset = ExaminationFormSet(request.POST or None)
        if examination_formset.is_valid():
            for examination_form in examination_formset:
                examination_object = examination_form.save()
                if employer_formset.is_valid():
                    for employer_form in employer_formset:
                        employer_object = employer_form.save(commit=False)
                        employer_object.examination = examination_object
                        employer_form.save()
                else:
                    raise ValidationError('Validation error descry in EmployerFormSet')
                if file_formset.is_valid():
                    for file_form in file_formset:
                        file_object = file_form.save(commit=False)
                        file_object.examination = examination_object
                        file_form.save()
                else:
                    raise ValidationError('Validation error descry in FileFormSet')
            return redirect('index')
        else:
            raise ValidationError('Validation error descry in ExaminationFormSet')
    else:
        employer_formset = EmployerFormSet(queryset=Employer.objects.none())
        file_formset = FileFormSet(queryset=File.objects.none())
        examination_formset = ExaminationFormSet(queryset=Examination.objects.none())

    context = {
        'employer_formset': employer_formset,
        'file_formset': file_formset,
        'examination_formset': examination_formset,
        'employer_extra': employer_extra,
        'file_extra': file_extra,
    }
    return render(request, 'index.html', context)
