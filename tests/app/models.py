import random

from django.utils.encoding import python_2_unicode_compatible
from django.utils import six
from django.utils.six.moves import range
from django.db import models


@python_2_unicode_compatible
class Office(models.Model):
    office = models.CharField('office', max_length=255)
    address = models.CharField('address', max_length=255)

    def __str__(self):
        return self.office

    class Meta:
        verbose_name = 'office'
        verbose_name_plural = 'offices'


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField('tag', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField('name', max_length=255)
    surname = models.CharField('surname', max_length=255)
    gender = models.CharField('gender', max_length=255, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    security_level = models.PositiveIntegerField('security level')
    some_excluded_field = models.DecimalField(
        'some decimal', max_digits=10, decimal_places=3, null=True)

    office = models.ForeignKey(Office, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def populate(self, num=100):
        for i in range(num):
            name = list(self.name)
            random.shuffle(name)
            name = ''.join(name)

            surname = list(self.surname)
            random.shuffle(surname)
            surname = ''.join(surname)

            newobj = self.__class__(
                name=name,
                office=self.office,
                surname=surname,
                gender=random.choice(['M', 'F']),
                security_level=random.choice(range(100))
            )
            newobj.save()
            newobj.tags.add(*self.tags.all())
            newobj.save()
        self.save()

    @property
    def custom_method(self):
        return six.text_type('{}-{}').format(self.name, self.surname)

    @custom_method.setter
    def custom_method(self, value):
        self.name, self.surname = value.split('-')

    @property
    def none_param(self):
        return None

    @none_param.setter
    def none_param(self, value):
        pass

    def __str__(self):
        return self.name

    @classmethod
    def some_queryset(model, settings):
        return model.objects.filter(security_level__gte=30)

    # TODO: fix description
    # some_queryset.short_description = 'some description'

    sync_settings = {
        'custom_fields': ['custom_method', 'none_param'],
        'exclude': ['some_excluded_field'],
        'querysets': ['some_queryset']
    }
