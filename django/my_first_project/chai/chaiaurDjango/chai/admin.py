from django.contrib import admin
from . import models


class ChaiReviewInline(admin.TabularInline):
    model = models.ChaiReview
    extra = 2


class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [ChaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("chai_variety",)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")



admin.site.register(models.ChaiVarity, ChaiVarietyAdmin)
admin.site.register(models.Store, StoreAdmin)
admin.site.register(models.Chai_Certificate, ChaiCertificateAdmin)