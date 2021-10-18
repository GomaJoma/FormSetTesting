from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
from .forms import EmployerForm, FileForm, ExaminationForm
from .models import Employer, File, Examination


def index(request):
    EmployerFormSet = modelformset_factory(Employer, form=EmployerForm)
    FileFormSet = modelformset_factory(File, form=FileForm)
    ExaminationFormSet = modelformset_factory(Examination, form=ExaminationForm)

    if request.method == "POST":
        employer_formset = EmployerFormSet(request.POST or None, prefix='employer')
        file_formset = FileFormSet(request.POST or None, request.FILES, prefix='file')
        examination_formset = ExaminationFormSet(request.POST or None, request.FILES, prefix='examination')
        if examination_formset.is_valid():
            for examination_form in examination_formset:
                examination_object = examination_form.save()
                if employer_formset.is_valid():
                    for employer_form in employer_formset:
                        employer_object = employer_form.save(commit=False)
                        employer_object.examination = examination_object
                        employer_form.save()
                else:
                    raise ValidationError(employer_formset.errors)
                    # raise ValidationError(employer_formset.error_messages)
                    # raise ValidationError(employer_formset.non_form_errors()
                if file_formset.is_valid():
                    for file_form in file_formset:
                        file_object = file_form.save(commit=False)
                        file_object.examination = examination_object
                        file_form.save()
                else:
                    # raise ValidationError(file_formset.errors)
                    raise ValidationError(file_formset.error_messages)
                    # raise ValidationError(file_formset.non_form_errors())
            print(request.POST)
            return redirect('index')
        else:
            raise ValidationError(examination_formset.errors)
            # raise ValidationError(examination_formset.error_messages)
            # raise ValidationError(examination_formset.non_form_errors())
    else:
        employer_formset = EmployerFormSet(queryset=Employer.objects.none(), prefix='employer')
        file_formset = FileFormSet(queryset=File.objects.none(), prefix='file')
        examination_formset = ExaminationFormSet(queryset=Examination.objects.none(), prefix='examination')

    context = {
        'employer_formset': employer_formset,
        'file_formset': file_formset,
        'examination_formset': examination_formset,
        'em_fs_len': range(len(employer_formset)),
    }
    return render(request, 'index.html', context)
