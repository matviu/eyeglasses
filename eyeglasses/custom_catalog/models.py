# -*- coding: utf-8 -*-
from django.db import models
from catalog.models import CatalogBase
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class MyCatalogBase(CatalogBase):
	name = models.CharField(max_length=200, verbose_name=u'название')
	slug = models.SlugField(max_length=200, verbose_name=u'слаг')
	description = models.TextField(max_length=500, verbose_name=u'описание', blank=True)

	class Meta:
		abstract = True



class Eyeglasses(MyCatalogBase):
	price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'цена', blank=True)
	discount = models.PositiveSmallIntegerField(default=0, verbose_name=u'скидка(в процентах)',
	                                            validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
	rating =  models.PositiveSmallIntegerField(default = 5, verbose_name=u'рейтинг',
	                                           validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True)
	leaf = True
	EYEGLASSES_TYPE = (
		(u'1', u'тонкое стекло'),
		(u'2', u'среднее стекло'),
		(u'3', u'толстое стекло'),
	)
	type = models.CharField(max_length=50, choices=EYEGLASSES_TYPE, blank=True)

	class Meta:
		verbose_name = u'очки'
		verbose_name_plural = u'очки'

	def __unicode__(self):
		return u'очки %s' % self.name


class Section(MyCatalogBase):
	add_description = models.TextField(max_length=500, verbose_name=u'дополнительное описание', blank=True)
	leaf = False

	class Meta:
		verbose_name = u'раздел'
		verbose_name_plural = u'разделы'

	def __unicode__(self):
		return u'Раздел каталога %s' % self.name
