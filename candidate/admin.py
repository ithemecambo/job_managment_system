from django.contrib import admin
from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'title',
        'status'
    ]
    ordering = [
        'title'
    ]
    list_per_page = 10


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class EducationLevelInline(admin.StackedInline):
    model = EducationLevel
    extra = 0


class PortfolioGalleryInline(admin.StackedInline):
    model = PortfolioGallery
    extra = 0


class PortfolioInline(admin.StackedInline):
    model = Portfolio
    inlines = [PortfolioGalleryInline]
    extra = 0


class CandidateAdmin(admin.ModelAdmin):

    list_display = [
        'get_full_name',
        'position',
        'high_education',
        'total_of_experience',
        'expect_salary',
        'status',
    ]
    list_display_links = [
        'get_full_name',
        'position',
        'high_education',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'account__first_name',
        'account__last_name',
        'position',
        'high_education__name',
        'total_of_experience',
        'expect_salary',
        'job_type__title',
        'skill__title',
        'status',
    ]
    list_per_page = 10
    save_on_top = True
    model = Candidate
    inlines = [ExperienceInline, EducationLevelInline, PortfolioInline]


class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'name',
        'status',
    ]
    list_per_page = 25


class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    list_filter = [
        'created_date',
        'status',
    ]
    search_fields = [
        'name',
    ]
    ordering = [
        'name',
    ]
    list_per_page = 10


admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Education, EducationAdmin)

