from movie.main.models import *
from django.contrib import admin
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
	



admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

admin.site.register(movieurl, movieurlAdmin)
