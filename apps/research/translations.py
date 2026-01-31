from modeltranslation.translator import register, TranslationOptions
from .models import Research

@register(Research)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)