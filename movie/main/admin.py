from movie.main.models import *
from django.contrib import admin
from django.contrib.admin.models import *
from django.utils.html import escape
from django.core.urlresolvers import reverse
from imdb import IMDb

def getmove (movieurlAdmin, request, queryset):
	access = IMDb()
	selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
	for selected_id in selected:
		movie = access.get_movie(queryset.get(id=selected_id).imdbid.replace('tt',''))
		movieurlAdmin.message_user(request,movie['title'] )
	getmove.short_description = "Get Movie"
	
class movieurlAdmin(admin.ModelAdmin):
	
	def Genre(self,obj):
		return Genre.objects.get(name=obj.filter_based_on)
		
	def Movie_url(self,obj):
		return "<a href=%s >%s</a>" %(obj.url,obj.url)
	Movie_url.allow_tags = True
	
	list_display = ('id','imdbid','movie_name','runcount','Movie_url','sucess_factor','run_date','last_rundate','Genre')
	search_fields = ['imdbid','url',]
	date_hierarchy = 'run_date'
	ordering = ('id',)
	actions = [getmove]
	
class GenreAdmin(admin.ModelAdmin):
	def refresh_btn(self, obj):
		return "<button onclick=foo('%s')>refresh</button>" % (obj.name)
	refresh_btn.short_description = 'Refresh'
	refresh_btn.allow_tags = True
	list_display = ('name','refresh_btn','total_movie')
	search_fields = ['name',]
	ordering = ('name',)

  
class MovieAdmin(admin.ModelAdmin):
	filter_horizontal = ('akas_id','plot','certificates','countries','genres','languages','sound_mix','animation_department','art_department','art_direction','assistant_director','camera_and_electrical_department','cast','casting_department','casting_director','cinematographer','color_info','costume_department','costume_designer','director','distributors','editor','languages','make_up','miscellaneous_companies','miscellaneous_crew','music_department','original_music','producer','production_companies','production_design','production_manager',
	'runtimes','set_decoration','sound_crew','special_effects_companies','special_effects_department','stunt_performer','transportation_department','visual_effects','writer')
	
class Animation_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Art_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Art_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Art_directionAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Assistant_directorAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Camera_and_electrical_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class CastAdmin(admin.ModelAdmin):
	filter_horizontal = ('name','charactor')
class Casting_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Casting_directorAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class CinematographerAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Color_infoAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Costume_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Costume_designerAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class DirectorAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class DistributorsAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class EditorAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class LanguagesAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Make_upAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Miscellaneous_companiesAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Miscellaneous_crewAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Music_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Original_musicAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class ProducerAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Production_companiesAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Production_designAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Production_managerAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class RuntimesAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Set_decorationAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Special_effects_companiesAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Special_effects_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Stunt_performerAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Sound_crewAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Transportation_departmentAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class Visual_effectsAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class WriterAdmin(admin.ModelAdmin):
	filter_horizontal = ('name',)
class PersonAdmin(admin.ModelAdmin):
	filter_horizontal = ('photo',)


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




admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Animation_department, Animation_departmentAdmin)
admin.site.register(Art_department, Art_departmentAdmin)
admin.site.register(Art_direction, Art_directionAdmin)
admin.site.register(Assistant_director, Assistant_directorAdmin)
admin.site.register(Camera_and_electrical_department, Camera_and_electrical_departmentAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Casting_department, Casting_departmentAdmin)
admin.site.register(Casting_director, Casting_directorAdmin)
admin.site.register(Cinematographer, CinematographerAdmin)
#admin.site.register(Color_info, Color_infoAdmin)
admin.site.register(Costume_department, Costume_departmentAdmin)
admin.site.register(Costume_designer, Costume_designerAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Distributors, DistributorsAdmin)
#admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Make_up, Make_upAdmin)
admin.site.register(Miscellaneous_companies, Miscellaneous_companiesAdmin)
admin.site.register(Miscellaneous_crew, Miscellaneous_crewAdmin)
admin.site.register(Music_department, Music_departmentAdmin)
admin.site.register(Original_music, Original_musicAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Production_companies, Production_companiesAdmin)
admin.site.register(Production_design, Production_designAdmin)
admin.site.register(Production_manager, Production_managerAdmin)
admin.site.register(Runtimes, RuntimesAdmin)
admin.site.register(Set_decoration, Set_decorationAdmin)
admin.site.register(Sound_crew, Sound_crewAdmin)
admin.site.register(Special_effects_companies, Special_effects_companiesAdmin)
admin.site.register(Special_effects_department, Special_effects_departmentAdmin)
admin.site.register(Stunt_performer,Stunt_performerAdmin)
admin.site.register(Transportation_department,Transportation_departmentAdmin)
admin.site.register(Visual_effects, Visual_effectsAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(movieurl, movieurlAdmin)

# Admin model registration 
admin.site.register(LogEntry, LogEntryAdmin)
