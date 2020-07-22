from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as core_models


class TfeUserAdmin(UserAdmin):
    model = core_models.TfeUser
    list_display = (
        'username',
        'uuid',
        'email',
        'id',
    )

    readonly_fields = (
        'username',
        'uuid',
        'email',
        'id',
    )


class UserProfileAdmin(admin.ModelAdmin):
    model = core_models.UserProfile
    list_display = ('uuid', 'username')
    readonly_fields = ('uuid',)

    def username(self, obj): return obj.user.username
    username.short_description = 'Username'


admin.site.register(core_models.TfeUser, TfeUserAdmin)
admin.site.register(core_models.UserProfile, UserProfileAdmin)
