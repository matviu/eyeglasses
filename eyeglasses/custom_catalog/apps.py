# -*- coding: utf-8 -*-
from django.apps import AppConfig


class CustomCatalogConfig(AppConfig):
	name = u'eyeglasses.custom_catalog'
	verbose_name = u'Каталог'

	def ready(self):
		import catalog.signals