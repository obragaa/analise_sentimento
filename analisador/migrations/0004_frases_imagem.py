# Generated by Django 5.0.4 on 2024-04-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisador', '0003_frases_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='frases',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/%Y/%m/%d/'),
        ),
    ]
