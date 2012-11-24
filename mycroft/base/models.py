from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from datetime import datetime


class Lecture(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    poem = models.ForeignKey(Poem)
    video = models.ForeignKey(Video)
    product = models.ForeignKey(Product)
    series = models.ForeignKey(Serie)
    synopsis = models.TextField()
    transcript = models.TextField()

    class Meta:
        verbose_name = u'Lecture'
        verbose_name_plural = u'Lectures'
    
    def __unicode__(self):
        pass

class Product(models.Model):
    reference = models.CharField(max_length=10)
    price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)
    sold = models.IntegerField()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        self.reference

class Video(models.Model):
    full_video = models.FileField(upload_to='lectures')
    preview_video = models.URLField()
    duration = IntegerField('duration in seconds')
    format = models.CharField('file format', max_length=20)
    subtitle = models.FileField(upload_to='subtitles')
    subtitle_language = models.CharField('file format', max_length=20)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __unicode__(self):
        pass
        
class Series(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')

    def __unicode__(self):
        pass
    

class Poet(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField()
    birthplace = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Poet')
        verbose_name_plural = _('Poets')

    def __unicode__(self):
        return self.first_name, self.last_name


class Poem(models.Model):
    poet = models.ForeignKey(Poet)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data of publishing')
    text = models.TextField()
    copyright = models.BooleanField()

    class Meta:
        verbose_name = _('Poem')
        verbose_name_plural = _('Poems')

    def __unicode__(self):
        return self.title


class Lecturer(models.Model):
    user = models.ForeignKey(User, unique=True)

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')

    def __unicode__(self):
        pass


class Testimonial(models.Model):
    TEACHER = 'T'
    POET = 'P'
    PROFESSIONS = (
        (TEACHER, 'Teacher'),
        (POET, 'Poet'),)
    profession = models.CharField(max_length=1, choices=PROFESSIONS, default=TEACHER)
    text = models.TextField()
    name = models.CharField(max_length=75)
    published_work = models.CharField(max_length=100)
    published_worl_url = models.URLField()
    credentials = models.TextField()

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __unicode__(self):
        pass
