from django.db import models

# Create your models here.

class Materia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=False, blank=True, max_length=2)
    descripcion = models.TextField(blank=True, null=True)
    correlativas = models.ManyToManyField('self',
                                          symmetrical=False,
                                          blank=True,
                                          related_name='materias_dependientes')
    

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
