from modeltranslation.translator import register, TranslationOptions
from .models import Services

@register(Services)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)