from modeltranslation.translator import register, TranslationOptions
from .models import Home

@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)