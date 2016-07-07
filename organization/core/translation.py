from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.pages.models import Page, RichText
from mezzanine.pages.translation import TranslatedRichText

from organization.core.models import BasicPage


@register(BasicPage)
class BasicPageTranslationOptions(TranslationOptions):

    fields = ('sub_title',)