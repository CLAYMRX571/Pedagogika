from modeltranslation.translator import register, TranslationOptions
from .models import Health

@register(Health)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)