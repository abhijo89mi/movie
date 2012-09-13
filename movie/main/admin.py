from movie.main.models import *
from django.contrib import admin

from django.core.urlresolvers import reverse
from django.contrib.admin.models import *
from django.utils.html import escape

	
class movieurlAdmin(admin.ModelAdmin):
	
		
	def Movie_url(self,obj):
		return "<a href=%s >%s</a>" %(obj.url,obj.url)
	Movie_url.allow_tags = True
	
	list_display = ('id','imdbid','movie_name','runcount','Movie_url','sucess_factor','run_date','last_rundate','filter_based_on')
	search_fields = ['imdbid','url',]
	date_hierarchy = 'run_date'
	ordering = ('id',)

class GenreAdmin(admin.ModelAdmin):
	def refresh_btn(self, obj):
		return "<button onclick=foo('%s')>refresh</button>" % (obj.name)
	refresh_btn.short_description = 'Refresh'
	refresh_btn.allow_tags = True
	list_display = ('display_name','name','refresh_btn','total_movie')
	search_fields = ['name',]
	ordering = ('name',)
class CharactorAdmin(admin.ModelAdmin):
	list_display = ('name','roleID',)
		
class CastAdmin(admin.ModelAdmin):
	filter_horizontal = ('charactor',)
	
class MovieAdmin(admin.ModelAdmin):

	list_display = ('id','title','votes','year','imdbid','rating',)
	search_fields = ['imdbid','title','year']
	readonly_fields = ('akas_id','plot','certificates','countries','genres','languages','sound_mix','animation_department','art_department','art_direction','assistant_director','camera_and_electrical_department','cast','casting_department','casting_director','cinematographer','color_info','costume_department','costume_designer','director','distributors','editor','languages','make_up','miscellaneous_companies','miscellaneous_crew','music_department','original_music','producer','production_companies','production_design','production_manager',
	'runtimes','set_decoration','sound_crew','special_effects_companies','special_effects_department','stunt_performer','transportation_department','visual_effects','writer')
	
	ordering = ('id',)
class Movie_Fetch_StatisticsAdmin(admin.ModelAdmin):
	list_display = ('id','start_date','end_date','total_count','total_run_count','start_movie_imdbid','end_movie_imdbid')
	date_hierarchy = 'start_date'
        ordering = ('-id',)
        search_fields = ('end_movie_imdbid','start_movie_imdbid')
	

class PersonAdmin(admin.ModelAdmin):
	list_display = ('id','name','personID',)
	search_fields = ('name','personID',)

		
class LanguagesAdmin(admin.ModelAdmin):
	list_display = ('name','code',)
	
class CountriesAdmin(admin.ModelAdmin):
	list_display = ('name','code',)
	
class PhotoAdmin(admin.ModelAdmin):
	def person(self,obj):
		return obj.Photo_M2M_Person.all()[0].name
	
	def personID(self,obj):
		return obj.Photo_M2M_Person.all()[0].personID
	list_display = ('id','url','person','personID')

class PhotoAdmin(admin.ModelAdmin):
	def person(self,obj):
		return obj.Photo_M2M_Person.all()[0].name
	
	def personID(self,obj):
		return obj.Photo_M2M_Person.all()[0].personID
	def image(self,obj):
		return "<img src=\"/media/person/"+obj.url+"\">"
	image.allow_tags = True

	list_display = ('image','url','person','personID')
	

class Person_StatisticsAdmin(admin.ModelAdmin):
	def person_name(self,obj):
		return obj.person.name
	
	list_display = ('person_name','date','name','note','default_info','biodata','date_of_birth','photo')
	date_hierarchy = 'date'
	ordering = ('-date',)
	search_fields = ('person_name',)


# Admin log file
class LogEntryAdmin(admin.ModelAdmin):

	date_hierarchy = 'action_time'

	readonly_fields = LogEntry._meta.get_all_field_names()

	list_filter = [
		'user',
		'content_type',
		'action_flag'
	]

	search_fields = [
		'object_repr',

		'change_message'
	]


	list_display = [
		'action_time',
		'user',
		'content_type',
		'object_link',
		'action_flag',
		'change_message',
	]

	def has_add_permission(self, request):
		return False

	def has_change_permission(self, request, obj=None):
		return request.user.is_superuser and request.method != 'POST'

	def has_delete_permission(self, request, obj=None):
		return False

	def object_link(self, obj):
		if obj.action_flag == DELETION:
			link = escape(obj.object_repr)
		else:
			ct = obj.content_type
			link = u'<a href="%s">%s</a>' % (
				reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
				escape(obj.object_repr),
			)
		return link
	object_link.allow_tags = True
	object_link.admin_order_field = 'object_repr'
	object_link.short_description = u'object'

class VideoAdmin(admin.ModelAdmin):
	list_display = ('movie_id','imdbid','video_url','movie_url')

class Person_StatisticsAdmin(admin.ModelAdmin):
	def person_name(self,obj):
		return obj.person.name
	
	list_display = ('person_name','date','name','note','default_info','biodata','date_of_birth','photo')
	
class UpdatehistoryAdmin(admin.ModelAdmin):
	list_display = ('date','boxoffice','upcoming','intheaters','opening','user','movie','akas','plot','certificates','countries','genres','sound_mix','animation_department','art_department','art_direction','assistant_director','camera_and_electrical_department','cast','casting_department','casting_director','cinematographer','color_info','costume_department','costume_designer','director','distributors','editor','languages','make_up','miscellaneous_companies','miscellaneous_crew','music_department','original_music','producer','production_companies','production_design','production_manager','runtimes','set_decoration','sound_crew','special_effects_companies','special_effects_department','stunt_performer','transportation_department','visual_effects','writer','Video','release_date')

class UrllogAdmin(admin.ModelAdmin):
	list_display =('start_url_id','end_url_id','end_date')

# Admin model registration 
admin.site.register(LogEntry, LogEntryAdmin)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Movie_Fetch_Statistics, Movie_Fetch_StatisticsAdmin)
admin.site.register(movieurl, movieurlAdmin)
admin.site.register(Charactor, CharactorAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Person_Statistics, Person_StatisticsAdmin)
admin.site.register(Updatehistory, UpdatehistoryAdmin)
admin.site.register(Urllog, UrllogAdmin)
Urllog
