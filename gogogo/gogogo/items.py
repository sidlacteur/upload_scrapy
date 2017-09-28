# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GogogoItem(scrapy.Item):
    url_image_full = scrapy.Field()
    url_image_thumb = scrapy.Field()
    url = scrapy.Field()
    identifiant = scrapy.Field()
    izza_code = scrapy.Field()
    ean = scrapy.Field()
    isbn = scrapy.Field()
    titre = scrapy.Field()
    prix = scrapy.Field()
    langue = scrapy.Field()
    date_parution = scrapy.Field()
    nombre_pages = scrapy.Field()
    poids = scrapy.Field()
    preface = scrapy.Field()
    auteur = scrapy.Field()
    traducteur=scrapy.Field()
    themes = scrapy.Field()
    tomes = scrapy.Field()
    volumes = scrapy.Field()
    numero_edition=scrapy.Field()
    collection = scrapy.Field()
    serie = scrapy.Field()
    format_livre = scrapy.Field()
    dimension = scrapy.Field()
    presentation = scrapy.Field()
    edition = scrapy.Field()
    source = scrapy.Field()
    note = scrapy.Field()
    type_livre = scrapy.Field()
    image_full = scrapy.Field()
    image_thumb = scrapy.Field()
    quantite= scrapy.Field()
