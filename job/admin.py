from django.contrib import admin
from candidate.models import *
from .forms import *


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryCreateForm
    list_display = [
        'title',
        'status',
    ]
    list_filter = [
        'created_date',
        'status',
    ]
    search_fields = [
        'title',
        'status',
        'created_date',
    ]
    ordering = [
        'title',
    ]
    list_per_page = 10


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'get_category',
        'title',
        'status',
    ]
    list_display_links = [
        'get_category',
        'title',
    ]
    list_filter = [
        'created_date',
        'status',
    ]
    search_fields = [
        'title',
        'category__title',
    ]
    ordering = [
        'title',
    ]
    list_per_page = 10


class JobTypeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
    ]
    list_filter = [
        'created_date',
        'status',
    ]


class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    list_filter = [
        'created_date',
        'status',
    ]
    ordering = [
        'name',
    ]


class CompanyAdmin(admin.ModelAdmin):

    list_display = [
        'profile',
        'name',
        'company_industry',
        'employee_num',
        'founded',
        'revenue',
        'status',
    ]
    list_display_links = [
        'profile',
        'name',
        'company_industry',
    ]
    list_filter = [
        'created_date',
        'employee_num',
        'status',
    ]
    search_fields = [
        'name',
        'company_industry__title',
        'employee_num',
        'company_type__name',
        'founded',
        'revenue',
        'phone',
        'fax',
        'website',
        'location__name',
        'location__name_kh',
        'address',
        'description',
    ]
    list_per_page = 10


class LanguageLevelInline(admin.TabularInline):
    model = LanguageLevel
    extra = 0


class JobAdmin(admin.ModelAdmin):

    list_display = [
        'profile',
        'get_company',
        'function',
        'level',
        'term',
        'salary',
        'year_of_experience',
        'hiring',
    ]
    list_display_links = [
        'profile',
        'get_company',
        'function',
        'level',
    ]
    list_filter = [
        'closing_date',
        'level',
        'term',
        'status',
    ]
    search_fields = [
        'company__name',
        'level',
        'term__title',
        'year_of_experience',
        'function__title',
        'education__name',
        'hiring',
        'salary',
    ]
    list_per_page = 10
    save_on_top = True
    inlines = [LanguageLevelInline]


class CompanyRatingAdmin(admin.ModelAdmin):
    list_display = [
        'account',
        'company',
        'rating',
        'status',
    ]
    list_filter = [
        'created_date',
        'status',
    ]
    search_fields = [
        'text',
        'rating_num',
    ]
    list_per_page = 10


admin.site.register(City)
admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CompanyRating, CompanyRatingAdmin)
