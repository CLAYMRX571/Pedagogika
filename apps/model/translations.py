from modeltranslation.translator import register, TranslationOptions
from .models import Model

@register(Model)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)