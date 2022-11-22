from django.contrib import admin
from .models import *


class SkuAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SkuDirtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku')
    list_filter = ('name', 'sku')
    list_editable = ('sku', )
    autocomplete_fields = ['sku']


class SOFileAdmin(admin.ModelAdmin):
    change_list_template = 'metabase_wrapper/sofile_change_list.html'
    list_display = ('filename', 'distributor', 'year', 'month', 'is_month_inside')
    list_editable = ('distributor', 'year', 'month', 'is_month_inside')
    autocomplete_fields = ['distributor']

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_upload_files_btn'] = SOFile.objects.count() > 0
        return super(SOFileAdmin, self).changelist_view(request, extra_context)


class DistributorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'operation_type', 'group')
    list_editable = ('operation_type', )


admin.site.site_header = "Aspect | Страница администрирования"  
admin.site.site_title = "Страница администрирования"
admin.site.index_title = "Aspect | Страница администрирования"

admin.site.register(Sku, SkuAdmin)
admin.site.register(SkuDirty, SkuDirtyAdmin)
admin.site.register(SOFile, SOFileAdmin)
admin.site.register(DistributorGroup)
admin.site.register(Distributor, DistributorAdmin)
