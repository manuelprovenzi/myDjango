# Generated by Django 4.2.1 on 2023-06-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appManu', '0005_alter_cd_azienda_alter_cd_prezzo'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('idCitta', models.IntegerField(primary_key=True, serialize=False)),
                ('nomeCitta', models.CharField(max_length=255, null=True)),
                ('nomeProvincia', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]