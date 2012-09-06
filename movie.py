#!/usr/bin/env python
PYTHON_BIN = "/usr/local/bin/python2.7"
import os, sys, getopt, cStringIO
from imdb import IMDb
sys.path[0:0] = [
		os.path.dirname(__file__) + '/eggs/ipython-0.10.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/South-0.7.1-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/django_markitup-0.5.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/django_robots-0.7.0-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/sorl_thumbnail-11.01-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/BeautifulSoup-3.2.0-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/Markdown-2.0.3-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/djangorecipe-0.99-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/Django-1.2.1-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/zc.recipe.egg-1.3.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/zc.buildout-1.5.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/setuptools-0.6c12dev_r88846-py2.7.egg',
		os.path.dirname(__file__) + '/parts/django',
		os.path.dirname(__file__),
		]

os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.development'
from django.conf import settings
from movie.main.models import *
from datetime import datetime



def fnPerson(person, sucess_factor):

	name = person.data['name']
	if not name : name = '====ERROR====='
	try :
		personID = person.personID
		note = person.notes
		default_info = person.default_info
		biodata = ''
	except KeyError as e:
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
		#save to the tblPerson
	tblPerson , Created = Person.objects.get_or_create(personID = personID, name = name, note = note, default_info = default_info, biodata = biodata)

	return tblPerson

def fnCompany(company):
	name = company.data['name']
	tblCompany , Created = Company.objects.get_or_create(name = name)
	return tblCompany

def fnCharactor(person):
	name = person.currentRole
	roleID = person.roleID
	tblCharactor , Created = Charactor.objects.get_or_create(name = name, roleID = roleID)
	return tblCharactor

def fnMovie (the_matrix, sucess_factor):
	try :
		title = the_matrix.data['title']
	except KeyError as e:
		title = ''
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		votes = the_matrix.data['votes']
	except KeyError as e:
		votes = 0
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		year = the_matrix.data['year']
	except KeyError as e:
		year = 0
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		aspect_ratio = the_matrix.data['aspect ratio']
	except KeyError as e:
		aspect_ratio = ''
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		mpaa = the_matrix.data['mpaa']
	except KeyError as e:
		mpaa = ''
		print str(e)
		pass
	try :
		rating = the_matrix.data['rating']
	except KeyError as e:
		rating = ''
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		imdbid = the_matrix.movieID
	except KeyError as e:
		imdbid = ''
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		top_250_rank = the_matrix.data['top 250 rank']
	except KeyError as e:
		top_250_rank = 10000
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		cover_url = the_matrix.data['cover url']
	except KeyError as e:
		cover_url = ''
		print str(e)
		pass
	try :
		plot_outline = the_matrix.data['plot outline']
	except KeyError as e:
		plot_outline = ''
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	try :
		summary = the_matrix.summary()
	except KeyError as e:
		print str(e)
		sucess_factor = sucess_factor + 1
		pass
	if title == '':
		exit(0)
	tblmovie, created = Movie.objects.get_or_create(title = title, votes = votes, year = year, aspect_ration = aspect_ratio, mpaa = mpaa,
	rating = rating, imdbid = imdbid, top_250_rank = top_250_rank, cover_url = cover_url, plot_outline = plot_outline, summary = summary)

	return tblmovie


def main ():

		count = 1
		data_fetched = 0
		if (len(sys.argv) > 1):
			count = sys.argv[1]
		ia = IMDb()
		# Get url from the tblmovieurl
		url_object = movieurl.objects.filter(runcount__lt = 1)[:count]

		start_movie_id = url_object[0].id
		total_count = int(count)
		total_run_count = 0
		extractor_statistics = Movie_Fetch_Statistics(start_date = datetime.now(), total_count = total_count, start_movie_imdbid = start_movie_id, total_run_count = total_run_count, end_date = datetime.now(), end_movie_imdbid = 0)
		extractor_statistics.save()
		for url in url_object :
			sucess_factor = 0
			imdbid = url.imdbid.replace('tt', '')

			print "Get movie information : " , url.movie_name
			the_matrix = ia.get_movie(imdbid)

			tblmovie = fnMovie(the_matrix, sucess_factor)


			try :
				animation_department = the_matrix.data['animation department']
				for person in animation_department :

					tblperson = fnPerson(person, sucess_factor)
					tblanimation_department, c = Animation_department.objects.get_or_create(name = tblperson)
					tblmovie.animation_department.add(tblanimation_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try :
				art_department = the_matrix.data['art department']
				for person in art_department :

					tblperson = fnPerson(person, sucess_factor)

					tblart_department, c = Art_department.objects.get_or_create(name = tblperson)
					tblmovie.art_department.add(tblart_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try :
				art_direction = the_matrix.data['art direction']
				for person in art_direction :

					tblperson = fnPerson(person, sucess_factor)

					tblart_direction, c = Art_direction.objects.get_or_create(name = tblperson)
					tblmovie.art_direction.add(tblart_direction)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try :
				assistant_director = the_matrix.data['assistant director']
				for person in assistant_director :

					tblperson = fnPerson(person, sucess_factor)

					tblassistant_director, c = Assistant_director.objects.get_or_create(name = tblperson)
					tblmovie.assistant_director.add(tblassistant_director)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				camera_and_electrical_department = the_matrix.data['camera and electrical department']
				for person in camera_and_electrical_department :

					tblperson = fnPerson(person, sucess_factor)

					tblcamera_and_electrical_department, c = Camera_and_electrical_department.objects.get_or_create(name = tblperson)
					tblmovie.camera_and_electrical_department.add(tblcamera_and_electrical_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				casting_department = the_matrix.data['casting department']
				for person in casting_department :

					tblperson = fnPerson(person, sucess_factor)

					tblcasting_department, c = Casting_department.objects.get_or_create(name = tblperson)
					tblmovie.casting_department.add(tblcasting_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:

				casting_director = the_matrix.data['casting director']
				for person in casting_director :

					tblperson = fnPerson(person, sucess_factor)

					tblcasting_director, c = Casting_director.objects.get_or_create(name = tblperson)
					tblmovie.casting_director.add(tblcasting_director)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:

				cinematographer = the_matrix.data['cinematographer']
				for person in cinematographer :

					tblperson = fnPerson(person, sucess_factor)

					tblcinematographer, c = Cinematographer.objects.get_or_create(name = tblperson)
					tblmovie.cinematographer.add(tblcinematographer)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				costume_department = the_matrix.data['costume department']
				for person in costume_department :

					tblperson = fnPerson(person, sucess_factor)

					tblcostume_department, c = Costume_department.objects.get_or_create(name = tblperson)
					tblmovie.costume_department.add(tblcostume_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				costume_designer = the_matrix.data['costume designer']
				for person in costume_designer :

					tblperson = fnPerson(person, sucess_factor)

					tblcostume_designer, c = Costume_designer.objects.get_or_create(name = tblperson)
					tblmovie.costume_designer.add(tblcostume_designer)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				director = the_matrix.data['director']
				for person in director :

					tblperson = fnPerson(person, sucess_factor)
					tbldirector, c = Director.objects.get_or_create(name = tblperson)
					tblmovie.director.add(tbldirector)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try :

				editor = the_matrix.data['editor']
				for person in editor :

					tblperson = fnPerson(person, sucess_factor)

					tbleditor, c = Editor.objects.get_or_create(name = tblperson)
					tblmovie.editor.add(tbleditor)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				make_up = the_matrix.data['make up']
				for person in make_up :

					tblperson = fnPerson(person, sucess_factor)

					tblmake_up, c = Make_up.objects.get_or_create(name = tblperson)
					tblmovie.make_up.add(tblmake_up)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				miscellaneous_crew = the_matrix.data['miscellaneous crew']
				for person in miscellaneous_crew :

					tblperson = fnPerson(person, sucess_factor)

					tblmiscellaneous_crew, c = Miscellaneous_crew.objects.get_or_create(name = tblperson)
					tblmovie.miscellaneous_crew.add(tblmiscellaneous_crew)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				music_department = the_matrix.data['music department']
				for person in music_department :

					tblperson = fnPerson(person, sucess_factor)

					tblmusic_department, c = Music_department.objects.get_or_create(name = tblperson)
					tblmovie.music_department.add(tblmusic_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				original_music = the_matrix.data['original music']
				for person in original_music :

					tblperson = fnPerson(person, sucess_factor)

					tbloriginal_music, c = Original_music.objects.get_or_create(name = tblperson)
					tblmovie.original_music.add(tbloriginal_music)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:

				producer = the_matrix.data['producer']
				for person in producer :

					tblperson = fnPerson(person, sucess_factor)
					tblproducer, c = Producer.objects.get_or_create(name = tblperson)
					tblmovie.producer.add(tblproducer)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:

				production_design = the_matrix.data['production design']
				for person in production_design :

					tblperson = fnPerson(person, sucess_factor)
					tblproduction_design, c = Production_design.objects.get_or_create(name = tblperson)
					tblmovie.production_design.add(tblproduction_design)

			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				production_manager = the_matrix.data['production manager']
				for person in production_manager :

					tblperson = fnPerson(person, sucess_factor)
					tblproduction_manager, c = Production_manager.objects.get_or_create(name = tblperson)
					tblmovie.production_manager.add(tblproduction_manager)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				set_decoration = the_matrix.data['set decoration']
				for person in set_decoration :

					tblperson = fnPerson(person, sucess_factor)
					tblset_decoration, c = Set_decoration.objects.get_or_create(name = tblperson)
					tblmovie.set_decoration.add(tblset_decoration)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				sound_crew = the_matrix.data['sound crew']
				for person in sound_crew :

					tblperson = fnPerson(person, sucess_factor)
					tblsound_crew, c = Sound_crew.objects.get_or_create(name = tblperson)
					tblmovie.sound_crew.add(tblsound_crew)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				special_effects_department = the_matrix.data['special effects department']
				for person in special_effects_department  :

					tblperson = fnPerson(person, sucess_factor)
					tblspecial_effects_department, c = Special_effects_department.objects.get_or_create(name = tblperson)
					tblmovie.special_effects_department.add(tblspecial_effects_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				stunt_performer = the_matrix.data['stunt performer']
				for person in stunt_performer  :

					tblperson = fnPerson(person, sucess_factor)
					tblstunt_performer, c = Stunt_performer.objects.get_or_create(name = tblperson)
					tblmovie.stunt_performer.add(tblstunt_performer)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				transportation_department = the_matrix.data['transportation department']
				for person in transportation_department  :

					tblperson = fnPerson(person, sucess_factor)
					tbltransportation_department, c = Transportation_department.objects.get_or_create(name = tblperson)
					tblmovie.transportation_department.add(tbltransportation_department)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				visual_effects = the_matrix.data['visual effects']
				for person in visual_effects  :

					tblperson = fnPerson(person, sucess_factor)
					tblvisual_effects, c = Visual_effects.objects.get_or_create(name = tblperson)
					tblmovie.visual_effects.add(tblvisual_effects)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				writer = the_matrix.data['writer']
				for person in writer  :

					tblperson = fnPerson(person, sucess_factor)
					tblwriter, c = Writer.objects.get_or_create(name = tblperson)
					tblmovie.writer.add(tblwriter)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				distributors = the_matrix.data['distributors']
				for company in distributors  :

					tblperson = fnCompany(company)
					tbldistributors, c = Distributors.objects.get_or_create(name = tblperson)
					tblmovie.distributors.add(tbldistributors)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				miscellaneous_companies = the_matrix.data['miscellaneous companies']
				for company in miscellaneous_companies  :

					tblcompany = fnCompany(company)
					tblmiscellaneous_companies, c = Miscellaneous_companies.objects.get_or_create(name = tblcompany)
					tblmovie.miscellaneous_companies.add(tblmiscellaneous_companies)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				production_companies = the_matrix.data['production companies']
				for company in production_companies  :

					tblcompany = fnCompany(company)
					tblproduction_companies, c = Production_companies.objects.get_or_create(name = tblcompany)
					tblmovie.production_companies.add(tblproduction_companies)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				special_effects_companies = the_matrix.data['special effects companies']
				for company in special_effects_companies  :

					tblcompany = fnCompany(company)
					tblspecial_effects_companies, c = Special_effects_companies.objects.get_or_create(name = tblcompany)
					tblmovie.special_effects_companies.add(tblspecial_effects_companies)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				cast = the_matrix.data['cast']
				for person in cast:

					tblcharactor = fnCharactor(person)
					tblperson = fnPerson(person, sucess_factor)
					tblcast, c = Cast.objects.get_or_create(name = tblperson)
					tblcast.charactor.add(tblcharactor)
					tblmovie.cast.add(tblcast)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				akas = the_matrix.data['akas']
				for name in akas  :
					tblakas, c = Akas.objects.get_or_create(name = name)
					tblmovie.akas_id.add(tblakas)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				plot = the_matrix.data['plot']
				for name in plot  :
					tblplot, c = Plot.objects.get_or_create(name = name)
					tblmovie.plot.add(tblplot)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				certificates = the_matrix.data['certificates']

				for name in certificates  :
					tblcertificates, c = Certificates.objects.get_or_create(name = name)
					tblmovie.certificates.add(tblcertificates)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass
			try:
				color_info = the_matrix.data['color info']
				for name in color_info  :
					tblcolor_info, c = Color_info.objects.get_or_create(color = name)
					tblmovie.color_info.add(tblcolor_info)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				genres = the_matrix.data['genres']
				for display_name in genres  :
					name = display_name.replace('-', '_').lower()
					tblgenres, c = Genre.objects.get_or_create(display_name = display_name, name = name)
					tblmovie.genres.add(tblgenres)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass


			try:
				runtimes = the_matrix.data['runtimes']
				for name in runtimes  :
					tblruntimes, c = Runtimes.objects.get_or_create(name = name)
					tblmovie.runtimes.add(tblruntimes)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				countries = the_matrix.data['countries']
				code = the_matrix.data['country codes']
				i = 0
				for name in countries  :
					tblcountries, c = Countries.objects.get_or_create(name = name, code = code[i])
					tblmovie.countries.add(tblcountries)
					i = i + 1
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				sound_mix = the_matrix.data['sound mix']
				for name in sound_mix :
					tblsound_mix, c = Sound_mix.objects.get_or_create(name = name)
					tblmovie.sound_mix.add(tblsound_mix)
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			try:
				languages = the_matrix.data['languages']
				code = the_matrix.data['language codes']
				i = 0
				for name in languages  :
					tbllanguages, c = Languages.objects.get_or_create(name = name, code = code[i])
					tblmovie.languages.add(tbllanguages)
					i = i + 1
			except Exception as e:
				print e
				sucess_factor = sucess_factor + 1
				pass

			url.runcount += 1
			url.last_rundate = datetime.now()
			url.save()

			#Update Statistics 
			extractor_statistics.total_run_count += 1
			extractor_statistics.end_date = datetime.now()
			extractor_statistics.end_movie_imdbid = url.id
			extractor_statistics.save()



		return 0

if __name__ == '__main__':

	main()


