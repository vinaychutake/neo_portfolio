# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('status', models.BooleanField(default=False, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('db_type', models.CharField(default=b'Other', max_length=20, choices=[(b'NoSql', b'NoSql'), (b'RDBMS', b'RDBMS'), (b'Other', b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('description', ckeditor.fields.RichTextField(default=b'Description of project')),
                ('url', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to=b'', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=False, help_text=b'Select if the project is activeself.', max_length=1)),
                ('order_sequence', models.IntegerField(default=0)),
                ('client_name', models.CharField(max_length=60, null=True, blank=True)),
                ('localization', models.BooleanField(default=False, help_text=b' ::- need to add.')),
                ('production_link', models.CharField(max_length=100, null=True, blank=True)),
                ('dev_link', models.CharField(max_length=100, null=True, blank=True)),
                ('created_by', models.CharField(max_length=100, null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='portfolio.Category', null=True)),
                ('database_used', models.ManyToManyField(to='portfolio.Database')),
            ],
            options={
                'ordering': ['order_sequence'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('images', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('symbol', models.ImageField(upload_to=b'', blank=True)),
                ('description', models.CharField(default=b'', max_length=60, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Versioning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Versioning',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(to='portfolio.ProjectImage'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='portfolio.Technology'),
        ),
        migrations.AddField(
            model_name='project',
            name='third_party_library',
            field=models.ManyToManyField(to='portfolio.Library'),
        ),
        migrations.AddField(
            model_name='project',
            name='version_control',
            field=models.ForeignKey(to='portfolio.Versioning', null=True),
        ),
    ]
