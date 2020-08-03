from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.functional import cached_property
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from PIL import Image as pImage
from PIL.ExifTags import TAGS
from gallery import settings
from pathlib import Path
from datetime import datetime
from django_countries.fields import CountryField
import os


class Image(models.Model):
#Parameters
    title = models.CharField(max_length=250)
    date = models.CharField(blank=True,null=True,max_length=300,verbose_name='Specific Date(s)')
#Culture Options
    GREEK = 'GK'
    ROMAN = 'R'
    EGYPTIAN = 'EG'
    ETRUSCAN = 'ET'
    PHOENICIAN = 'PH'
    ANATOLIAN = 'AN'
    PERSIAN = 'PR'
    MACEDONIAN = 'MC'
    GALLIC = 'GA'
    HYBRID = 'HY'
    CULTURE_OTHER = 'CO'
    culture_choices = [
	(GREEK, 'Greek'),
	(ROMAN, 'Roman'),
	(EGYPTIAN, 'Egyptian'),
	(ETRUSCAN, 'Etruscan'),
	(PHOENICIAN, 'Phoenician'),
	(ANATOLIAN, 'Anatolian'),
	(PERSIAN, 'Persian'),
	(MACEDONIAN, 'Macedonian'),
	(GALLIC, 'Gallic'),
	(HYBRID, 'Hybrid'),
	(CULTURE_OTHER, 'Other'),
    ]
    culture = models.CharField(max_length=2,choices=culture_choices,null=True)
#Period Options
    GENERAL = 'GN'
    EARLY = 'ER'
    MIDDLE = 'MD'
    LATE = 'LT'
    period_prefix_choices = [
	(GENERAL, 'General'),
	(EARLY, 'Early'),
	(MIDDLE, 'Middle'),
	(LATE, 'Late'),
    ]
    period_prefix = models.CharField(max_length=2, choices=period_prefix_choices,blank=True,null=True)

    BRONZE = 'BR'
    IRON_EARLY_GREEK = 'IG'
    ARCHAIC = 'AC'
    CLASSICAL = 'CL'
    HELLENISTIC = 'HL'
    ETRUSCAN_MONARCHY = 'EM'
    ROMAN_REPUBLIC = 'RR'
    ROMAN_EMPIRE = 'RE'
    LATE_ANTIQUE = 'LA'
    PERIOD_OTHER = 'PO'
    period_choices = [
	(BRONZE, 'Bronze Age'),
	(IRON_EARLY_GREEK, 'Iron Age/Early Greek'),
	(ARCHAIC, 'Archaic'),
	(CLASSICAL, 'Classical'),
	(HELLENISTIC, 'Hellenistic'),
	(ETRUSCAN_MONARCHY, 'Etruscan/Monarchy'),
	(ROMAN_REPUBLIC, 'Roman Republic'),
	(ROMAN_EMPIRE, 'Roman Empire'),
	(LATE_ANTIQUE, 'Late Antique'),
	(PERIOD_OTHER, 'Other'),
    ]
    period = models.CharField(max_length=2, choices=period_choices,null=True)
#Object Type
    VASES_VESSELS = 'VV'
    STATUES_BUSTS = 'SB'
    ARCHITECTURAL_SCULPTURE = 'AS'
    RELIEF_SCULPTURE = 'RS'
    INSCRIPTIONS = 'IS'
    MOSAICS = 'MS'
    COINS = 'CS'
    PAINTING = 'PT'
    SARCOPHAGUS = 'SC'
    JEWELRY_BEAUTY = 'JB'
    TOOLS_WEAPONS = 'TW'
    LAMPS = 'LP'
    FIGURINES_VOTIVES = 'FV'
    PLANS_PHOTOS = 'PP'
    MODELS_RECONSTRUCTIONS = 'MR' 
    OBJECT_OTHER = 'OO'
    object_type_choices = [
	(VASES_VESSELS, 'Vases & Vessels'),
	(STATUES_BUSTS, 'Statues & Busts'),
	(ARCHITECTURAL_SCULPTURE, 'Architectural Sculpture'),
	(RELIEF_SCULPTURE, 'Relief Sculpture'),
	(INSCRIPTIONS, 'Inscriptions'),
	(MOSAICS, 'Mosaics'),
	(COINS, 'Coins'),
	(PAINTING, 'Painting'),
	(SARCOPHAGUS, 'Sarcophagus'),
	(JEWELRY_BEAUTY, 'Jewelry & Beauty'),
	(TOOLS_WEAPONS, 'Tools & Weapons'),
	(LAMPS, 'Lamps'),
	(FIGURINES_VOTIVES, 'Figurines & Votives'),
	(PLANS_PHOTOS, 'Plans & Photos'),
	(MODELS_RECONSTRUCTIONS, 'Models & Reconstructions'),
	(OBJECT_OTHER, 'Other'),
    ]   
    object_type = models.CharField(max_length=2,choices=object_type_choices,null=True)
#Vase Technique
    HAND_THROWN = 'HT'
    GEOMETRIC = 'GM'
    BLACK_FIGURE = 'BF'
    RED_FIGURE = 'RF'
    STAMPED = 'SM'
    MOLD_MADE = 'MM'
    WHITE_GROUND = 'WG'
    COOKWARE = 'CW'
    UNDECORATED = 'UD'
    VTECH_OTHER = 'TO'
    vase_technique_choices = [
	(GEOMETRIC, 'Geometric/Proto-Geometric'),
	(BLACK_FIGURE, 'Black-Figure'),
	(RED_FIGURE, 'Red-Figure'),
	(WHITE_GROUND, 'White-Ground'),
	(MOLD_MADE, 'Mold-Made'),
	(STAMPED, 'Stamped'),
	(UNDECORATED, 'Undecorated'),
	(COOKWARE, 'Cookware'),
	(HAND_THROWN, 'Hand-Thrown'),
	(VTECH_OTHER, 'Other'),
    ]
    vase_technique = models.CharField(max_length=2,choices=vase_technique_choices,blank=True,null=True,)
#Vase Shape
    AMPHORA = 'AMP'
    KRATER = 'KRA'
    HYDRIA = 'HYD'
    KYLIX = 'KYL'
    PITHOS = 'PIT'
    KANTHAROS = 'KAN'
    OLPE = 'OLP'
    OINOCHOE = 'OIN'
    LEBES_GAMIKOS = 'LEB'
    PELIKE = 'PEL'
    STAMNOS = 'STA'
    DINOS = 'DIN'
    PSYKTER = 'PSY'
    PLATE = 'PLA'
    PHIALE = 'PHI'
    RHYTON = 'RHY'
    MASTOS = 'MAS'
    SKYPHOS = 'SKY'
    ALABASTRON = 'ALA'
    ARYBALLOS = 'ARY'
    LEKYTHOS = 'LEK'
    LOUTROPHOROS = 'LOU'
    PYXIS = 'PYX'
    VSHAPE_OTHER = 'VSO'
    vase_shape_choices = [
	(AMPHORA, 'Amphora'),
	(KRATER, 'Krater'),
	(HYDRIA, 'Hydria'),
	(KYLIX, 'Kylix'),
	(PITHOS, 'Pithos'),
	(KANTHAROS, 'Kantharos'),
	(OLPE, 'Olpe'),
	(OINOCHOE, 'Oinochoe'),
	(LEBES_GAMIKOS, 'Lebes Gamikos'),
	(PELIKE, 'Pelike'),
	(STAMNOS, 'Stamnos'),
	(DINOS, 'Dinos'),
	(PSYKTER, 'Psykter'),
	(PLATE, 'Plate'),
	(PHIALE, 'Phiale'),
	(RHYTON, 'Rhyton'),
	(MASTOS, 'Mastos'),
	(SKYPHOS, 'Skyphos'),
	(ALABASTRON, 'Alabastron'),
	(ARYBALLOS, 'Aryballos'),
	(LEKYTHOS, 'Lekythos'),
	(LOUTROPHOROS, 'Loutrophoros'),
	(PYXIS, 'Pyxis'),
	(VSHAPE_OTHER, 'Other'),
    ]
    vase_shape = models.CharField(max_length=3,choices=vase_shape_choices,blank=True,null=True,)
#Material
    STONE = 'ST'
    TERRACOTTA = 'TC'
    BONE = 'BN'
    GLASS = 'GL'
    IVORY = 'IV'
    WOOD = 'WD'
    FRESCO = 'FR'
    MARBLE = 'MR'
    MARBLE_BRONZE = 'MB'
    MARBLE_LEAD = 'ML'
    METAL_GOLD = 'MG'
    METAL_SILVER = 'MS'
    METAL_OTHER = 'MO'
    ORGANIC = 'OG'
    NO_ANSWER = 'NA'
    OTHER_UNKNOWN = 'OU'
    material_choices = [
        (STONE,'Stone'),
        (TERRACOTTA,'Terracotta'),
        (BONE,'Bone'),
        (GLASS,'Glass'),
        (IVORY,'Ivory'),
        (WOOD,'Wood'),
        (FRESCO,'Fresco'),
        (MARBLE,'Marble'),
        (MARBLE_BRONZE,'Marble-Bronze'),
        (MARBLE_LEAD,'Marble-Lead'),
        (METAL_GOLD,'Metal-Gold'),
        (METAL_SILVER,'Metal-Silver'),
        (METAL_OTHER,'Metal-Other'),
        (ORGANIC,'Organic'),
        (NO_ANSWER,'N/A'),
        (OTHER_UNKNOWN,'Other/Unknown'),
    ]
    material = models.CharField(max_length=2,choices=material_choices,null=True)
#country
    country = CountryField(blank_label='(Country of Origin)',blank=True,null=True)
#Artist/Attribution
    artist_or_attribution = models.CharField(max_length=150,blank=True,null=True)
#CHANGED
#Associated Building/site
#   MYCENAE = 'MY'
#   ATHENIAN_ACROPOLIS = 'AA'
#   PARTHENON = 'PR'
#   PANTHEON = 'PN'
#   ALTAR_OF_GODS = 'AG'
#   EPHESOS = 'EP'
#   APHRODISIAS = 'AD'
#   SEBASTEION = 'SB'
#   PERGAMON = 'PG'
#   PERGE = 'PE'
#   SAGALASSOS = 'SG'
#   TEMPLE_ZEUS = 'TZ'
#   OLYMPIA = 'OA'
#   CORINTH = 'CR'
#   ROMAN_FORUM = 'RF'
#   ATHENS = 'AT'
#   ROME = 'RM'
#   POMPEII = 'PI'
#   ARA_PACIS = 'AP'
#   BUILDING_OTHER='BO'
#   associated_building_choices = [
#       (MYCENAE, 'Mycenae'),
#       (ATHENIAN_ACROPOLIS, 'Athenian Acropolis'),
#       (PARTHENON, 'Parthenon'),
#       (PANTHEON, 'Pantheon'),
#       (ALTAR_OF_GODS, 'Altar of the Gods (Pergamon)'),
#       (EPHESOS, 'Ephesos'),
#       (APHRODISIAS, 'Aphrodisias'),
#       (SEBASTEION, 'Sebasteion (Aphrodisias)'),
#       (PERGAMON, 'Pergamon'),
#       (PERGE, 'Perge'),
#       (SAGALASSOS, 'Sagalassos'),
#       (TEMPLE_ZEUS, 'Temple of Zeus (Olympia)'),
#       (OLYMPIA, 'Olympia'),
#       (CORINTH, 'Corinth'),
#       (ROMAN_FORUM, 'Roman Forum'),
#       (ATHENS, 'Athens'),
#       (ROME, 'Rome'),
#       (POMPEII, 'Pompeii'),
#       (ARA_PACIS, 'Ara Pacis'),
#       (BUILDING_OTHER,'Other'),
#   ]
#   associated_building = models.CharField(max_length=2, choices=associated_building_choices,blank=True,null=True)

    associated_building = models.CharField(max_length=300,blank=True,null=True)
    associated_site = models.CharField(max_length=300,blank=True,null=True)

#subject
    MYTH = 'MY'
    DAILY_LIFE = 'DL'
    POLITICS = 'PL'
    RITUAL = 'RT'
    DECORATIVE = 'DC'
    MILITARY = 'ML'
    FUNERARY = 'FN'
    SUBJECT_OTHER = 'SO'
    subject_choices = [
        (MYTH, 'Myth'),
        (DAILY_LIFE, 'Daily Life'),
        (POLITICS, 'Politics'),
        (RITUAL, 'Ritual'),
        (DECORATIVE, 'Decorative'),
        (MILITARY, 'Military'),
        (FUNERARY, 'Funerary'),
        (SUBJECT_OTHER, 'Other'),
    ]
    subject = models.CharField(max_length=2, choices=subject_choices,null=True)
#Description
    description = models.TextField(default = 'No description added',null=True)
#Museum Collection
    ATHENS_NATIONAL_MUSEUM = 'ANM'
    ATHENIAN_ACROPOLIS_MUSEUM = 'AAM'
    GETTY_VILLA = 'GTV'
    SAN_ANTONIO_MUSEUM = 'SAM'
    CAPITOLINE_MUSEUM = 'CPM'
    MONTEMARTINI = 'MMI'
    ANTAKYA = 'ATK'
    ANTALYA = 'ANT'
    OLYMPIA = 'OLY'
    APHRODISAS = 'APH'
    EPHESOS = 'EPH'
    CORINTH = 'COR'
    ISTANBUL = 'IST'
    ISTHMIA = 'IMA'
    NEMEA = 'NMA'
    PERGAMON_MUSEUM = 'PMB'
    SEVILLE = 'SVL'
    HOUSTON_GLADIATOR_EXHIBIT = 'HGE'
    VATICAN_MUSEUM = 'VTM'
    ZEUGMA = 'ZGM'
    MYCENAE = 'MYC'
    DELPHI = 'DEL'
    ELEUSIS = 'ELE'
    HIERAPOLIS = 'HPS'
    BERGAMA = 'BMA'
    PELLA = 'PLA'
    VERGINA = 'VGA'
    IZMIR = 'IZM'
    EPIDAUROS = 'EPI'
    BOSTON_MUSEUM_FINE_ARTS = 'BMF'
    SAGALASSOS = 'SAG'
    MUSEUM_OTHER = 'MUO'
    museum_collection_choices = [
        (ATHENS_NATIONAL_MUSEUM, 'Athens National Museum'),
        (ATHENIAN_ACROPOLIS_MUSEUM, 'Athenian Acropolis Museum'),
        (GETTY_VILLA, 'Getty Villa'),
        (SAN_ANTONIO_MUSEUM, 'San Antonio Museum of Art'),
        (CAPITOLINE_MUSEUM, 'Capitoline Museum'),
        (MONTEMARTINI, 'Montemartini (Rome)'),
        (ANTAKYA, 'Antakya'),
        (ANTALYA, 'Antalya'),
        (OLYMPIA, 'Olympia'),
        (APHRODISAS, 'Aphrodisas'),
        (EPHESOS, 'Ephesos'),
        (CORINTH, 'Corinth'),
        (ISTANBUL, 'Istanbul'),
        (ISTHMIA, 'Isthmia'),
        (NEMEA, 'Nemea'),
        (PERGAMON_MUSEUM, 'Pergamon Museum (Berlin)'),
        (SEVILLE, 'Seville'),
        (HOUSTON_GLADIATOR_EXHIBIT, 'Houston Gladiator Exhibit'),
        (VATICAN_MUSEUM, 'Vatican Museum'),
        (ZEUGMA, 'Zeugma'),
        (MYCENAE, 'Mycenae'),
        (DELPHI, 'Delphi'),
        (ELEUSIS, 'Eleusis'),
        (HIERAPOLIS, 'Hierapolis'),
        (BERGAMA, 'Bergama'),
        (PELLA, 'Pella'),
        (VERGINA, 'Vergina'),
        (IZMIR, 'Izmir'),
        (EPIDAUROS, 'Epidauros'),
        (BOSTON_MUSEUM_FINE_ARTS, 'Boston Museum of Fine Arts'),
        (SAGALASSOS, 'Sagalassos'),
        (MUSEUM_OTHER,'Other'),
    ]
    museum_collection = models.CharField(max_length=3,choices=museum_collection_choices,null=True)
#boolean validation
    is_validated = models.BooleanField(default=False)
    incomplete_info = models.BooleanField(default=True)


    data = models.ImageField(upload_to='images')
    data_thumbnail = ImageSpecField(source='data',
                                    processors=[ResizeToFit(
                                        height=settings.GALLERY_THUMBNAIL_SIZE * settings.GALLERY_HDPI_FACTOR)],
                                    format='JPEG',
                                    options={'quality': settings.GALLERY_RESIZE_QUALITY})
    data_preview = ImageSpecField(source='data',
                                  processors=[ResizeToFit(width=settings.GALLERY_PREVIEW_SIZE * settings.GALLERY_HDPI_FACTOR,
                                                          height=settings.GALLERY_PREVIEW_SIZE * settings.GALLERY_HDPI_FACTOR)],
                                  format='JPEG',
                                  options={'quality': settings.GALLERY_RESIZE_QUALITY})
    date_uploaded = models.DateTimeField(auto_now_add=True)

    @cached_property
    def slug(self):
        return slugify(self.title)

    @cached_property
    def exif(self):
        exif_data = {}
        self.data.open()
        with pImage.open(self.data) as img:
            if hasattr(img, '_getexif'):
                info = img.getexif()
                if not info:
                    return {}
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    exif_data[decoded] = value
                # Process some data for easy rendering in template
                exif_data['Camera'] = exif_data.get('Model', '')
                if exif_data.get('Make', '') not in exif_data['Camera']:  # Work around for Canon
                    exif_data['Camera'] = "{0} {1}".format(exif_data['Make'].title(), exif_data['Model'])
                if 'FNumber' in exif_data:
                    exif_data['Aperture'] = str(exif_data['FNumber'].numerator / exif_data['FNumber'].denominator)
                if 'ExposureTime' in exif_data:
                    exif_data['Exposure'] = "{0}/{1}".format(exif_data['ExposureTime'].numerator,
                                                             exif_data['ExposureTime'].denominator)
            img.close()
        return exif_data

    @cached_property
    def date_taken(self):
        original_exif = self.exif.get('DateTimeOriginal')
        if not original_exif:
            return self.mtime
        try:
            return datetime.strptime(original_exif, "%Y:%m:%d %H:%M:%S")
        except ValueError:  # Fall back to file modification time
            return self.mtime

    @cached_property
    def mtime(self):
        return datetime.fromtimestamp(os.path.getmtime(self.data.path))


    def get_absolute_url(self):
        return reverse('gallery:image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    images = models.ManyToManyField(Image, blank=True, related_name='image_albums')
    highlight = models.OneToOneField(Image,
                                     related_name='album_highlight',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order', '-pk']

    @property
    def slug(self):
        return slugify(self.title)

    @property
    def display_highlight(self):
        # if there is no highlight but there are images in the album, use the first
        if not self.highlight and self.images.count():
            image = self.images.earliest('id')
        else:
            image = self.highlight
        if image:
            image.title = self.title  # use the album title instead of the highlight title
            image.description = self.description
        return image

    def get_absolute_url(self):
        return reverse('gallery:album_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title
