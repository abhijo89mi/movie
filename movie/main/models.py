from django.contrib.auth.models import User, Group
from django.db import models
from datetime import datetime

class Movie(models.Model):
	title= models.CharField(max_length=100,)
	votes=models.IntegerField(null=True)
	year=models.IntegerField(null=True)
	aspect_ration=models.CharField(max_length=50,)
	mpaa=models.CharField(max_length=200,)
	rating =models.CharField(max_length=20,)
	imdbid=models.CharField(max_length=50,)
	top_250_rank=models.IntegerField(null=True)
	cover_url=models.CharField(max_length=500,)
	plot_outline=models.TextField(blank=True, null=True)
	summary= models.TextField(blank=True, null=True)
	
	#M2M Tables
	akas_id  		= models.ManyToManyField('Akas', verbose_name=u'Akas ID',related_name="Akas_M2M_Movie")
	plot=models.ManyToManyField('Plot', verbose_name=u'Plot ID',related_name="Plot_M2M_Movie")
	certificates= models.ManyToManyField('Certificates', verbose_name=u'Certificate ID',related_name="Certificates_M2M_Movie",null=True,blank=True)
	countries=models.ManyToManyField('Countries', verbose_name=u'Country ID',related_name="Country_M2M_Movie",blank=True)
	genres=models.ManyToManyField('Genre', verbose_name=u'Genres ID',related_name="Genres_M2M_Movie",blank=True)
	sound_mix=models.ManyToManyField('Sound_mix', verbose_name=u'Sound_mix ID',related_name="Sound_mix_M2M_Movie",blank=True)
	animation_department=models.ManyToManyField('Animation_department', verbose_name=u'Animation Department',related_name="animation_department_M2M_Movie",blank=True)
	art_department=models.ManyToManyField('Art_department', verbose_name=u'Art Department',related_name="Art_department_M2M_Movie",blank=True)
	art_direction=models.ManyToManyField('Art_direction', verbose_name=u'Art_directionD',related_name="Art_direction_M2M_Movie",blank=True)
	assistant_director=models.ManyToManyField('Assistant_director', verbose_name=u'Assistant_director ID',related_name="Assistant_director_M2M_Movie",blank=True)
	camera_and_electrical_department=models.ManyToManyField('Camera_and_electrical_department', verbose_name=u'camera_and_electrical_department ID',related_name="camera_and_electrical_department_M2M_Movie",blank=True)
	cast=models.ManyToManyField('Cast', verbose_name=u'Cast',related_name="Cast_M2M_Movie",blank=True)
	casting_department=models.ManyToManyField('Casting_department', verbose_name=u'Casting_department',related_name="Casting_department_M2M_Movie",blank=True)
	casting_director=models.ManyToManyField('Casting_director', verbose_name=u'casting_director ID',related_name="casting_director_M2M_Movie",blank=True)
	cinematographer=models.ManyToManyField('Cinematographer', verbose_name=u'Cinematographer',related_name="Cinematographer_M2M_Movie",blank=True)
	color_info=models.ManyToManyField('Color_info', verbose_name=u'Color_info ID',related_name="Color_info_M2M_Movie",blank=True)
	costume_department=models.ManyToManyField('Costume_department', verbose_name=u'costume_department ID',related_name="costume_department_M2M_Movie",blank=True)
	costume_designer=models.ManyToManyField('Costume_designer', verbose_name=u'costume_designer ID',related_name="costume_designer_M2M_Movie")
	director=models.ManyToManyField('Director', verbose_name=u'Director ID',related_name="Director_M2M_Movie",blank=True)
	distributors=models.ManyToManyField('Distributors', verbose_name=u'Distributors ID',related_name="Distributors_M2M_Movie",blank=True)
	editor=models.ManyToManyField('Editor', verbose_name=u'Editor ID',related_name="Editor_M2M_Movie",blank=True)
	languages=models.ManyToManyField('Languages', verbose_name=u'Languages ID',related_name="Languages_M2M_Movie",blank=True)
	make_up=models.ManyToManyField('Make_up', verbose_name=u'Make_up ID',related_name="Make_up_M2M_Movie",blank=True)
	miscellaneous_companies=models.ManyToManyField('Miscellaneous_companies', verbose_name=u'Miscellaneous_companies ID',related_name="miscellaneous_companies_M2M_Movie",blank=True)
	miscellaneous_crew=models.ManyToManyField('Miscellaneous_crew', verbose_name=u'Miscellaneous_crew ID',related_name="Miscellaneous_crew_M2M_Movie",blank=True)
	music_department=models.ManyToManyField('Music_department', verbose_name=u'Music_department ID',related_name="Music_department_M2M_Movie",blank=True)
	original_music=models.ManyToManyField('Original_music', verbose_name=u'Original_music ID',related_name="Original_music_M2M_Movie",blank=True)
	producer=models.ManyToManyField('Producer', verbose_name=u'Producer ID',related_name="Producer_M2M_Movie",blank=True)
	production_companies=models.ManyToManyField('Production_companies', verbose_name=u'Production_companies ID',related_name="Production_companies_M2M_Movie",blank=True)
	production_design=models.ManyToManyField('Production_design', verbose_name=u'Production_design ID',related_name="Production_design_M2M_Movie",blank=True)
	production_manager=models.ManyToManyField('Production_manager', verbose_name=u'Production_manager ID',related_name="Production_manager_M2M_Movie",blank=True)
	runtimes=models.ManyToManyField('Runtimes', verbose_name=u'Runtimes ID',related_name="Sound_mix_M2M_Movie",blank=True)
	set_decoration=models.ManyToManyField('Set_decoration', verbose_name=u'Set_decoration ID',related_name="Set_decoration_M2M_Movie",blank=True)
	sound_crew=models.ManyToManyField('Sound_crew', verbose_name=u'Sound_crew ID',related_name="Sound_crew_M2M_Movie",blank=True)
	special_effects_companies=models.ManyToManyField('Special_effects_companies', verbose_name=u'Special_effects_companies ID',related_name="Special_effects_companies_M2M_Movie",blank=True)
	special_effects_department=models.ManyToManyField('Special_effects_department', verbose_name=u'Special_effects_department ID',related_name="Special_effects_department_M2M_Movie",blank=True)
	stunt_performer=models.ManyToManyField('Stunt_performer', verbose_name=u'Stunt_performer ID',related_name="Stunt_performer_M2M_Movie",blank=True)
	transportation_department=models.ManyToManyField('Transportation_department', verbose_name=u'Transportation_department ID',related_name="Transportation_department_M2M_Movie",blank=True)
	visual_effects=models.ManyToManyField('Visual_effects', verbose_name=u'Visual_effects ID',related_name="Visual_effects_M2M_Movie",blank=True)
	writer=models.ManyToManyField('Writer', verbose_name=u'Writer ID',related_name="Writer_M2M_Movie",blank=True)
	Video=models.ManyToManyField('Video', verbose_name=u'Video url',related_name="Video_M2M_Movie",blank=True)
	release_date = models.ManyToManyField('Release_date', verbose_name=u'Release Date',related_name="Release_date_M2M_Movie",blank=True)
	def __unicode__(self):
		return u'%s' % (self.title)
	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movies'
		db_table = 'movie'

class Akas(models.Model):
	name=models.CharField(max_length=500,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Other Movie Title'
		verbose_name_plural = 'Other Movie Titles'
		db_table = 'Akas'
class Release_date(models.Model):
	date=models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.date)
	class Meta:
		verbose_name = 'Release Date'
		verbose_name_plural = 'Release Dates'
		db_table = 'Release_date'

class Certificates(models.Model):
	name=models.CharField(max_length=200,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Certificate'
		verbose_name_plural = 'Certificates'
		db_table = 'Certificates'

class Countries(models.Model):
	name=models.CharField(max_length=100,)
	code=models.CharField(max_length=10,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		db_table = 'Countries'

class Languages(models.Model):
	name=models.CharField(max_length=100,)
	code=models.CharField(max_length=10,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'
		db_table = 'Languages'

class Sound_mix(models.Model):
	name= models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Sound Mix'
		verbose_name_plural = 'Sound Mix'
		db_table = 'Sound_mix'

class Animation_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Animation_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Animation Department'
		verbose_name_plural = 'Animation Department'
		db_table = 'Animation_department'

class Art_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Art_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Art Department'
		verbose_name_plural = 'Art Department'
		db_table = 'Art_department'

class Art_direction(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Art_direction")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Art Direction'
		verbose_name_plural = 'Art Direction'
		db_table = 'Art_direction'

class Assistant_director(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Assistant_director")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Assistant Director'
		verbose_name_plural = 'Assistant Directors'
		db_table = 'Assistant_director'

class Camera_and_electrical_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Camera_and_electrical_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Camera And Electrical Department'
		verbose_name_plural = 'Camera And Electrical Departments'
		db_table = 'Camera_and_electrical_department'

class Cast(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Cast")
	charactor=models.ManyToManyField('Charactor', verbose_name=u'Charactor ID',related_name="Charactor_FK_Cast")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Cast'
		verbose_name_plural = 'Casts'
		db_table = 'Cast'
	
class Casting_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Casting_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Casting Department'
		verbose_name_plural = 'Casting Department'
		db_table = 'Casting_department'

class Casting_director(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Casting_director")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Casting Director'
		verbose_name_plural = 'Casting Directors'
		db_table = 'Casting_director'

class Cinematographer(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Cinematographer")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Cinematographer'
		verbose_name_plural = 'Cinematographeres'
		db_table = 'Cinematographer'

class Color_info(models.Model):
	color= models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.color)
	class Meta:
		verbose_name = 'Color Information'
		verbose_name_plural = 'Color Information'
		db_table = 'Color_info'

class Costume_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Costume_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Costume Department'
		verbose_name_plural = 'Costume Department'
		db_table = 'Costume_department'

class Costume_designer(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Costume_designer")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Costume Designer'
		verbose_name_plural = 'Costume Designers'
		db_table = 'Costume_designer'

class Director(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Director")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Director'

class Distributors(models.Model):
	name= models.ForeignKey('Company', verbose_name=u'Person ID',related_name="Person_FK_Distributors")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Distributors'

class Editor(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Editor")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Editor'


class Make_up(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Make_up")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Make Up'
		verbose_name_plural = 'Make Up'
		db_table = 'Make_up'

class Miscellaneous_companies(models.Model):
	name= models.ForeignKey('Company', verbose_name=u'Company ID',related_name="Company_FK_Miscellaneous_companies")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Miscellaneous Companey'
		verbose_name_plural = 'Miscellaneous Companies'
		db_table = 'Miscellaneous_companies'

class Miscellaneous_crew(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Company ID',related_name="Company_FK_Miscellaneous_crew")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Miscellaneous Crew'
		verbose_name_plural = 'Miscellaneous Crew'
		db_table = 'Miscellaneous_crew'

class Music_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Music_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Music Department'
		verbose_name_plural = 'Music Department'
		db_table = 'Music_department'

class Original_music(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Original_music")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Original Music'
		verbose_name_plural = 'Original Music'
		db_table = 'Original_music'

class Producer(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Producer")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:

		db_table = 'Producer'

class Production_companies(models.Model):
	name= models.ForeignKey('Company', verbose_name=u'Company ID',related_name="Company_FK_Production_companies")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Production Companey'
		verbose_name_plural = 'Production Companies'
		db_table = 'Production_companies'

class Production_design(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Production_design")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Production Design'
		verbose_name_plural = 'Production Designers'
		db_table = 'Production_design'

class Production_manager(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Production_manager")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Production Manager'
		verbose_name_plural = 'Production Managers'
		db_table = 'Production_manager'

class Runtimes(models.Model):
	name= models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Run Time'
		verbose_name_plural = 'Run Times'
		db_table = 'Runtimes'

class Set_decoration(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Set_decoration")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Set Decoration'
		verbose_name_plural = 'Set Decorations'
		db_table = 'Set_decoration'

class Sound_crew(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Sound_crew")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Sound Crew'
		verbose_name_plural = 'Sound Crew'
		db_table = 'Sound_crew'

class Special_effects_companies(models.Model):
	name= models.ForeignKey('Company', verbose_name=u'Compny ID',related_name="Person_FK_Special_effects_companies")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Special Effects Companey'
		verbose_name_plural = 'Special Effects Companies'
		db_table = 'Special_effects_companies'

class Special_effects_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Special_effects_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Special Effects Department'
		verbose_name_plural = 'Special Effects Departments'
		db_table = 'Special_effects_department'

class Stunt_performer(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Stunt_performer")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Stunt Performer'
		verbose_name_plural = 'Stunt Performers'
		db_table = 'Stunt_performer'

class Transportation_department(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Transportation_department")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Transportation Department'
		verbose_name_plural = 'Transportation Departments'
		db_table = 'Transportation_department'

class Visual_effects(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Visual_effects")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		verbose_name = 'Visual Effect'
		verbose_name_plural = 'Visual Effects'
		db_table = 'Visual_effects'

class Writer(models.Model):
	name= models.ForeignKey('Person', verbose_name=u'Person ID',related_name="Person_FK_Writer")
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		
		db_table = 'Writer'

class Person(models.Model):
	personID=models.CharField(max_length=100,unique=True)
	name=models.CharField(max_length=100,)
	note=models.TextField(blank=True, null=True)
	default_info=models.TextField(blank=True, null=True)
	biodata=models.TextField(blank=True, null=True)
	date_of_birth=models.CharField(max_length=100,)
	photo=models.ManyToManyField('Photo', verbose_name=u'Photo',related_name="Photo_M2M_Person",blank=True)
	
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Person'
class Company(models.Model):
	name=models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Company'
class Charactor(models.Model):
	name=models.CharField(max_length=100,)
	roleID=models.CharField(max_length=100,null=True)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'Charactor'
class Plot(models.Model):
	name=models.TextField(blank=True, null=True)
	def __unicode__(self):
		return u'%s' % (self.name)
	class Meta:
		db_table = 'plot'
class Photo(models.Model):
	url=models.CharField(max_length=100,)
	def __unicode__(self):
		return u'%s' % (self.url)
	class Meta:
		db_table = 'Photo'

#-----------------------------------------------------------------

class Genre(models.Model):
	''''''
	display_name= models.CharField(max_length=100,unique=True)
	name 		= models.CharField(max_length=100,unique=True)
	total_movie	= models.IntegerField(null=True, blank=True,default=0)
	
	def __unicode__(self):
		return self.name
		
class movieurl(models.Model):
	imdbid =models.SlugField(max_length=200,unique=True)
	movie_name=models.CharField(max_length=500)
	runcount 				=models.IntegerField(null=True, blank=True,default=0)
	url 						= models.CharField(max_length=500)
	filter_based_on	= models.ForeignKey('Genre', verbose_name=u'Genre name')
	sucess_factor 	= models.IntegerField(null=True, blank=True,default=0)
	run_date 				=models.DateTimeField(null=True, blank=True) 
	last_rundate		=models.DateTimeField(null=True, blank=True) 
	
	def __unicode__(self):
		return self.url
		
class Urllog(models.Model):
	''''''
	start_url_id 	=models.IntegerField(null=False, blank=False)
	end_url_id		=models.IntegerField(null=False, blank=False)
	end_date			=models.DateTimeField(null=True, blank=True)  
	
	def __unicode__(self):
		return str(self.end_date)
		
class Errorlog(models.Model):
	
	function_name	= models.CharField(max_length=500)
	message		= models.CharField(max_length=500)
	date		= models.DateTimeField(null=True, blank=True) 
	def __unicode__(self):
		return self.message
		
		
class Movie_Fetch_Statistics(models.Model):
	start_date= models.DateTimeField(null=True, blank=True) 
	end_date= models.DateTimeField(null=True, blank=True) 
	total_count =models.IntegerField(null=False, blank=False,default=0)
	total_run_count =models.IntegerField(null=False, blank=False,default=0)
	start_movie_imdbid= models.CharField(max_length=100)
	end_movie_imdbid= models.CharField(max_length=100)
	
	class Meta:
		verbose_name = 'Movie Extractor Statistics'
		verbose_name_plural = 'Movie Extractor Statistics'

	
class Video(models.Model):
	movie_id=models.IntegerField(null=False, blank=False,default=0)
	imdbid=models.CharField(max_length=100)
	video_url= models.CharField(max_length=255,unique=True)
	movie_url= models.CharField(max_length=500)
	
	class Meta:
		verbose_name = 'Video'
		verbose_name_plural = 'Videos'
		db_table = 'Video'

class Boxoffice(models.Model):
	imdbid  = models.ForeignKey('Movie', verbose_name=u'Movie')
	country= models.ManyToManyField('Countries', verbose_name=u'country')
	date		= models.DateField(null=True, blank=True)
	
	class Meta:
		verbose_name = 'Boxoffice'
		verbose_name_plural = 'Boxoffice'
		db_table = 'Boxoffice'
		 
class Upcoming(models.Model):
	imdbid  = models.ForeignKey('Movie', verbose_name=u'Movie')
	country= models.ManyToManyField('Countries', verbose_name=u'country')
	date		= models.DateField(null=True, blank=True) 
	
	class Meta:
		verbose_name = 'Upcoming'
		verbose_name_plural = 'Upcoming'
		db_table = 'Upcoming'
class Opening(models.Model):
	imdbid  = models.ForeignKey('Movie', verbose_name=u'Movie')
	country= models.ManyToManyField('Countries', verbose_name=u'country')
	date		= models.DateField(null=True, blank=True) 
	
	class Meta:
		verbose_name = 'Opening'
		verbose_name_plural = 'Opening'
		db_table = 'Opening'
		
class Intheaters(models.Model):
	imdbid  = models.ForeignKey('Movie', verbose_name=u'Movie')
	country= models.ManyToManyField('Countries', verbose_name=u'country')
	date		= models.DateField(null=True, blank=True) 
	
	class Meta:
		verbose_name = 'Intheaters'
		verbose_name_plural = 'Intheaters'
		db_table = 'Intheaters'




class Updatehistory(models.Model):
	
	date  = models.DateTimeField(null=True, blank=True)
	boxoffice  = models.IntegerField(null=True, blank=True,default=0)
	upcoming  = models.IntegerField(null=True, blank=True,default=0)
	intheaters  = models.IntegerField(null=True, blank=True,default=0)
	opening  = models.IntegerField(null=True, blank=True,default=0)
	user  = models.IntegerField(null=True, blank=True,default=0)
	movie  = models.IntegerField(null=True, blank=True,default=0)
	akas  	= models.IntegerField(null=True, blank=True,default=0)
	
	plot= models.IntegerField(null=True, blank=True,default=0)
	certificates= models.IntegerField(null=True, blank=True,default=0)
	countries= models.IntegerField(null=True, blank=True,default=0)
	genres= models.IntegerField(null=True, blank=True,default=0)
	sound_mix= models.IntegerField(null=True, blank=True,default=0)
	animation_department= models.IntegerField(null=True, blank=True,default=0)
	art_department= models.IntegerField(null=True, blank=True,default=0)
	art_direction= models.IntegerField(null=True, blank=True,default=0)
	assistant_director= models.IntegerField(null=True, blank=True,default=0)
	camera_and_electrical_department= models.IntegerField(null=True, blank=True,default=0)
	cast= models.IntegerField(null=True, blank=True,default=0)
	casting_department= models.IntegerField(null=True, blank=True,default=0)
	casting_director= models.IntegerField(null=True, blank=True,default=0)
	cinematographer= models.IntegerField(null=True, blank=True,default=0)
	color_info= models.IntegerField(null=True, blank=True,default=0)
	costume_department= models.IntegerField(null=True, blank=True,default=0)
	costume_designer= models.IntegerField(null=True, blank=True,default=0)
	director= models.IntegerField(null=True, blank=True,default=0)
	distributors= models.IntegerField(null=True, blank=True,default=0)
	editor= models.IntegerField(null=True, blank=True,default=0)
	languages= models.IntegerField(null=True, blank=True,default=0)
	make_up= models.IntegerField(null=True, blank=True,default=0)
	miscellaneous_companies= models.IntegerField(null=True, blank=True,default=0)
	miscellaneous_crew= models.IntegerField(null=True, blank=True,default=0)
	music_department= models.IntegerField(null=True, blank=True,default=0)
	original_music= models.IntegerField(null=True, blank=True,default=0)
	producer= models.IntegerField(null=True, blank=True,default=0)
	production_companies= models.IntegerField(null=True, blank=True,default=0)
	production_design= models.IntegerField(null=True, blank=True,default=0)
	production_manager= models.IntegerField(null=True, blank=True,default=0)
	runtimes= models.IntegerField(null=True, blank=True,default=0)
	set_decoration= models.IntegerField(null=True, blank=True,default=0)
	sound_crew= models.IntegerField(null=True, blank=True,default=0)
	special_effects_companies= models.IntegerField(null=True, blank=True,default=0)
	special_effects_department= models.IntegerField(null=True, blank=True,default=0)
	stunt_performer= models.IntegerField(null=True, blank=True,default=0)
	transportation_department= models.IntegerField(null=True, blank=True,default=0)
	visual_effects= models.IntegerField(null=True, blank=True,default=0)
	writer= models.IntegerField(null=True, blank=True,default=0)
	Video= models.IntegerField(null=True, blank=True,default=0)
	release_date = models.IntegerField(null=True, blank=True,default=0)

	
	def __unicode__(self):
		return u'%s' % (self.date)
	class Meta:
		verbose_name = 'Updatehistory'
		verbose_name_plural = 'Updatehistory'
		db_table = 'Updatehistory'
		
class Person_Statistics(models.Model):
	date  = models.DateTimeField(null=True, blank=True)
	person= models.ForeignKey('Person', verbose_name=u'Person')
	name=models.BooleanField(default=False)
	note=models.BooleanField(default=False)
	default_info=models.BooleanField(default=False)
	biodata=models.BooleanField(default=False)
	date_of_birth=models.BooleanField(default=False)
	photo=models.BooleanField(default=False)
	
	class Meta:
		verbose_name = 'Person_Statistics'
		verbose_name_plural = 'Person_Statistics'
		db_table = 'Person_Statistics'
