# Generated by Django 4.0.1 on 2022-01-16 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('font_awesome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Font Awesome')),
                ('logo_url', models.ImageField(blank=True, help_text='Allowed size is 10MB', null=True, upload_to='categories/', verbose_name='Icon')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_kh', models.CharField(max_length=100, verbose_name='Khmer Name')),
                ('logo_url', models.ImageField(blank=True, help_text='Allowed size is 10MB', null=True, upload_to='cities/', verbose_name='Logo')),
                ('code', models.CharField(max_length=5, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Company Name')),
                ('employee_num', models.CharField(choices=[('N1', '<10'), ('N2', '10~50'), ('N3', '50~100'), ('N4', '100~200'), ('N5', '>200'), ('N6', '>500'), ('N7', '>1000')], default='~', max_length=10, verbose_name='Employee Number')),
                ('founded', models.CharField(max_length=6, verbose_name='Founded')),
                ('revenue', models.CharField(max_length=50, verbose_name='Revenue')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('website', models.CharField(blank=True, max_length=50, null=True, verbose_name='Website')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('latitude', models.CharField(max_length=20, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=20, verbose_name='Longitude')),
                ('banner_url', models.ImageField(blank=True, help_text='Allowed size is 100MB', null=True, upload_to='companies/banners/%Y-%m-%d/', verbose_name='Banner')),
                ('logo_url', models.ImageField(blank=True, help_text='Allowed size is 10MB', null=True, upload_to='companies/logos/%Y-%m-%d/', verbose_name='Logo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('company_industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category', verbose_name='Company Industry')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Company Name')),
            ],
            options={
                'verbose_name_plural': 'CompanyTypes',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'JobTypes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('font_awesome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Font Awesome')),
                ('logo_url', models.ImageField(blank=True, help_text='Allowed size is 10MB', null=True, upload_to='subcategories/', verbose_name='Icon')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(choices=[('EL', 'Entry Level'), ('MD', 'Middle'), ('SE', 'Senior'), ('TP', 'Top'), ('FG', 'Fresh Graduate')], default='Entry Level', max_length=3, verbose_name='Level')),
                ('year_of_experience', models.IntegerField(blank=True, default=1, null=True, verbose_name='Year of Experience')),
                ('hiring', models.IntegerField(blank=True, default=1, null=True, verbose_name='Hiring')),
                ('salary', models.CharField(blank=True, default='Negotiable', max_length=20, null=True, verbose_name='Salary')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('MF', 'Male/Female')], default='Male/Female', max_length=3, verbose_name='Sex')),
                ('age', models.CharField(blank=True, default='~', max_length=10, null=True, verbose_name='Age')),
                ('marital_status', models.CharField(choices=[('SL', 'Single'), ('MR', 'Married'), ('DD', 'Divorced'), ('ST', 'Separated'), ('WN', 'Window'), ('OT', 'Others')], default='Single', max_length=3, verbose_name='Marital Status')),
                ('publish_date', models.DateField(default=django.utils.timezone.now, verbose_name='Publish Date')),
                ('closing_date', models.DateField(default=django.utils.timezone.now, verbose_name='Closing Date')),
                ('twitter', models.CharField(blank=True, max_length=120, null=True, verbose_name='Twitter')),
                ('facebook', models.CharField(blank=True, max_length=120, null=True, verbose_name='Facebook')),
                ('linkedin', models.CharField(blank=True, max_length=120, null=True, verbose_name='LinkedIn')),
                ('instagram', models.CharField(blank=True, max_length=120, null=True, verbose_name='Instagram')),
                ('status', models.CharField(choices=[('AP', 'Approved'), ('PD', 'Pending'), ('EP', 'Expire'), ('RJ', 'Rejected')], default='Approved', max_length=3, verbose_name='Status')),
                ('premium', models.CharField(choices=[('UT', 'Urgent'), ('FT', 'Featured'), ('HL', 'Highlight')], default='Urgent', max_length=3, verbose_name='Premium')),
                ('job_description', models.TextField(blank=True, null=True, verbose_name='Job Description')),
                ('job_requirement', models.TextField(blank=True, null=True, verbose_name='Job Requirement')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company', verbose_name='Company')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.education', verbose_name='Education')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.subcategory', verbose_name='Function')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobtype', verbose_name='Term')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='CompanyRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('rating_num', models.IntegerField(default=1, verbose_name='Rating Num')),
                ('text', models.TextField(verbose_name='Text')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company', verbose_name='Company')),
            ],
            options={
                'verbose_name_plural': 'CompanyRatings',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.companytype', verbose_name='Company Type'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.city', verbose_name='City'),
        ),
    ]
