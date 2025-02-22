from django.contrib import admin

from app.models import Banner, MainInfo, AboutImages, Prospecs, Apartments, AboutPageParagraph, \
    AboutPageBannerParagraph, AboutPageVideoParagraph

# Register your models here.
admin.site.register({Banner, MainInfo, AboutImages, Prospecs,
                     Apartments, AboutPageParagraph,
                     AboutPageBannerParagraph, AboutPageVideoParagraph})