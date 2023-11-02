from django.db import models
from django.contrib.auth.models import User

class Specie(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField('Name of the pet',  max_length=50)
    age = models.IntegerField('Age in years', default=0)
    description = models.TextField('General description', blank=True, null=True)
    adopted = models.BooleanField('Is adopted?')
    create_at = models.DateField(auto_now_add=False)
    created_by = models.ForeignKey(User, verbose_name="Owner", related_name='pets', on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, related_name='pets', verbose_name="Pet's specie", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_images', blank=True, null=True)
