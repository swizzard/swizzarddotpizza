from django.contrib import admin
from models import Hashtag, Cluster, Votes


class GenAdmin(admin.ModelAdmin):
    ordering = ('id',)

admin.site.register(Cluster, GenAdmin)
admin.site.register(Hashtag, GenAdmin)
admin.site.register(Votes, GenAdmin)
