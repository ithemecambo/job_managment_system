from django import forms
from candidate.models import *


class CandidateCreateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['account', 'position', 'expect_salary', 'total_of_experience', 'high_education', 'job_type',
                  'skill', 'twitter', 'facebook', 'linkedin', 'instagram', 'curriculum', 'candidate_vision']

    def clean_account(self):
        account = self.cleaned_data.get('account')
        if not account:
            raise forms.ValidationError('This field is required.')
        return account

    def clean_position(self):
        position = self.cleaned_data.get('position')
        if not position:
            raise forms.ValidationError('This field is required.')
        return position

    def clean_total_of_experience(self):
        total_of_experience = self.cleaned_data.get('total_of_experience')
        if not total_of_experience:
            raise forms.ValidationError('This field is required.')
        return total_of_experience

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')
        if not job_type:
            raise forms.ValidationError('This field is required.')
        return job_type

    def clean_skill(self):
        skill = self.cleaned_data.get('skill')
        if not skill:
            raise forms.ValidationError('This field is required.')
        return skill

