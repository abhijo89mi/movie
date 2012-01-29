from django.db import models
from movie.widgets import *
from django.db.models.query import QuerySet
from django.contrib.sitemaps import ping_google
import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from movie.main.models import Movie,Countries

GENTER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Navigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    nav_class = models.CharField(max_length=30, null=True, blank=True)
    image = RemovableImageField(upload_to='images/navigations/', null=True, blank=True)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ['order',]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if 'home' in self.slug:
            return ''
        return '%s/' % (self.slug)

    def save(self, **kwargs):
        dir = self.slug+'/'
        #self.content=migrate(dir, self.content)
        super(Navigation, self).save(**kwargs)
        try:
            ping_google()
        except Exception:
            pass

class SubNavigationManager(models.Manager):
    def publish(self):
        return self.filter(publish=True)

class SubNavigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    order = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    navigation = models.ForeignKey(Navigation)
    external_url = models.CharField(max_length=200, null=True, blank=True)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    objects = SubNavigationManager()

    class Meta:
        ordering = ['order', 'title']
        unique_together  = (('order', 'navigation'),)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.external_url:
            return self.external_url
        else:
            return '%s/%s/' % (self.navigation.slug, self.slug)

    def save(self, **kwargs):
        dir = self.navigation.slug+'/'+self.slug+'/'
        #self.content=migrate(dir, self.content)
        super(SubNavigation, self).save(**kwargs)
        try:
            ping_google()
        except Exception:
            pass

class Team_Members(models.Model):
  name=models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  order = models.IntegerField(null=True, blank=True, unique=True)
  image= RemovableImageField(upload_to='images/team_memders/', null=True, blank=True)
  email=models.CharField(max_length=200)
  phone= models.CharField(max_length=200)
  address=models.TextField(null=True, blank=True)
  about= models.TextField(null=True, blank=True)
  note= models.TextField(null=True, blank=True)
  publish = models.BooleanField(default=True)
  publish_date = models.DateTimeField(default=datetime.datetime.now())
  
  def __unicode__(self):
    return self.name
    
  def get_absolute_url(self):
    return '%s/' % (self.slug)
    
class UserProfile(models.Model):
    '''This class will store extra user information to database'''
    user  = models.ForeignKey(User, unique=True)
    is_active=models.BooleanField(default=False)
    city  = models.ForeignKey('City', related_name="city", null=True, blank=True)
    gender  = models.CharField(max_length=1, choices=GENTER_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    secret_key = models.CharField(max_length=200, null=True, blank=True)
    addresses = models.ManyToManyField('Address', through='AddressType')
    send_me_daily_email = models.BooleanField(default=True)
    send_me_daily_sms = models.BooleanField(default=False)
    profile_pic = RemovableImageField(upload_to="images/profile_pics", default="images/profile_pics/profile.png")
    viewed_movie = models.ManyToManyField(Movie)
    friends = models.ManyToManyField(User, related_name='friends')

    def home_address(self):
        if self.addresstype_set.filter(name__iexact='Home'):
            return self.addresstype_set.filter(name__iexact='Home')[0].address
        return False

    def work_address(self):
        if self.addresstype_set.filter(name__iexact='Work'):
            return self.addresstype_set.filter(name__iexact='Work')[0].address
        return False

    def other_address(self):
        from django.db.models import Q
        addresses = self.addresstype_set.filter(~Q(name__iexact='Work')).filter(~Q(name__iexact='Home'))
        if addresses.count() != 0:
            return addresses.all()[0].address
        return False

    def __unicode__(self):
        return self.user.username

class City(models.Model):
    ''' This class will store all Cites for the user '''
    name = models.CharField(max_length=100, unique=True)
    live = models.BooleanField(default=False)
    country =models.ForeignKey(Countries, related_name="country", null=True, blank=True)
    slug  = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ('name', )

    def __unicode__(self):
        return self.name
        
class State(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
        
class AddressType(models.Model):
    name = models.CharField(max_length=20)
    address = models.ForeignKey('Address', null=True, blank=True)
    user_profile = models.ForeignKey('UserProfile')

    def __unicode__(self):
        return self.name
        
        
class Address(models.Model):
    city = models.ForeignKey('City', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=13, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=13, null=True, blank=True)
    phoneNumber = models.CharField(max_length=20,null=False, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    user_streetAddress = models.CharField(max_length=500,null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.name
    



