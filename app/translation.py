from app.models import MainInfo, Banner, Apartments
from modeltranslation.translator import register, TranslationOptions

@register(MainInfo)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", )


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title_part1', 'title_part2', "description", "button_text")

@register(Apartments)
class ApartmentsTranslationOptions(TranslationOptions):
    fields = ("title", "description", "text",)