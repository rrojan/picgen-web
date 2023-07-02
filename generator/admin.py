from django.contrib import admin
from .models import Photo, GeneratedPhoto


class GenericPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'formatted_created_at')
    readonly_fields = ('formatted_created_at',)

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')

    formatted_created_at.short_description = 'Created At'


admin.site.register(Photo, GenericPhotoAdmin)
admin.site.register(GeneratedPhoto, GenericPhotoAdmin)
