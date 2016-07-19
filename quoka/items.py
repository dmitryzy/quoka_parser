# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class QuokaItem(scrapy.Item):
    id = scrapy.Field()
    Boersen_ID = scrapy.Field()
    OBID = scrapy.Field()
    erzeugt_am = scrapy.Field()
    Anbieter_ID = scrapy.Field()
    Anbieter_ObjektID = scrapy.Field()
    Immobilientyp = scrapy.Field()
    Immobilientyp_detail = scrapy.Field()
    Vermarktungstyp = scrapy.Field()
    Land = scrapy.Field()
    Bundesland = scrapy.Field()
    Bezirk = scrapy.Field()
    Stadt = scrapy.Field()
    PLZ = scrapy.Field()
    Strasse = scrapy.Field()
    Hausnummer = scrapy.Field()
    Uberschrift = scrapy.Field()
    Beschreibung = scrapy.Field()
    Etage = scrapy.Field()
    Kaufpreis = scrapy.Field()
    Kaltmiete = scrapy.Field()
    Warmmiete = scrapy.Field()
    Nebenkosten = scrapy.Field()
    Zimmeranzahl = scrapy.Field()
    Wohnflaeche = scrapy.Field()
    Monat = scrapy.Field()
    url = scrapy.Field()
    Telefon = scrapy.Field()
    Erstellungsdatum = scrapy.Field()
    Gewerblich = scrapy.Field()


