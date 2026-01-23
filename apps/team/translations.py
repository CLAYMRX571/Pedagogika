from modeltranslation.translator import register, TranslationOptions
from .models import About

@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)