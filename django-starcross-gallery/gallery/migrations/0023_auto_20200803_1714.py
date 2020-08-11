# Generated by Django 3.0.7 on 2020-08-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0022_auto_20200803_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='culture',
            field=models.CharField(choices=[('GK', 'Greek'), ('R', 'Roman'), ('EG', 'Egyptian'), ('ET', 'Etruscan'), ('PH', 'Phoenician'), ('AN', 'Anatolian'), ('PR', 'Persian'), ('MC', 'Macedonian'), ('GA', 'Gallic'), ('HY', 'Hybrid'), ('CO', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='material',
            field=models.CharField(choices=[('ST', 'Stone'), ('TC', 'Terracotta'), ('BN', 'Bone'), ('GL', 'Glass'), ('IV', 'Ivory'), ('WD', 'Wood'), ('FR', 'Fresco'), ('MR', 'Marble'), ('MB', 'Marble-Bronze'), ('ML', 'Marble-Lead'), ('MG', 'Metal-Gold'), ('MS', 'Metal-Silver'), ('MO', 'Metal-Other'), ('OG', 'Organic'), ('NA', 'N/A'), ('OU', 'Other/Unknown')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='museum_collection',
            field=models.CharField(choices=[('ANM', 'Athens National Museum'), ('AAM', 'Athenian Acropolis Museum'), ('GTV', 'Getty Villa'), ('SAM', 'San Antonio Museum of Art'), ('CPM', 'Capitoline Museum'), ('MMI', 'Montemartini (Rome)'), ('ATK', 'Antakya'), ('ANT', 'Antalya'), ('OLY', 'Olympia'), ('APH', 'Aphrodisas'), ('EPH', 'Ephesos'), ('COR', 'Corinth'), ('IST', 'Istanbul'), ('IMA', 'Isthmia'), ('NMA', 'Nemea'), ('PMB', 'Pergamon Museum (Berlin)'), ('SVL', 'Seville'), ('HGE', 'Houston Gladiator Exhibit'), ('VTM', 'Vatican Museum'), ('ZGM', 'Zeugma'), ('MYC', 'Mycenae'), ('DEL', 'Delphi'), ('ELE', 'Eleusis'), ('HPS', 'Hierapolis'), ('BMA', 'Bergama'), ('PLA', 'Pella'), ('VGA', 'Vergina'), ('IZM', 'Izmir'), ('EPI', 'Epidauros'), ('BMF', 'Boston Museum of Fine Arts'), ('SAG', 'Sagalassos'), ('MUO', 'Other')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='object_type',
            field=models.CharField(choices=[('VV', 'Vases & Vessels'), ('SB', 'Statues & Busts'), ('AS', 'Architectural Sculpture'), ('RS', 'Relief Sculpture'), ('IS', 'Inscriptions'), ('MS', 'Mosaics'), ('CS', 'Coins'), ('PT', 'Painting'), ('SC', 'Sarcophagus'), ('JB', 'Jewelry & Beauty'), ('TW', 'Tools & Weapons'), ('LP', 'Lamps'), ('FV', 'Figurines & Votives'), ('PP', 'Plans & Photos'), ('MR', 'Models & Reconstructions'), ('OO', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='period',
            field=models.CharField(choices=[('BR', 'Bronze Age'), ('IG', 'Iron Age/Early Greek'), ('AC', 'Archaic'), ('CL', 'Classical'), ('HL', 'Hellenistic'), ('EM', 'Etruscan/Monarchy'), ('RR', 'Roman Republic'), ('RE', 'Roman Empire'), ('LA', 'Late Antique'), ('PO', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='subject',
            field=models.CharField(choices=[('MY', 'Myth'), ('DL', 'Daily Life'), ('PL', 'Politics'), ('RT', 'Ritual'), ('DC', 'Decorative'), ('ML', 'Military'), ('FN', 'Funerary'), ('SO', 'Other')], max_length=2, null=True),
        ),
    ]