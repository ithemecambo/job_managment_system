from datetime import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.safestring import mark_safe

from account.models import Account

EMPLOYEE_NUM_CHOICES = (
    ('N1', '<10'),
    ('N2', '10~50'),
    ('N3', '50~100'),
    ('N4', '100~200'),
    ('N5', '>200'),
    ('N6', '>500'),
    ('N7', '>1000')
)

JOB_STATUS_CHOICES = (
    ('AP', 'Approved'),
    ('PD', 'Pending'),
    ('EP', 'Expire'),
    ('RJ', 'Rejected')
)

PREMIUM_CHOICES = (
    ('UT', 'Urgent'),
    ('FT', 'Featured'),
    ('HL', 'Highlight')
)

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('MF', 'Male/Female')
)

LEVEL_CHOICES = (
    ('EL', 'Entry Level'),
    ('MD', 'Middle'),
    ('SE', 'Senior'),
    ('TP', 'Top'),
    ('FG', 'Fresh Graduate')
)

SKILL_LEVEL_CHOICES = (
    ('PR', 'Poor'),
    ('FR', 'Fair'),
    ('GD', 'Good'),
    ('EL', 'Excellent'),
    ('MT', 'Mother Tongue')
)

MARITAL_STATUS_CHOICES = (
    ('SL', 'Single'),
    ('MR', 'Married'),
    ('DD', 'Divorced'),
    ('ST', 'Separated'),
    ('WN', 'Window'),
    ('OT', 'Others')
)


def is_empty(self):
    if self is None:
        return True
    return False


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class City(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name')
    name_kh = models.CharField(max_length=100, verbose_name='Khmer Name')
    logo_url = models.ImageField(upload_to='cities/', blank=True, null=True, verbose_name='Logo',
                                 help_text='Allowed size is 10MB')
    code = models.CharField(max_length=5, null=True, verbose_name='Code')

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name}'


class JobType(BaseModel):
    title = models.CharField(max_length=50, verbose_name='Title')

    class Meta:
        verbose_name_plural = 'JobTypes'

    def __str__(self):
        return f'{self.title}'


class Category(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title')
    font_awesome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Font Awesome')
    logo_url = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Icon',
                                 help_text='Allowed size is 10MB')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    title = models.CharField(max_length=100, verbose_name='Title')
    font_awesome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Font Awesome')
    logo_url = models.ImageField(upload_to='subcategories/', blank=True, null=True, verbose_name='Icon',
                                 help_text='Allowed size is 10MB')

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return f'{self.title}'

    def get_category(self):
        return f'{self.category.title}'
    get_category.short_description = 'Category'


class CompanyType(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Company Name')

    class Meta:
        verbose_name_plural = 'CompanyTypes'

    def __str__(self):
        return f'{self.name}'


class CompanyManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(company_industry__icontains=query) |
                         Q(phone__icontains=query) |
                         Q(website__icontains=query) |
                         Q(location__icontains=query) |
                         Q(address__icontains=query) |
                         Q(description__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Company(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    name = models.CharField(max_length=150, verbose_name='Company Name')
    company_industry = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Company Industry')
    employee_num = models.CharField(choices=EMPLOYEE_NUM_CHOICES, default='~', max_length=10,
                                    verbose_name='Employee Number')
    company_type = models.ForeignKey(CompanyType, on_delete=models.CASCADE, verbose_name='Company Type')
    founded = models.CharField(max_length=6, verbose_name='Founded')
    revenue = models.CharField(max_length=50, verbose_name='Revenue')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    fax = models.CharField(max_length=20, blank=True, null=True, verbose_name='Fax')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    website = models.CharField(max_length=50, blank=True, null=True, verbose_name='Website')
    location = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')
    address = models.CharField(max_length=250, verbose_name='Address')
    latitude = models.CharField(max_length=20, verbose_name='Latitude')
    longitude = models.CharField(max_length=20, verbose_name='Longitude')
    banner_url = models.ImageField(upload_to='companies/banners/%Y-%m-%d/', blank=True, null=True,
                                   verbose_name='Banner', help_text='Allowed size is 100MB')
    logo_url = models.ImageField(upload_to='companies/logos/%Y-%m-%d/', blank=True, null=True,
                                 verbose_name='Logo', help_text='Allowed size is 10MB')
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    objects = CompanyManager()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        if is_empty(self.name):
            return ''
        return f'{self.name}'

    def profile(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.logo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

    def get_absolute_url(self):
        return reverse('company-details', kwargs={
            'company_industry': self.company_industry.title.replace('/', '-'),
            'pk': self.id
        })


class Education(BaseModel):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = 'Educations'

    def __str__(self):
        return f'{self.name}'


class JobManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
                    Q(company__name__icontains=query) |
                    Q(level__icontains=query) |
                    Q(term__icontains=query) |
                    Q(year_of_experience__icontains=query) |
                    Q(function__icontains=query) |
                    Q(hiring__icontains=query) |
                    Q(salary__icontains=query) |
                    Q(education__icontains=query) |
                    Q(sex__icontains=query) |
                    Q(age__icontains=query) |
                    Q(status__icontains=query) |
                    Q(premium__icontains=query) |
                    Q(job_description__icontains=query) |
                    Q(job_requirement__icontains=query)
                )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Job(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company')
    level = models.CharField(choices=LEVEL_CHOICES, max_length=3, default='Entry Level', verbose_name='Level')
    term = models.ForeignKey(JobType, on_delete=models.CASCADE, verbose_name='Term')
    year_of_experience = models.IntegerField(default=1, blank=True, null=True, verbose_name='Year of Experience')
    function = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Function')
    hiring = models.IntegerField(default=1, blank=True, null=True, verbose_name='Hiring')
    salary = models.CharField(max_length=20, default='Negotiable', blank=True, null=True, verbose_name='Salary')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name='Education')
    sex = models.CharField(choices=SEX_CHOICES, max_length=3, default='Male/Female', verbose_name='Sex')
    age = models.CharField(max_length=10, default='~', blank=True, null=True, verbose_name='Age')
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=3, default='Single',
                                      verbose_name='Marital Status')
    publish_date = models.DateField(default=timezone.now, verbose_name='Publish Date')
    closing_date = models.DateField(default=timezone.now, verbose_name='Closing Date')
    twitter = models.CharField(max_length=120, blank=True, null=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=120, blank=True, null=True, verbose_name='Facebook')
    linkedin = models.CharField(max_length=120, blank=True, null=True, verbose_name='LinkedIn')
    instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')
    status = models.CharField(choices=JOB_STATUS_CHOICES, max_length=3, default='Approved', verbose_name='Status')
    premium = models.CharField(choices=PREMIUM_CHOICES, max_length=3, default='Urgent', verbose_name='Premium')
    job_description = models.TextField(blank=True, null=True, verbose_name='Job Description')
    job_requirement = models.TextField(blank=True, null=True, verbose_name='Job Requirement')
    job_benefit = models.TextField(blank=True, null=True, verbose_name='Benefit')

    objects = JobManager()

    class Meta:
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return f'{self.level} {self.function}'

    def get_company(self):
        return f'{self.company.name}'
    get_company.short_description = 'Company'

    def replace_function(self):
        return f"{self.function.replace('/', '_')}"

    def profile(self):
        if self.company.logo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.company.logo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

    def remaining_day(self):
        date_format = '%Y-%m-%d'
        current_date = datetime.strptime(str(datetime.now().date()), date_format)
        closing_date = datetime.strptime(str(self.closing_date), date_format)
        delta = closing_date - current_date
        if delta.days <= 0:
            return 'Expire'
        else:
            return f'{delta.days} Days'
    remaining_day.short_description = 'Remaining Day'

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={
            'function': self.function.title.replace('/', '-'),
            'pk': self.id
        })


class Todo(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.title}'


class CompanyRating(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company')
    rating_num = models.IntegerField(default=1, verbose_name='Rating Num')
    text = models.TextField(verbose_name='Text')

    class Meta:
        verbose_name_plural = 'CompanyRatings'

    def __str__(self):
        return f'{self.account}, {self.company}'

    # ⭐ ★☆ 💫
    def rating(self):
        if self.rating_num == 1:
            return '⭐'
        elif self.rating_num == 2:
            return '⭐⭐'
        elif self.rating_num == 3:
            return '⭐⭐⭐'
        elif self.rating_num == 4:
            return '⭐⭐⭐⭐'
        elif self.rating_num == 5:
            return '⭐⭐⭐⭐⭐'
        else:
            return '⭐⭐⭐⭐⭐'

