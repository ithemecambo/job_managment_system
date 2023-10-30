from django.utils.safestring import mark_safe

from job.models import *

PUBLISH_CHOICES = (
    ('PB', 'Publish'),
    ('PD', 'Pending')
)

DEVICE_CHOICES = (
    ('All', 'All'),
    ('iOS', 'iOS'),
    ('Android', 'Android')
)


class BlogCategory(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title')

    class Meta:
        verbose_name_plural = 'BlogCategories'

    def __str__(self):
        return f"{self.title}"


class Blog(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title')
    categories = models.ManyToManyField(to='BlogCategory', verbose_name='Category')
    tags = models.CharField(max_length=150, verbose_name='Tags')
    publish = models.CharField(choices=PUBLISH_CHOICES, max_length=3, default='Publish', verbose_name='Publish')
    photo_url = models.ImageField(upload_to='blogs/%Y-%m-%d/', blank=True, null=True, verbose_name='Photo',
                                  help_text='Allowed size is 100MB')
    quote = models.TextField(blank=True, null=True, verbose_name='Quote')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("blog-details", kwargs={
            'slug': self.slug,
            'pk': self.id
        })

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Blog')
    name = models.CharField(max_length=100, verbose_name='Full Name')
    tel = models.CharField(max_length=20, verbose_name='Tel')
    email = models.CharField(max_length=100, verbose_name='Email')
    website = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.name}"


class Contact(BaseModel):
    full_name = models.CharField(max_length=150, verbose_name='Full Name')
    tel = models.CharField(max_length=20, verbose_name='Tel')
    email = models.EmailField(max_length=50, verbose_name='Email')
    comment = models.TextField(verbose_name='Comment')

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.full_name}"


class FAQ(BaseModel):
    question = models.CharField(max_length=250, verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')

    class Meta:
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return f"{self.question}"


class CompanySetting(BaseModel):
    company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Company Name')
    contact_person = models.CharField(max_length=50, blank=False, null=False, verbose_name='Contact Person')
    address = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state_province = models.CharField(max_length=50, blank=False, null=False, verbose_name='State/Province')
    postal_code = models.CharField(max_length=15, blank=False, null=False, verbose_name='Postal Code')
    email = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False, verbose_name='Phone Number')
    mobile_number = models.CharField(max_length=20, blank=False, null=False, verbose_name='Mobile Number')
    fax = models.CharField(max_length=20, blank=False, null=False)
    website_url = models.CharField(max_length=150, blank=False, null=False, verbose_name='Website URL')

    class Meta:
        verbose_name_plural = 'CompanySettings'

    def __str__(self):
        return f'{self.company_name}'


class Slider(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    caption = models.CharField(max_length=250, default='', blank=False, null=False)
    photo_url = models.ImageField(upload_to='settings/sliders/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 200MB', blank=False, null=False)

    def get_caption(self):
        return self.caption[:30]

    def __str__(self):
        return self.title

    def banner_slider(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_slider.short_description = 'Banner'


class Notification(BaseModel):
    title = models.CharField(max_length=150)
    device = models.CharField(choices=DEVICE_CHOICES, max_length=10, default='All')
    photo_url = models.ImageField(upload_to='settings/notifications/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 200MB', blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.title

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

