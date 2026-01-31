from modeltranslation.translator import register, TranslationOptions
from .models import Brain

@register(Brain)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)