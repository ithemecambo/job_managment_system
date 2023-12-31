# Generated by Django 4.0.1 on 2022-01-16 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('tags', models.CharField(max_length=150, verbose_name='Tags')),
                ('publish', models.CharField(choices=[('PB', 'Publish'), ('PD', 'Pending')], default='Publish', max_length=3, verbose_name='Publish')),
                ('photo_url', models.ImageField(blank=True, help_text='Allowed size is 100MB', null=True, upload_to='blogs/%Y-%m-%d/', verbose_name='Photo')),
                ('quote', models.TextField(blank=True, null=True, verbose_name='Quote')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'BlogCategories',
            },
        ),
        migrations.CreateModel(
            name='CompanySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('contact_person', models.CharField(max_length=50, verbose_name='Contact Person')),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50, verbose_name='State/Province')),
                ('postal_code', models.CharField(max_length=15, verbose_name='Postal Code')),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('mobile_number', models.CharField(max_length=20, verbose_name='Mobile Number')),
                ('fax', models.CharField(max_length=20)),
                ('website_url', models.CharField(max_length=150, verbose_name='Website URL')),
            ],
            options={
                'verbose_name_plural': 'CompanySettings',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('tel', models.CharField(max_length=20, verbose_name='Tel')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=250, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('device', models.CharField(choices=[('All', 'All'), ('iOS', 'iOS'), ('Android', 'Android')], default='All', max_length=10)),
                ('photo_url', models.ImageField(help_text='Allowed size is 200MB', upload_to='settings/notifications/%Y-%m-%d/', verbose_name='Photo URL')),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(default='', max_length=250)),
                ('photo_url', models.ImageField(help_text='Allowed size is 200MB', upload_to='settings/sliders/%Y-%m-%d/', verbose_name='Photo URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('tel', models.CharField(max_length=20, verbose_name='Tel')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.blog', verbose_name='Blog')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='setting.BlogCategory', verbose_name='Category'),
        ),
    ]
