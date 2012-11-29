from utils import unique_slugify

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from datetime import datetime


class Product(models.Model):
    reference = models.CharField(max_length=10)
    price_in_dollars = models.DecimalField(default=4.99, max_digits=5, decimal_places=2)
    sold = models.IntegerField(default=0)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')

    def __unicode__(self):
        return self.reference


class Video(models.Model):
    video = models.FileField(upload_to='lectures')
    duration = models.IntegerField('duration in seconds', default=3600)
    # format = models.CharField('file format', max_length=20, default='MKV')
    subtitle = models.FileField(upload_to='subtitles', blank=True)
    subtitle_language = models.CharField(max_length=20, default='English')

    class Meta:
        verbose_name = ('Video')
        verbose_name_plural = ('Videos')


class Preview(models.Model):
    vimeo_id = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Preview')
        verbose_name_plural = ('Previews')

    def __unicode__(self):
        return self.title


class Lecturer(models.Model):
    user = models.ForeignKey(User, unique=True)

    class Meta:
        verbose_name = ('Lecturer')
        verbose_name_plural = ('Lecturers')

    def __unicode__(self):
        return unicode(self.user)


class Series(models.Model):
    name = models.CharField('lecture series', max_length=100, default='Mycroft Online Lectures')

    class Meta:
        verbose_name = ('Series')
        verbose_name_plural = ('Series')

    def __unicode__(self):
        return self.name


class Poet(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField(default=0)
    year_of_death = models.IntegerField(default=0)
    nationality = models.CharField(max_length=50, default='English')
    description = models.TextField(default="This is the story of this particular poet")

    class Meta:
        verbose_name = ('Poet')
        verbose_name_plural = ('Poets')

    def __unicode__(self):
        return  '%s,  %s' % (self.last_name, self.first_name)


class Poem(models.Model):
    poet = models.ForeignKey(Poet)
    title = models.CharField(max_length=200)
    pub_year = models.IntegerField('data of publishing', default=1900)
    text = models.TextField(blank=True)
    copyright = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Poem')
        verbose_name_plural = ('Poems')

    def __unicode__(self):
        return self.title


class Lecture(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    poem = models.ForeignKey(Poem)
    video = models.ForeignKey(Video)
    preview = models.ForeignKey(Preview)
    product = models.ForeignKey(Product)
    series = models.ForeignKey(Series)
    synopsis = models.TextField(blank=True)
    transcript = models.TextField(blank=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=40, unique=True, default="")

    class Meta:
        verbose_name = u'Lecture'
        verbose_name_plural = u'Lectures'

    def save(self, *args, **kwargs):
        if not self.id:
            unique_slugify(self, self.title)

        super(Lecture, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Testimonial(models.Model):
    TEACHER = 'T'
    POET = 'P'
    PROFESSIONS = (
        (TEACHER, 'Teacher'),
        (POET, 'Poet'),)
    profession = models.CharField(max_length=1, choices=PROFESSIONS, default=TEACHER)
    text = models.TextField()
    name = models.CharField(max_length=75)
    published_work = models.CharField(max_length=100, blank=True)
    published_work_url = models.URLField(blank=True)
    credentials = models.TextField()

    class Meta:
        verbose_name = ('Testimonial')
        verbose_name_plural = ('Testimonials')

    def __unicode__(self):
        return self.name
