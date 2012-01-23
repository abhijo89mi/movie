from django.contrib import admin
from tracking.models import BannedIP, UntrackedUserAgent,Visitor
class VisitorAdmin(admin.ModelAdmin):
	list_display = ('ip_address','user','referrer','url','page_views')
admin.site.register(BannedIP)
admin.site.register(UntrackedUserAgent)
admin.site.register(Visitor,VisitorAdmin)
