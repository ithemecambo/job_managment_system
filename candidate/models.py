from job.models import *

SKILL_LEVEL_CHOICES = (
    ('PR', 'Poor'),
    ('FR', 'Fair'),
    ('GD', 'Good'),
    ('EL', 'Excellent'),
    ('MT', 'Mother Tongue')
)


class Language(BaseModel):
    name = models.CharField(max_length=70, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Languages'

    def __str__(self):
        return f"{self.name}"


class LanguageLevel(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='Job')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Language')
    level = models.CharField(choices=SKILL_LEVEL_CHOICES, max_length=5, default='Good', verbose_name='Level')

    class Meta:
        verbose_name_plural = 'LanguageLevels'

    def __str__(self):
        return f'{self.job}, {self.language}'


class Skill(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title')

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.title}'


class CandidateManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(position__icontains=query) |
                         Q(expect_salary__icontains=query) |
                         Q(candidate_vision__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Candidate(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    position = models.CharField(max_length=150, verbose_name='Position')
    expect_salary = models.CharField(max_length=20, default='Negotiable', blank=True, null=True,
                                     verbose_name='Expect Salary')
    total_of_experience = models.CharField(max_length=20, verbose_name='Total of Experience')
    high_education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name='Education')
    job_type = models.ManyToManyField(JobType, verbose_name='Job')
    skill = models.ManyToManyField(to='Skill', verbose_name='Skill')
    twitter = models.CharField(max_length=120, blank=True, null=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=120, blank=True, null=True, verbose_name='Facebook')
    linkedin = models.CharField(max_length=120, blank=True, null=True, verbose_name='LinkedIn')
    instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')
    curriculum = models.FileField(upload_to='candidates/curriculums/%Y-%m-%d/', blank=True, null=True,
                                  verbose_name='Curriculum', help_text='Allowed size is 100MB')
    candidate_vision = models.TextField(blank=True, null=True, verbose_name='Candidate Vision')

    objects = CandidateManager()

    class Meta:
        verbose_name_plural = 'Candidates'

    def __str__(self):
        return f"{self.account.get_full_name}"

    def get_full_name(self):
        full_name = '%s %s' % (self.account.first_name, self.account.last_name)
        return full_name.strip()
    get_full_name.short_description = 'Full Name'

    def get_absolute_url(self):
        return reverse("candidate-details", kwargs={
            'position': self.position,
            'pk': self.id
        })


class Experience(BaseModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='Candidate')
    company_name = models.CharField(max_length=100, verbose_name='Company Name')
    location = models.CharField(max_length=250, verbose_name='Location')
    logo_url = models.ImageField(upload_to='candidates/experiences/%Y-%m-%d/', blank=True, null=True,
                                 verbose_name='Logo', help_text='Allowed size is 10MB')
    position = models.CharField(max_length=100, verbose_name='Position')
    start_work = models.DateField(default=timezone.now, verbose_name='Start Work')
    end_work = models.DateField(default=timezone.now, verbose_name='End Work')
    responsibilities = models.CharField(max_length=250, verbose_name='Responsibility')
    skill_used = models.CharField(max_length=250, verbose_name='Skill Used')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f"{self.company_name}"


class Responsibility(BaseModel):
    title = models.CharField(max_length=250)
    responsibilities = models.ForeignKey(Experience, on_delete=models.CASCADE, verbose_name='Experience')

    class Meta:
        verbose_name_plural = 'Responsibilities'

    def __str__(self):
        return f"{self.title}"


class EducationLevel(BaseModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='Candidate')
    school_name = models.CharField(max_length=150, verbose_name='School Name')
    major = models.CharField(max_length=150, verbose_name='Major')
    start_year = models.DateField(default=timezone.now, verbose_name='Start Year')
    end_year = models.DateField(default=timezone.now, verbose_name='End Year')
    logo_url = models.ImageField(upload_to='candidates/educations/%Y-%m-%d/', blank=True, null=True,
                                 verbose_name='Logo', help_text='Allowed size is 10MB')
    activities_societies = models.CharField(max_length=250, verbose_name='Activity Society')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name_plural = 'EducationLevels'

    def __str__(self):
        return f"{self.school_name}"


class Portfolio(BaseModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='Candidate')
    title = models.CharField(max_length=150, verbose_name='Title')
    photo_url = models.ImageField(upload_to='candidates/portfolios/%Y-%m-%d/', blank=True, null=True,
                                  verbose_name='Photo', help_text='Allowed size is 100MB')
    status = models.BooleanField(default=True, verbose_name='Status')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return f"{self.title}"


class PortfolioGallery(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name='Portfolio')
    thumbnail = models.ImageField(upload_to='portfolios/galleries/%Y-%m-%d/', blank=True, null=True,
                                  verbose_name='ThumbNail', help_text='Allowed size is 100MB')
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        verbose_name_plural = 'PortfolioGalleries'

    def __str__(self):
        return f"{self.portfolio.title}"

