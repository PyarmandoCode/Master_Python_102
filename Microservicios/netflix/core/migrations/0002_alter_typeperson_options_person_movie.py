# Generated by Django 5.0 on 2024-08-23 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeperson',
            options={'ordering': ['type'], 'verbose_name': 'TypePerson', 'verbose_name_plural': 'Tipo_de_Personas'},
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=180)),
                ('firstname', models.CharField(max_length=180)),
                ('aliases', models.CharField(blank=True, max_length=80, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person')),
                ('state', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('typepersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='core.typeperson')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Personas',
                'ordering': ['firstname'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=180)),
                ('sipnosis', models.TextField(blank=True, null=True)),
                ('release_year', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('genre', models.CharField(choices=[('Horro', 'Horro'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Scifi', 'Scifi'), ('Action', 'Action')], max_length=10)),
                ('top', models.ImageField(blank=True, null=True, upload_to='movies')),
                ('state', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Actor_Actress', models.ManyToManyField(related_name='actor_actress', to='core.person')),
                ('Director', models.ManyToManyField(related_name='director', to='core.person')),
                ('Producer', models.ManyToManyField(related_name='producer', to='core.person')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Peliculas',
                'ordering': ['title'],
            },
        ),
    ]