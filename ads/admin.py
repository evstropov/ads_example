from django.contrib import admin

from .models import Ad, AdUserHit


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time')
    list_filter = ('author', 'create_time')
    readonly_fields = ('hits',)
    search_fields = ['title']


class AdUserHitAdmin(admin.ModelAdmin):
    list_display = ('ad', 'user', 'time')
    list_filter = ('user', 'time')
    readonly_fields = ('ad', 'user', 'time')

    def has_add_permission(self, request):
        return False

admin.site.register(Ad, AdAdmin)
admin.site.register(AdUserHit, AdUserHitAdmin)
