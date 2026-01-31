from modeltranslation.translator import register, TranslationOptions
from .models import Pedagogical

@register(Pedagogical)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)