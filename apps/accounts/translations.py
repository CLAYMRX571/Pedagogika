from modeltranslation.translator import register, TranslationOptions
from .models import Accounts

@register(Accounts)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)