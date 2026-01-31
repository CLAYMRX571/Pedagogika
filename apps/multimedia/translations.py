from modeltranslation.translator import register, TranslationOptions
from .models import Multimedia

@register(Multimedia)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)