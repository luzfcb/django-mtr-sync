# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('office', models.CharField(verbose_name='office', max_length=255)),
                ('address', models.CharField(verbose_name='address', max_length=255)),
            ],
            options={
                'verbose_name': 'office',
                'verbose_name_plural': 'offices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('surname', models.CharField(verbose_name='surname', max_length=255)),
                ('gender', models.CharField(verbose_name='gender', choices=[('M', 'Male'), ('F', 'Female')], max_length=255)),
                ('security_level', models.PositiveIntegerField(verbose_name='security level')),
                ('some_excluded_field', models.DecimalField(verbose_name='some decimal', decimal_places=3, null=True, max_digits=10)),
                ('office', models.ForeignKey(to='app.Office', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='tag', max_length=255)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
            preserve_default=True,
        ),
    ]
