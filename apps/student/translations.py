from modeltranslation.translator import register, TranslationOptions
from .models import Student

@register(Student)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)