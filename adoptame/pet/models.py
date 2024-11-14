from django.db import models
from django.contrib.auth.models import User

class Specie(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField("Raza", max_length=50)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField('Name of the pet',  max_length=50)
    age = models.IntegerField('Age in years', default=0)
    description = models.TextField('General description', blank=True, null=True)
    adopted = models.BooleanField('Is adopted?', null=True)
    create_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name="Owner", related_name='pets', on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, related_name='pets', verbose_name="Pet's specie", on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='pets', verbose_name="Pet's race", null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='pet_images', blank=True, null=True)
