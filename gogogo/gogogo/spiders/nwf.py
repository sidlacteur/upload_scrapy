# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from gogogo.items import GogogoItem

from scrapy.linkextractors import LinkExtractor
EDITEUR='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[8]/td[1]/text()'
TITRED='.//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[2]/td[1]/text()'
PRIX='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[7]/td[2]/text()'
AUTEURD='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[6]/td[2]/a/text()'
DATEPARUTION='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[6]/td[2]/text()'
TRADUCTION='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[7]/td[1]/text()'
EDITEUR='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[8]/td[1]/text()'
COLLECTION='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[8]/td[1]/a/text()'
DIMENSION='//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[9]/td[1]/text()'
IMAGEL='.//*[@id="body-wrapper"]/div[1]/div[1]/table/tr/td[@class="image"]/img/@src'
EAN='.//*[@id="body-wrapper"]/div[1]/div[1]/table/tr[13]/td[1]/text()'
TEST='.//*[@id="body-wrapper"]/div[1]/div[1]/table/tr/descendant::*/text()'
THEME='.//*[@name="itemKeywords"]/@content'
def nettoyer(elm):
    return (elm.replace('\n','').strip())
class NwfSpider(scrapy.Spider):
    name = "nwf"
    allowed_domains = ["www.neelwafurat.com"]
    start_urls = (
        'http://www.neelwafurat.com/itempage.aspx?id=lbb212312-230451&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb249482-230962&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb245170-226167&search=books',
        'http://www.neelwafurat.com/browse.aspx?ddmsubject=01&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb255714-238540&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb247307-228491&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb119397-79524&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=egb120195-5158005&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=lbb255714-238540&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=egb159739-5170983&search=books',
        'http://www.neelwafurat.com/itempage.aspx?id=egb176034-5188471&search=books',
    )
    rules = (Rule (LinkExtractor(allow=(),deny=(),restrict_xpaths=()), callback="parse_o", follow= True),)

    def parse(self, response):
        livre = GogogoItem()
        livre['url'] = response.url
        livre['source'] = 'nwf'
        fichTechs=response.xpath(TEST).extract()
        for i in range(len(fichTechs)):
            fichTechs[i] = fichTechs[i].replace('\n','').strip()
        fichTech = list(filter(None,fichTechs))
        for i in range(len(fichTech)):
            if fichTech[i]=='الكمية:':
                try:
                    while isinstance(int(fichTech[i+1]),int):
                        fichTech.remove(fichTech[i+1])
                        continue
                except:
                    break
        try:
            fichTech.remove('الكمية:')
        except:
            pass
        fi={}
        for i in range(len(fichTech)):
            if ':' in fichTech[i]:

                z=i+1
                if z < len(fichTech)-1:
                    lot=[]
                    while not (':' in fichTech[z]):
                        lot.append(fichTech[z])
                        z+=1
                    fi[fichTech[i]]  =lot

        print(fichTech)
        #i=iter(fichTech)
        #dicos=dict(zip(i,i))
        #print(dicos)
        livre['titre'] = response.xpath(TITRED).extract()
        livre['ean'] =  response.xpath(EAN).extract()
        livre['auteur'] =  response.xpath(AUTEURD).extract()
        livre['edition'] =  response.xpath(EDITEUR).extract()
        livre['prix'] =  response.xpath(PRIX).extract()
        livre['themes'] =  response.xpath(THEME).extract()
        livre['image_thumb'] =  response.xpath(IMAGEL).extract()
        livre['image_thumb'] =  livre['image_thumb'][0].strip()
        try:
            livre['langue'] =  fi['اللغة:']
        except:
            pass
        try:
            livre['dimension'] =  fi['حجم:']
        except:
            pass
        try:
            livre['presentation'] =fi['النوع:']
        except:
            pass
        try:
            livre['date_parution'] =  fi['تاريخ النشر:']
        except:
            pass
        try:
            livre['nombre_pages'] =  fi['عدد الصفحات:']
        except:
            pass
        try:
            livre['traducteur'] =  fi['ترجمة، تحقيق:']
        except:
            pass
        livre['collection'] =  response.xpath(COLLECTION).extract()


        #isbn from ean
        #livre['isbn'] =  response.xpath().extract()
        #livre['type_livre'] =  response.xpath().extract()
        #livre['format_livre'] =  response.xpath().extract()
        #livre['poids'] =  response.xpath().extract()
        #livre['preface'] =  response.xpath().extract()


        yield(livre)
