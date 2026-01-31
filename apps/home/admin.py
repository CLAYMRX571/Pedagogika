from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Home

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ('research_name', 'pedagogical_name', 'model_name', 'student_name', 'monitor_name', 'multimedia_name',)