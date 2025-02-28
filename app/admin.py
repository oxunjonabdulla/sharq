# from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
#
# from app.models import Banner, MainInfo, AboutImages, Prospecs, Apartments, AboutPageParagraph, \
#     AboutPageBannerParagraph, AboutPageVideoParagraph
#
# @admin.register(MainInfo)
# class MainInfoAdmin(TranslationAdmin):
#     pass
#
#     class Media:
#         js = (
#             'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js',
#             'js/translation.js',)
#
# # Register your models here.
# admin.site.register({Banner, AboutImages, Prospecs,
#                      Apartments, AboutPageParagraph,
#                      AboutPageBannerParagraph, AboutPageVideoParagraph})




from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import MainInfo, Banner, Apartments


class CustomTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(MainInfo)
class MainInfoAdmin(CustomTranslationAdmin):
    list_display = ('title', )


@admin.register(Banner)
class BannerAdmin(CustomTranslationAdmin):
    list_display = ('title_part1', 'title_part2', "description", "button_text")


@admin.register(Apartments)
class ApartmentAdmin(CustomTranslationAdmin):
    list_display = ("title", "description", "text")



# admin.site.register([
#     RoomImages,
#     RoomAmenity,
#     Gallery,
#     MainSocial,
#     Contact,
#     Comment,
#     Booking,
#     QRCodeURL
# ])
















