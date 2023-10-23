from django.contrib import admin
from .models import Post, Relation, Person
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'created',)
    search_fields = ('slug',)
    prepopulated_fields = ({'slug': ('body',)})
    raw_id_fields = ('user',)


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False


class ExtendedPersonAdmin(UserAdmin):
    inlines = (PersonInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedPersonAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Relation)
