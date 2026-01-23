from modeltranslation.translator import register, TranslationOptions
from .models import Gallery

@register(Gallery)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)