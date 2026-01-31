from modeltranslation.translator import register, TranslationOptions
from .models import Home

@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('research_name', 'pedagogical_name', 'model_name', 'student_name', 'monitor_name', 'multimedia_name',)