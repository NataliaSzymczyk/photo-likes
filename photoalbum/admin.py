from django.contrib import admin
from photoalbum.models import (Comment, Photo, Vote)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("like", "voting_photo", "voting_user_list")
    def voting_user_list(self, obj):
        return ", ".join([str(u) for u in obj.voting_user.all()])


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("votes", "path", "creation_date", "photo")


admin.site.register(Comment)

