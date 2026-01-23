from modeltranslation.translator import register, TranslationOptions
from .models import Team

@register(Team)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)