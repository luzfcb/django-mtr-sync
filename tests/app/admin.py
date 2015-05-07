import django

from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

if django.get_version() >= '1.7':
    from mtr.sync.admin import SyncAdminMixin, SyncStackedInlineMixin
else:
    from mtr_sync.admin import SyncAdminMixin, SyncStackedInlineMixin

from .models import Person, Office, Tag


class PersonAdmin(SyncAdminMixin, TabbedTranslationAdmin):

    list_display = ('name', 'surname', 'security_level', 'gender')
    list_filter = ('security_level', 'tags', 'office', 'name', 'gender')

    actions = ['copy_100']

    def copy_100(self, request, queryset):
        for item in queryset.all():
            item.populate()
    copy_100.short_description = 'Copy 100 objects with random data'


class PersonStackedInline(SyncStackedInlineMixin, admin.StackedInline):
    model = Person
    extra = 0


class OfficeAdmin(admin.ModelAdmin):
    inlines = (PersonStackedInline,)
    list_display = ('office', 'address')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Tag, TagAdmin)
