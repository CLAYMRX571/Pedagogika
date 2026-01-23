from modeltranslation.translator import register, TranslationOptions
from .models import Contact

@register(Contact)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)