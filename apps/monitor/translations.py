from modeltranslation.translator import register, TranslationOptions
from .models import Monitor

@register(Monitor)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)