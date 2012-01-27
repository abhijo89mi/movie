from django.db import models
from movie.widgets import *
from django.db.models.query import QuerySet
from django.contrib.sitemaps import ping_google
import datetime
from django.core.urlresolvers import reverse

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
