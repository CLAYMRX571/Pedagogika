from modeltranslation.translator import register, TranslationOptions
from .models import Handshake

@register(Handshake)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)