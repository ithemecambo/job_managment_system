from django import forms
from job.models import *


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'font_awesome', 'logo_url']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required.')
        for category in Category.objects.all():
            if category.title == title:
                raise forms.ValidationError(title + ' is already created')
        return title


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'font_awesome', 'logo_url', 'status']


class SubCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'title', 'font_awesome', 'logo_url']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required.')
        return category

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required.')
        return title


class SubCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'title', 'font_awesome', 'logo_url', 'status']


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['account', 'name', 'company_industry', 'employee_num', 'company_type', 'founded',
                  'revenue', 'phone', 'fax', 'email', 'website', 'location', 'address', 'latitude',
                  'longitude', 'banner_url', 'logo_url', 'description']

    def clean_account(self):
        account = self.cleaned_data.get('account')
        if not account:
            raise forms.ValidationError('This field is required.')
        return account

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required.')
        return name


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['account', 'name', 'company_industry', 'employee_num', 'company_type', 'founded',
                  'revenue', 'phone', 'fax', 'email', 'website', 'location', 'address', 'latitude',
                  'longitude', 'banner_url', 'logo_url', 'status', 'description']


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'level', 'term', 'year_of_experience', 'function', 'hiring', 'salary', 'education',
                  'sex', 'age', 'marital_status', 'publish_date', 'closing_date', 'twitter', 'facebook',
                  'linkedin', 'instagram', 'status', 'premium', 'job_description', 'job_requirement', 'job_benefit']

    def clean_company(self):
        company = self.cleaned_data.get('company')
        if not company:
            raise forms.ValidationError('This field is required.')
        return company

    def clean_level(self):
        level = self.cleaned_data.get('level')
        if not level:
            raise forms.ValidationError('This field is required.')
        return level

    def clean_term(self):
        term = self.cleaned_data.get('term')
        if not term:
            raise forms.ValidationError('This field is required.')
        return term

    def clean_year_of_experiece(self):
        year_of_experience = self.cleaned_data.get('year_of_experience')
        if not year_of_experience:
            raise forms.ValidationError('This field is required.')
        return year_of_experience

    def clean_function(self):
        function = self.cleaned_data.get('function')
        if not function:
            raise forms.ValidationError('This field is required.')
        return function

    def clean_hiring(self):
        hiring = self.cleaned_data.get('hiring')
        if not hiring:
            raise forms.ValidationError('This field is required.')
        return hiring

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if not salary:
            raise forms.ValidationError('This field is required.')
        return salary


class JobUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['company', 'level', 'term', 'year_of_experience', 'function', 'hiring', 'salary', 'education',
                  'sex', 'age', 'marital_status', 'publish_date', 'closing_date', 'twitter', 'facebook',
                  'linkedin', 'instagram', 'status', 'premium', 'status', 'job_description', 'job_requirement',
                  'job_benefit']


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required.')
        return title
