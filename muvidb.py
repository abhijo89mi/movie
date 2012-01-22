#!/usr/local/bin/python2.7


PYTHON_BIN = "/usr/local/bin/python2.7"
import os, sys, getopt, cStringIO
from imdb import IMDb
sys.path[0:0] = [
		os.path.dirname(__file__)+'/eggs/ipython-0.10.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/South-0.7.1-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/django_markitup-0.5.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/django_robots-0.7.0-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/sorl_thumbnail-11.01-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/BeautifulSoup-3.2.0-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/Markdown-2.0.3-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/djangorecipe-0.99-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/Django-1.2.1-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/zc.recipe.egg-1.3.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/zc.buildout-1.5.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/setuptools-0.6c12dev_r88846-py2.7.egg',
		os.path.dirname(__file__)+'/parts/django',
		os.path.dirname(__file__),
		]
		
os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.development'
from django.conf import settings
from movie.main.models import *
from datetime import datetime
def fnPerson(person):
	
	name=person.data['name']
	if not name : name ='====ERROR====='
	try :
		personID=person.personID
		note=person.notes
		default_info=person.default_info
		biodata=''
	except KeyError as e:
		print str(e)
		pass
		#save to the tblPerson
	tblPerson ,Created =Person.objects.get_or_create(personID=personID,name=name,note=note,default_info=default_info,biodata=biodata)
		
	return tblPerson

def fnMovie (the_matrix):
	try :
		title=the_matrix.data['title']
	except KeyError as e:
		title=''
		print str(e)
		pass
	try :
		votes=the_matrix.data['votes']
	except KeyError as e:
		votes=0
		print str(e)
		pass
	try :
		year=the_matrix.data['year']
	except KeyError as e:
		year=0
		print str(e)
		pass
	try :
		aspect_ratio=the_matrix.data['aspect ratio']
	except KeyError as e:
		aspect_ratio=''
		print str(e)
		pass
	try :
		mpaa=the_matrix.data['mpaa']
	except KeyError as e:
		mpaa=''
		print str(e)
		pass
	try :
		rating=the_matrix.data['rating']
	except KeyError as e:
		rating=''
		print str(e)
		pass
	try :
		imdbid=the_matrix.movieID
	except KeyError as e:
		imdbid=''
		print str(e)
		pass
	try :
		top_250_rank=the_matrix.data['top 250 rank']
	except KeyError as e:
		top_250_rank=10000
		print str(e)
		pass
	try :
		cover_url=the_matrix.data['cover url']
	except KeyError as e:
		cover_url=''
		print str(e)
		pass
	try :
		plot_outline=the_matrix.data['plot outline']
	except KeyError as e:
		plot_outline=''
		print str(e)
		pass
	try :
		summary=the_matrix.summary()
	except KeyError as e:
		print str(e)
		pass
	tblmovie, created =Movie.objects.get_or_create(title=title,votes=votes,year=year,aspect_ration=aspect_ratio,mpaa=mpaa,
	rating=rating,imdbid=imdbid,top_250_rank=top_250_rank,cover_url=cover_url,plot_outline=plot_outline,summary=summary)
	
	return tblmovie
	

def main ():
	
		ia = IMDb()
		# Get url from the tblmovieurl
		url_object =movieurl.objects.filter(runcount__lt=1)[:100]
		for url in url_object :
			imdbid=url.imdbid.replace('tt','')
			
			print "Get movie information : " , url.movie_name
			the_matrix = ia.get_movie(imdbid)
			
			tblmovie =fnMovie(the_matrix)
			try :
				animation_department=the_matrix.data['animation department']
				for person in animation_department :
					
					tblperson = fnPerson(person)
					tblanimation_department,c = Animation_department.objects.get_or_create(name=tblperson)
					tblmovie.animation_department.add(tblanimation_department)
			except Exception as e:
				print e
				pass
			try :
				art_department = the_matrix.data['art department']
				for person in art_department :
					
					tblperson = fnPerson(person)
					
					tblart_department,c = Art_department.objects.get_or_create(name=tblperson)
					tblmovie.art_department.add(tblart_department)
			except Exception as e:
				print e
				pass
			try :	
				art_direction=the_matrix.data['art direction']
				for person in art_direction :
					
					tblperson = fnPerson(person)
					
					tblart_direction,c = Art_direction.objects.get_or_create(name=tblperson)
					tblmovie.art_direction.add(tblart_direction)
			except Exception as e:
				print e
				pass
			try :
				assistant_director=the_matrix.data['assistant director']
				for person in assistant_director :
					
					tblperson = fnPerson(person)
					
					tblassistant_director,c = Assistant_director.objects.get_or_create(name=tblperson)
					tblmovie.assistant_director.add(tblassistant_director)
			except Exception as e:
				print e
				pass
			try:
				camera_and_electrical_department=the_matrix.data['camera and electrical department']
				for person in camera_and_electrical_department :
					
					tblperson = fnPerson(person)
					
					tblcamera_and_electrical_department,c = Camera_and_electrical_department.objects.get_or_create(name=tblperson)
					tblmovie.camera_and_electrical_department.add(tblcamera_and_electrical_department)
			except Exception as e:
				print e
				pass
			try:
				casting_department=the_matrix.data['casting department']
				for person in casting_department :
					
					tblperson = fnPerson(person)
					
					tblcasting_department,c = Casting_department.objects.get_or_create(name=tblperson)
					tblmovie.casting_department.add(tblcasting_department)
			except Exception as e:
				print e
				pass
			try:
				
				casting_director=the_matrix.data['casting director']
				for person in casting_director :
					
					tblperson = fnPerson(person)
					
					tblcasting_director,c = Casting_director.objects.get_or_create(name=tblperson)
					tblmovie.casting_director.add(tblcasting_director)
			except Exception as e:
				print e
				pass
			try:
				
				cinematographer=the_matrix.data['cinematographer']
				for person in cinematographer :
					
					tblperson = fnPerson(person)
					
					tblcinematographer,c = Cinematographer.objects.get_or_create(name=tblperson)
					tblmovie.cinematographer.add(tblcinematographer)
			except Exception as e:
				print e
				pass
			try:
				costume_department=the_matrix.data['costume department']
				for person in costume_department :
					
					tblperson = fnPerson(person)
					
					tblcostume_department,c = Costume_department.objects.get_or_create(name=tblperson)
					tblmovie.costume_department.add(tblcostume_department)
			except Exception as e:
				print e
				pass
			try:
				costume_designer=the_matrix.data['costume designer']
				for person in costume_designer :
					
					tblperson = fnPerson(person)
					
					tblcostume_designer,c = Costume_designer.objects.get_or_create(name=tblperson)
					tblmovie.costume_designer.add(tblcostume_designer)
			except Exception as e:
				print e
				pass
				
			try:
				director = the_matrix.data['director']
				for person in director :
					
					tblperson = fnPerson(person)
					tbldirector,c = Director.objects.get_or_create(name=tblperson)
					tblmovie.director.add(tbldirector)
			except Exception as e:
				print e
				pass
			try :
				
				editor=the_matrix.data['editor']
				for person in editor :
					
					tblperson = fnPerson(person)
					
					tbleditor,c = Editor.objects.get_or_create(name=tblperson)
					tblmovie.editor.add(tbleditor)
			except Exception as e:
				print e
				pass
				
			try:
				make_up=the_matrix.data['make up']
				for person in make_up :
					
					tblperson = fnPerson(person)
					
					tblmake_up,c = Make_up.objects.get_or_create(name=tblperson)
					tblmovie.make_up.add(tblmake_up)
			except Exception as e:
				print e
				pass
			try:
				miscellaneous_crew=the_matrix.data['miscellaneous crew']
				for person in miscellaneous_crew :
					
					tblperson = fnPerson(person)
					
					tblmiscellaneous_crew,c = Miscellaneous_crew.objects.get_or_create(name=tblperson)
					tblmovie.miscellaneous_crew.add(tblmiscellaneous_crew)
			except Exception as e:
				print e
				pass
			try:
				music_department=the_matrix.data['music department']
				for person in music_department :
					
					tblperson = fnPerson(person)
					
					tblmusic_department,c = Music_department.objects.get_or_create(name=tblperson)
					tblmovie.music_department.add(tblmusic_department)
			except Exception as e:
				print e
				pass
			try:
				original_music=the_matrix.data['original music']
				for person in original_music :
					
					tblperson = fnPerson(person)
					
					tbloriginal_music,c = Original_music.objects.get_or_create(name=tblperson)
					tblmovie.original_music.add(tbloriginal_music)
			except Exception as e:
				print e
				pass
			
			try:
				
				producer=the_matrix.data['producer']
				for person in producer :
					
					tblperson = fnPerson(person)
					tblproducer,c = Producer.objects.get_or_create(name=tblperson)
					tblmovie.producer.add(tblproducer)
			except Exception as e:
				print e
				pass
			try:
				
				production_design=the_matrix.data['production design']
				for person in production_design :
					
					tblperson = fnPerson(person)
					tblproduction_design,c = Production_design.objects.get_or_create(name=tblperson)
					tblmovie.production_design.add(tblproduction_design)
					
			except Exception as e:
				print e
				pass
			try:
				production_manager=the_matrix.data['production manager']
				for person in production_manager :
					
					tblperson = fnPerson(person)
					tblproduction_manager,c = Production_manager.objects.get_or_create(name=tblperson)
					tblmovie.production_manager.add(tblproduction_manager)
			except Exception as e:
				print e
				pass
			try:
				set_decoration=the_matrix.data['set decoration']
				for person in set_decoration :
					
					tblperson = fnPerson(person)
					tblset_decoration,c = Set_decoration.objects.get_or_create(name=tblperson)
					tblmovie.set_decoration.add(tblset_decoration)
			except Exception as e:
				print e
				pass
			try:
				sound_crew=the_matrix.data['sound crew']
				for person in sound_crew :
					
					tblperson = fnPerson(person)
					tblsound_crew,c = Sound_crew.objects.get_or_create(name=tblperson)
					tblmovie.sound_crew.add(tblsound_crew)
			except Exception as e:
				print e
				pass
			try:
				special_effects_department=the_matrix.data['special effects department']
				for person in special_effects_department  :
					
					tblperson = fnPerson(person)
					tblspecial_effects_department,c = Special_effects_department.objects.get_or_create(name=tblperson)
					tblmovie.special_effects_department.add(tblspecial_effects_department)
			except Exception as e:
				print e
				pass
			try:
				stunt_performer=the_matrix.data['stunt performer']
				for person in stunt_performer  :
					
					tblperson = fnPerson(person)
					tblstunt_performer,c = Stunt_performer.objects.get_or_create(name=tblperson)
					tblmovie.stunt_performer.add(tblstunt_performer)
			except Exception as e:
				print e
				pass
			try:
				transportation_department=the_matrix.data['transportation department']
				for person in transportation_department  :
					
					tblperson = fnPerson(person)
					tbltransportation_department,c = Transportation_department.objects.get_or_create(name=tblperson)
					tblmovie.transportation_department.add(tbltransportation_department)
			except Exception as e:
				print e
				pass
			visual_effects=the_matrix.data['visual effects']
			for person in visual_effects  :
				
				tblperson = fnPerson(person)
				tblvisual_effects,c = Visual_effects.objects.get_or_create(name=tblperson)
				tblmovie.visual_effects.add(tblvisual_effects)

			writer=the_matrix.data['writer']
			for person in visual_effects  :
				
				tblperson = fnPerson(person)
				tblwriter,c = Writer.objects.get_or_create(name=tblperson)
				tblmovie.writer.add(tblwriter)
			url.runcount+=1	
			url.last_rundate=datetime.now()
			url.save()

		return 0
		
if __name__ == '__main__':
	
	main()


